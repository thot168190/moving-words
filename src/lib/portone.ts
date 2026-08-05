// ============================================================
// 포트원 V2 설정
// ============================================================
// storeId / channelKey 는 공개키다. API Secret 은 절대 여기 넣지 않는다.
// payMethod 는 채널의 PG사에 따라 다르다 — .env 로 전환한다.
//   · 카카오페이 채널 → EASY_PAY (+ easyPayProvider: KAKAOPAY)
//   · KPN / 카드 채널 → CARD
// ============================================================

export const PORTONE_CONFIG = {
  storeId: import.meta.env.VITE_PORTONE_STORE_ID || '',
  channelKey: import.meta.env.VITE_PORTONE_CHANNEL_KEY || '',
  payMethod: (import.meta.env.VITE_PORTONE_PAY_METHOD || 'CARD') as string,
  easyPayProvider: (import.meta.env.VITE_PORTONE_EASYPAY_PROVIDER || '') as string,
  redirectUrl: typeof window !== 'undefined' ? `${window.location.origin}/payment/success` : '',
};

export function generatePaymentId(): string {
  // ⛔ 하이픈·언더바 금지.
  // KPN 규칙: ALLOWED_CHARACTERS(upper=true, lower=true, digits=true, otherCharacters="")
  // 영문 대소문자와 숫자만 허용한다. 하이픈을 넣으면 결제창 호출이 실패한다.
  const t = Date.now().toString(36);
  const r = Math.random().toString(36).slice(2, 10);
  return `payment${t}${r}`.replace(/[^A-Za-z0-9]/g, '');
}
