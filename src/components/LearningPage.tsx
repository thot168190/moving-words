import { useEffect, useRef, useState } from 'react';
import { AuthModal } from './AuthModal';
import { useAuth } from '../contexts/AuthContext';

type SceneCompleteMessage = {
  type: 'inkword:scene-complete' | 'inkword:logout';
  sceneId?: string;
  wordIds?: string[];
};

/**
 * 로그인 후 사용하는 실제 학습장입니다.
 * 학습장 화면은 독립된 HTML로 유지해 디자인 수정이 쉽고,
 * 완료 기록만 안전한 메시지로 React/Firebase에 전달합니다.
 */
export default function LearningPage() {
  const { user, loading, learningProgress, recordSceneCompletion, signOut } = useAuth();
  const [authOpen, setAuthOpen] = useState(false);
  const frameRef = useRef<HTMLIFrameElement>(null);

  const sendAccountState = () => {
    if (!user) return;
    frameRef.current?.contentWindow?.postMessage(
      {
        type: 'inkword:init',
        user: {
          displayName: user.displayName,
          email: user.email,
          photoURL: user.photoURL,
        },
        progress: learningProgress,
      },
      window.location.origin,
    );
  };

  useEffect(() => {
    const receiveLearningEvent = (event: MessageEvent<SceneCompleteMessage>) => {
      if (event.origin !== window.location.origin) return;
      if (event.data?.type === 'inkword:logout') {
        void signOut();
        return;
      }
      if (event.data?.type !== 'inkword:scene-complete' || !event.data.sceneId) return;
      void recordSceneCompletion(event.data.sceneId, event.data.wordIds || []);
    };
    window.addEventListener('message', receiveLearningEvent);
    return () => window.removeEventListener('message', receiveLearningEvent);
  }, [recordSceneCompletion, signOut]);

  useEffect(sendAccountState, [user, learningProgress]);

  if (loading) {
    return <div className="min-h-screen bg-white" aria-label="학습장 불러오는 중" />;
  }

  if (!user) {
    return (
      <main className="min-h-screen bg-white text-[#07533f] flex items-center justify-center px-6 font-pretendard">
        <section className="w-full max-w-[560px] text-center">
          <a href="/" className="inline-block text-[18px] font-black text-[#07533f] no-underline mb-14">보는 단어장</a>
          <p className="text-[13px] font-bold tracking-[0.18em] text-[#3d8f73] mb-4">MY LEARNING</p>
          <h1 className="text-[clamp(36px,7vw,62px)] leading-[1.12] font-black tracking-[-0.05em] mb-6">내 학습장으로<br />이어갈게요.</h1>
          <p className="text-[#3d4541] text-[17px] leading-7 mb-10">로그인하면 학습한 장면과 모은 단어 카드가<br className="hidden sm:block" /> 계정에 계속 기록됩니다.</p>
          <button onClick={() => setAuthOpen(true)} className="h-14 px-10 rounded-full border-0 bg-[#07533f] text-white text-[17px] font-black cursor-pointer">로그인하고 학습하기</button>
        </section>
        <AuthModal isOpen={authOpen} onClose={() => setAuthOpen(false)} />
      </main>
    );
  }

  return (
    // 정적 학습장 파일을 수정했을 때 브라우저의 이전 캐시가 남지 않도록
    // 화면 버전을 주소에 함께 표시합니다. 배포 후 즉시 최신 지도를 불러옵니다.
    <iframe
      ref={frameRef}
      title="보는 단어장 실제 학습장"
      src="/learning/index.html?v=20260719-20"
      onLoad={sendAccountState}
      className="fixed inset-0 w-full h-full border-0 bg-white"
      allow="autoplay; microphone"
    />
  );
}
