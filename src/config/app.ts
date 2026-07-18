/**
 * 랜딩페이지에서 실제 학습 앱으로 이동할 때 사용하는 단일 진입점입니다.
 *
 * 기본값은 이 저장소에 포함된 학습장(/#learn)입니다. 랜딩과 앱을 서로
 * 다른 도메인으로 배포할 때만 VITE_APP_ENTRY_URL을 설정하면 됩니다.
 */
export const APP_ENTRY_URL =
  import.meta.env.VITE_APP_ENTRY_URL?.trim() || '/#learn';
