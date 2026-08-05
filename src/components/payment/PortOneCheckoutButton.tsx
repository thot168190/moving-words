// ============================================================
// 포트원 V2 결제 버튼 (KPN 채널 · 인증 단건결제)
// ============================================================
// ⛔ 수정 금지 사항 (로부장 2026-08-04 확정)
//  - payMethod 는 .env 로 정한다. 코드에 박지 않는다.
//      카카오페이 채널 → EASY_PAY(+easyPayProvider)  ·  KPN/카드 채널 → CARD
//    KPN 서브몰 심사자료는 「인증 단건결제 → 카드사 인증창 → 하나카드 결제창」을 요구하므로,
//    KPN 채널이 생기면 .env 의 VITE_PORTONE_PAY_METHOD 를 CARD 로 바꾼다.
//  - alert / confirm / prompt 사용 금지. 페이지를 정지시켜 진단을 막는다.
//  - storeId / channelKey 하드코딩 금지. .env 만 사용한다.
//  - 버튼 문구·가격·디자인 변경 금지 (카드사·카카오페이 심사 중)
// ============================================================

import React, { useState, useEffect, useCallback } from 'react';
import { PORTONE_CONFIG, generatePaymentId } from '../../lib/portone';

declare global {
  interface Window {
    PortOne?: { requestPayment: (options: any) => Promise<any> };
  }
}

interface PortOneCheckoutButtonProps {
  amount?: number;
  orderName?: string;
  customerEmail?: string;
  customerName?: string;
  onError?: (error: any) => void;
  className?: string;
}

const SDK_SRC = 'https://cdn.portone.io/v2/browser-sdk.js';

const PortOneCheckoutButton: React.FC<PortOneCheckoutButtonProps> = ({
  amount = 9900,
  orderName = '보는 단어장 출시 기념 이용권',
  customerEmail,
  customerName,
  onError,
  className,
}) => {
  const [sdkLoaded, setSdkLoaded] = useState(false);
  const [processing, setProcessing] = useState(false);
  const [errMsg, setErrMsg] = useState('');

  useEffect(() => {
    if (window.PortOne) { setSdkLoaded(true); return; }

    const existing = document.querySelector<HTMLScriptElement>(`script[src="${SDK_SRC}"]`);
    if (existing) {
      existing.addEventListener('load', () => setSdkLoaded(true));
      existing.addEventListener('error', () => setErrMsg('결제 모듈을 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.'));
      return;
    }

    const script = document.createElement('script');
    script.src = SDK_SRC;
    script.async = true;
    script.onload = () => { console.log('[PortOne] SDK loaded'); setSdkLoaded(true); };
    script.onerror = () => {
      console.error('[PortOne] SDK load failed');
      setErrMsg('결제 모듈을 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.');
    };
    document.head.appendChild(script);
  }, []);

  const handlePayment = useCallback(async () => {
    if (processing) return;
    setErrMsg('');

    if (!window.PortOne) {
      console.error('[PortOne] window.PortOne undefined');
      setErrMsg('결제 모듈 준비 중입니다. 잠시 후 다시 눌러 주세요.');
      return;
    }

    const { storeId, channelKey, redirectUrl, payMethod, easyPayProvider } = PORTONE_CONFIG;
    if (!storeId || !channelKey) {
      console.error('[PortOne] missing config', { storeId, channelKey });
      setErrMsg('결제 설정이 누락되었습니다. (storeId / channelKey)');
      return;
    }

    setProcessing(true);
    try {
      const options: any = {
        storeId,
        channelKey,
        paymentId: generatePaymentId(),
        orderName,
        totalAmount: amount,
        currency: 'CURRENCY_KRW',
        payMethod,
        redirectUrl,
        customer: {
          fullName: customerName || '고객',
          email: customerEmail || undefined,
        },
      };
      if (payMethod === 'EASY_PAY' && easyPayProvider) {
        options.easyPay = { easyPayProvider };
      }
      console.log('[PortOne] requestPayment', options);

      const res = await window.PortOne.requestPayment(options);
      console.log('[PortOne] response', res);

      if (res && res.code != null) {
        if (res.code === 'USER_CANCEL') {
          console.log('[PortOne] 사용자 취소');
        } else {
          setErrMsg(`[${res.code}] ${res.message || '결제를 진행하지 못했습니다.'}`);
          onError?.(res.message || res.code);
        }
      }
    } catch (e: any) {
      console.error('[PortOne] exception', e);
      setErrMsg(`[예외] ${e?.message || e?.code || JSON.stringify(e)?.slice(0,200) || String(e)}`);
      onError?.(e);
    } finally {
      setProcessing(false);
    }
  }, [amount, orderName, customerEmail, customerName, processing, onError]);

  return (
    <>
      <button
        onClick={handlePayment}
        disabled={!sdkLoaded || processing}
        className={`
          w-full max-w-none mx-auto h-[68px] rounded-[18px] font-black text-[20px]
          flex items-center justify-center gap-2
          transition-all duration-200 shadow-sm hover:shadow-md
          ${processing
            ? 'bg-[#8BB7A7] cursor-wait'
            : sdkLoaded
              ? 'bg-[#07533F] hover:bg-[#0B684F] active:bg-[#064534] active:scale-[0.97] cursor-pointer'
              : 'bg-neutral-400 cursor-not-allowed'
          }
          text-white border-none
          ${className || ''}
        `}
      >
        {processing ? (
          <>
            <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24" fill="none">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
            </svg>
            <span>결제 처리 중...</span>
          </>
        ) : !sdkLoaded ? (
          <span>로딩 중...</span>
        ) : (
          <>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className="mr-0.5">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <span>₩{amount.toLocaleString()} 시작하기</span>
          </>
        )}
      </button>
      {errMsg && (
        <p style={{ marginTop: 10, color: '#c0392b', fontSize: 14, fontWeight: 700, textAlign: 'center' }}>
          {errMsg}
        </p>
      )}
    </>
  );
};

export default PortOneCheckoutButton;
