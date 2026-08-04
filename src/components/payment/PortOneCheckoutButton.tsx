import React, { useState, useEffect, useCallback } from 'react';

declare global {
  interface Window {
    PortOne?: {
      requestPayment: (options: any) => Promise<any>;
    };
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

// 매또컴퍼니 포트원 V2 Store ID
export const PORTONE_STORE_ID = 'store-04d68797-1bc3-47a4-8254-ff9ee66a532d';

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

  useEffect(() => {
    if (window.PortOne) {
      setSdkLoaded(true);
      return;
    }

    const existing = document.querySelector('script[src*="portone.io"]');
    if (existing) {
      existing.addEventListener('load', () => setSdkLoaded(true));
      return;
    }

    const script = document.createElement('script');
    script.src = 'https://cdn.portone.io/v2/browser-sdk.js';
    script.async = true;
    script.onload = () => setSdkLoaded(true);
    script.onerror = () => onError?.('포트원 SDK 로드 실패');
    document.head.appendChild(script);
  }, []);

  const handlePayment = useCallback(async () => {
    if (!window.PortOne || processing) return;

    setProcessing(true);

    try {
      const paymentId = `payment-${Date.now()}-${Math.random().toString(36).substring(2, 7)}`;
      const response = await window.PortOne.requestPayment({
        storeId: PORTONE_STORE_ID,
        paymentId,
        orderName,
        totalAmount: amount,
        currency: 'CURRENCY_KRW',
        payMethod: 'CARD',
        customer: {
          fullName: customerName || '고객',
          email: customerEmail || undefined,
        },
      });

      if (response && response.code != null) {
        console.log('[PortOne] Payment response/cancel:', response);
        if (response.code !== 'USER_CANCEL') {
          alert(`포트원 결제 안내: ${response.message || '결제창이 닫혔거나 처리되었습니다.'}`);
        }
      } else {
        console.log('[PortOne] Payment Success:', response);
        alert('테스트 결제가 성공적으로 요청되었습니다!');
      }
    } catch (error: any) {
      console.error('[PortOne] Error:', error);
      onError?.(error);
    } finally {
      setProcessing(false);
    }
  }, [amount, orderName, customerEmail, customerName, processing]);

  return (
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
        <span>결제 처리 중...</span>
      ) : !sdkLoaded ? (
        <span>로딩 중...</span>
      ) : (
        <>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className="mr-0.5">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
            <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
          </svg>
          <span>₩{amount.toLocaleString()} 시작하기 (포트원 결제)</span>
        </>
      )}
    </button>
  );
};

export default PortOneCheckoutButton;
