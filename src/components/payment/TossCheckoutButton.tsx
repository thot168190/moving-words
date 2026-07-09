// ============================================================
// 토스페이먼츠 결제 버튼 컴포넌트
// ============================================================
// 토스페이먼츠 JavaScript SDK를 사용한 결제 버튼
// 
// 사용법:
//   <TossCheckoutButton
//     product={product}
//     customerEmail="user@example.com"
//     customerName="홍길동"
//     onError={(err) => console.error(err)}
//   />
// ============================================================

import React, { useState, useEffect, useCallback } from 'react';
import { TOSS_CONFIG, generateOrderId, type TossProduct } from '../../lib/toss';

// 토스페이먼츠 SDK 타입 (외부 스크립트)
declare global {
  interface Window {
    TossPayments?: (clientKey: string) => {
      requestPayment: (method: string, params: any) => Promise<void>;
    };
  }
}

interface TossCheckoutButtonProps {
  product: TossProduct;
  customerEmail?: string;
  customerName?: string;
  customerKey?: string;
  method?: '카드' | '가상계좌' | '계좌이체' | '휴대폰';
  onError?: (error: any) => void;
  className?: string;
}

const TossCheckoutButton: React.FC<TossCheckoutButtonProps> = ({
  product,
  customerEmail,
  customerName,
  customerKey,
  method = '카드',
  onError,
  className,
}) => {
  const [sdkLoaded, setSdkLoaded] = useState(false);
  const [processing, setProcessing] = useState(false);

  // 토스페이먼츠 SDK 로드
  useEffect(() => {
    if (window.TossPayments) {
      setSdkLoaded(true);
      return;
    }

    const existing = document.querySelector('script[src*="tosspayments"]');
    if (existing) {
      existing.addEventListener('load', () => setSdkLoaded(true));
      return;
    }

    const script = document.createElement('script');
    script.src = 'https://js.tosspayments.com/v1/payment';
    script.async = true;
    script.onload = () => setSdkLoaded(true);
    script.onerror = () => onError?.('토스페이먼츠 SDK 로드 실패');
    document.head.appendChild(script);
  }, []);

  // 결제 요청
  const handlePayment = useCallback(async () => {
    if (!window.TossPayments || processing) return;

    setProcessing(true);

    try {
      const tossPayments = window.TossPayments(TOSS_CONFIG.clientKey);
      const orderId = generateOrderId();

      await tossPayments.requestPayment(method, {
        amount: product.price,
        orderId,
        orderName: product.name,
        customerName: customerName || '고객',
        customerEmail: customerEmail || undefined,
        customerKey: customerKey || TOSS_CONFIG.customerKey || undefined,
        successUrl: TOSS_CONFIG.successUrl,
        failUrl: TOSS_CONFIG.failUrl,
      });
    } catch (error: any) {
      // 사용자가 결제창을 닫은 경우
      if (error.code === 'USER_CANCEL') {
        console.log('[Toss] 사용자 취소');
      } else {
        console.error('[Toss] Error:', error);
        onError?.(error);
      }
    } finally {
      setProcessing(false);
    }
  }, [product, customerEmail, customerName, customerKey, method, processing]);

  return (
    <button
      onClick={handlePayment}
      disabled={!sdkLoaded || processing}
      className={`
        w-full max-w-md mx-auto h-[56px] rounded-[16px] font-bold text-[16px]
        flex items-center justify-center gap-2
        transition-all duration-200 shadow-sm hover:shadow-md
        ${processing
          ? 'bg-blue-300 cursor-wait'
          : sdkLoaded
            ? 'bg-[#3182f6] hover:bg-[#1b64da] active:scale-[0.97] cursor-pointer'
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
          <span>₩{product.price.toLocaleString()} 시작하기</span>
        </>
      )}
    </button>
  );
};

export default TossCheckoutButton;
