import { useState, useEffect, useRef } from 'react';
import {
  motion,
} from 'framer-motion';
import { Navbar } from './components/Navbar';
import { ScrambleIn } from './components/ScrambleText';
import { ConnectAILabLogo } from './components/ConnectAILabLogo';
import HeroDoodle from './components/HeroDoodle';
import HeroWords from './components/HeroWords';
import FeatureDoodle from './components/FeatureDoodle';
import WordRain from './components/WordRain';
import TossCheckoutButton from './components/payment/TossCheckoutButton';
import { useAuth } from './contexts/AuthContext';
import { TOSS_PRODUCTS } from './lib/toss';
import { VIDEO_URLS } from './config/videos';
import { SITE_CONFIG } from './config/content';

const PRET = "'Pretendard Variable', Pretendard, -apple-system, sans-serif";
const CARD_COLORS = ['#3b6ba5', '#c2410c', '#2f8f83', '#b98a2f'];

// 랜딩 3번째 영역에서 순서대로 보여줄 학습 영상입니다.
// 영상을 추가하려면 이 배열에만 항목을 추가하면 됩니다.
const LEARNING_PREVIEW_VIDEOS = [
  {
    title: '바람을 타는 범선', src: '/learning-preview/scene-ch1-03.mp4',
    words: [
      { en: 'sail', ko: '돛', x: 48, y: 31 }, { en: 'horizon', ko: '수평선', x: 77, y: 25 },
      { en: 'voyage', ko: '항해', x: 19, y: 65 }, { en: 'current', ko: '해류', x: 70, y: 77 },
    ],
  },
  {
    title: '밤하늘의 별자리', src: '/learning-preview/scene-ch1-05.mp4',
    words: [
      { en: 'telescope', ko: '망원경', x: 31, y: 58 }, { en: 'constellation', ko: '별자리', x: 59, y: 30 },
      { en: 'observe', ko: '관찰하다', x: 77, y: 66 }, { en: 'universe', ko: '우주', x: 20, y: 23 },
    ],
  },
  {
    title: '깊은 바다의 산호 협곡', src: '/learning-preview/scene-ch1-08.mp4',
    words: [
      { en: 'coral', ko: '산호', x: 18, y: 69 }, { en: 'canyon', ko: '협곡', x: 52, y: 69 },
      { en: 'creature', ko: '생물', x: 69, y: 37 }, { en: 'ecosystem', ko: '생태계', x: 80, y: 70 },
    ],
  },
];

export default function App() {
  const [entranceComplete, setEntranceComplete] = useState(false);
  const [previewIndex, setPreviewIndex] = useState(0);
  const [previewProgress, setPreviewProgress] = useState(0);
  const { user, deleteAccount } = useAuth();

  // 그림 위 단어를 누르면 영어 발음을 들려줍니다.
  const speakPreviewWord = (word: string) => {
    if (!window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(word);
    utterance.lang = 'en-US';
    utterance.rate = 0.82;
    window.speechSynthesis.speak(utterance);
  };

  const handleDeleteAccount = async () => {
    const isConfirmed = window.confirm(
      '정말로 회원 탈퇴를 진행하시겠습니까?\\n탈퇴 시 즉시 모든 학습 기록과 계정 정보가 영구 삭제되며, 이 작업은 복구할 수 없습니다.'
    );
    if (!isConfirmed) return;

    try {
      await deleteAccount();
      alert('회원 탈퇴가 완료되었습니다. 그동안 서비스를 이용해 주셔서 감사합니다.');
      window.location.reload();
    } catch (err: any) {
      alert(err.message || '회원 탈퇴 처리 중 오류가 발생했습니다. 다시 시도해 주세요.');
    }
  };

  // 결제 성공/실패 페이지 분기 처리
  const path = window.location.pathname;
  if (path === '/payment/success') {
    return <PaymentSuccessPage />;
  }
  if (path === '/payment/fail') {
    return <PaymentFailPage />;
  }

  /* Hero video mouse scrubbing removed per A 항목 */

  /* ── Entrance delay ── */
  useEffect(() => {
    const timer = setTimeout(() => setEntranceComplete(true), 800);
    return () => clearTimeout(timer);
  }, []);

  /* ── iOS & 모바일 브라우저용 TTS(SpeechSynthesis) 잠금 해제 ── */
  useEffect(() => {
    const unlockTTS = () => {
      if (typeof window !== 'undefined' && window.speechSynthesis) {
        const utterance = new SpeechSynthesisUtterance('');
        window.speechSynthesis.speak(utterance);
        window.removeEventListener('click', unlockTTS);
        window.removeEventListener('touchstart', unlockTTS);
      }
    };
    window.addEventListener('click', unlockTTS);
    window.addEventListener('touchstart', unlockTTS);
    return () => {
      window.removeEventListener('click', unlockTTS);
      window.removeEventListener('touchstart', unlockTTS);
    };
  }, []);

  /* ── Section 2 scroll-driven 3D text ── */
  const section2Ref = useRef<HTMLDivElement>(null);


  /* ── Destructure config for readability ── */
  const { hero, cinematic, metrics, technology, architecture } = SITE_CONFIG; // brand name updated

  return (
    <div style={{ fontFamily: PRET, overflowX: 'hidden' }}>
      <Navbar entranceComplete={entranceComplete} />

      {/* ════════════════ SECTION 1: HERO ════════════════ */}
      <section className="relative min-h-[100dvh] md:h-screen md:h-[100dvh] overflow-hidden bg-white flex flex-col md:flex-row">
        {/* 모바일 최상단 카피 (텍스트가 흰 배경 위에만 얹히도록 보증) */}
        <div className="block md:hidden w-full bg-white pt-24 pb-8 px-6">
          <h1 className="text-[#141414] font-gmarket font-black leading-[1.1] tracking-[-0.03em]" style={{ fontSize: 'clamp(32px, 8vw, 48px)', wordBreak: 'keep-all' }}>
            <ScrambleIn text={hero.titleLeft[0]} delay={200} triggered={entranceComplete} />
            <br />
            <ScrambleIn text={hero.titleLeft[1]} delay={500} triggered={entranceComplete} />
          </h1>
          <motion.p
            className="max-w-md text-[16px] text-[#1a1a1a] leading-relaxed font-black mt-4"
            initial={{ opacity: 0, y: 15 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.2 }}
          >
            {hero.description}
          </motion.p>
          <motion.a
            href="#course"
            className="inline-flex items-center gap-2 border-2 border-[#141414] bg-[#141414] hover:bg-white hover:text-[#141414] text-white font-black text-[15px] tracking-wide px-6 py-3 rounded-full transition-colors mt-6"
            initial={{ opacity: 0, y: 15 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.35 }}
          >
            학습 시작 →
          </motion.a>
        </div>

        {/* 오른쪽/하단: 비디오 영역 (데스크톱에서는 w-[58%] / 모바일에서는 h-[45vh] w-full 스택) */}
        <div className="relative w-full h-[45vh] md:absolute md:right-0 md:top-0 md:h-full md:w-[58%]">
          {VIDEO_URLS.hero ? (
            <video src={VIDEO_URLS.hero}
              className="absolute inset-0 w-full h-full object-cover" playsInline muted autoPlay loop preload="auto" />
          ) : <HeroDoodle />}
          {VIDEO_URLS.hero && <HeroWords />}
          {/* 왼쪽으로 부드럽게 흰 페이드 (데스크톱 전용) */}
          <div className="hidden md:block absolute inset-y-0 left-0 w-1/3 bg-gradient-to-r from-white to-transparent pointer-events-none" />
        </div>

        {/* 데스크톱 왼쪽 카피 영역 */}
        <motion.div
          className="hidden md:flex relative z-20 h-full flex flex-col justify-center max-w-3xl w-[50%] px-6 sm:px-10 lg:px-16"
          initial={{ opacity: 0 }} animate={{ opacity: entranceComplete ? 1 : 0 }} transition={{ duration: 1 }}
        >
          <h1 className="text-[#141414] font-gmarket font-black leading-[1.1] tracking-[-0.03em]" style={{ fontSize: 'clamp(32px, 5vw, 72px)', wordBreak: 'keep-all' }}>
            <ScrambleIn text={hero.titleLeft[0]} delay={200} triggered={entranceComplete} />
            <br />
            <ScrambleIn text={hero.titleLeft[1]} delay={500} triggered={entranceComplete} />
          </h1>
          <motion.p
            className="max-w-md text-[16px] sm:text-[18px] text-[#1a1a1a] leading-relaxed font-black mt-6"
            initial={{ opacity: 0, y: 25 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.2 }}
          >
            {hero.description}
          </motion.p>
          <motion.a
            href="#course"
            className="inline-flex items-center gap-2 self-start border-2 border-[#141414] bg-[#141414] hover:bg-white hover:text-[#141414] text-white font-black text-[15px] sm:text-[17px] tracking-wide px-7 py-3.5 rounded-full transition-colors mt-8"
            initial={{ opacity: 0, y: 25 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.35 }}
          >
            학습 시작 →
          </motion.a>
        </motion.div>
      </section>

      {/* ════════════════ SECTION 2: 워드레인 + 스타워즈 크롤 ════════════════ */}
      <section ref={section2Ref} className="relative h-screen h-[100dvh] overflow-hidden bg-white flex items-center justify-center">
        {/* 영단어 떨어짐 */}
        <WordRain />
        
        {/* 위/아래 흰 그라디언트로 텍스트가 부드럽게 나타나고 사라지도록 */}
        <div className="absolute inset-x-0 top-0 h-32 bg-gradient-to-b from-white to-transparent z-10 pointer-events-none" />
        <div className="absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-white to-transparent z-10 pointer-events-none" />
        
        {/* 스타워즈 크롤 (Pretendard 서체) */}
        <div className="absolute inset-0 flex justify-center overflow-hidden z-[5] pointer-events-none" style={{ perspective: '340px' }}>
          <div
            className="sw-crawl text-center font-black text-[#141414] text-[26px] sm:text-[48px] md:text-[64px] leading-[1.8] w-full px-6"
            style={{ whiteSpace: 'pre', fontFamily: 'Pretendard, sans-serif' }}
          >
            {cinematic.text}
          </div>
        </div>
        <style>{`.sw-crawl{transform-origin:50% 100%;animation:sw-crawl 30s linear infinite}@keyframes sw-crawl{0%{transform:rotateX(22deg) translateY(95vh)}100%{transform:rotateX(22deg) translateY(-170%)}}`}</style>
      </section>

      {/* ════════════════ SECTION 3: INTERACTIVE DEMO & METRICS ════════════════ */}
      <section className="relative overflow-hidden bg-white py-24 sm:py-28">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-center text-[#141414] mb-4" style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(26px, 3.2vw, 40px)', letterSpacing: '-0.025em' }}>
            그려지는 순간, 단어가 장면으로 남습니다.
          </h2>
          <p className="text-center text-[#5d665f] mb-8 sm:mb-10" style={{ fontFamily: PRET, fontWeight: 600, fontSize: 'clamp(15px, 1.8vw, 18px)' }}>
            범선에서 별자리로, 다시 깊은 바다로 이어지는 세 장면을 보세요.
          </p>
          <div className="relative mx-auto w-full max-w-[960px] mb-20">
            <div className="relative overflow-hidden rounded-[18px] bg-[#f8faf8]" style={{ aspectRatio: '16 / 9' }}>
              <video
                key={LEARNING_PREVIEW_VIDEOS[previewIndex].src}
                src={LEARNING_PREVIEW_VIDEOS[previewIndex].src}
                className="absolute inset-0 h-full w-full object-contain"
                playsInline muted autoPlay preload="metadata"
                onLoadedMetadata={(event) => {
                  event.currentTarget.play().catch(() => undefined);
                  setPreviewProgress(0);
                }}
                onTimeUpdate={(event) => {
                  const { currentTime, duration } = event.currentTarget;
                  setPreviewProgress(duration ? currentTime / duration : 0);
                }}
                onEnded={() => {
                  setPreviewProgress(0);
                  setPreviewIndex((current) => (current + 1) % LEARNING_PREVIEW_VIDEOS.length);
                }}
              />

              {/* 그림이 완성되는 후, 단어가 장면 위에 하나씩 나타납니다. */}
              {LEARNING_PREVIEW_VIDEOS[previewIndex].words.map((word, index) => {
                const visible = previewProgress >= 0.46 + index * 0.09;
                return (
                  <button
                    key={word.en}
                    type="button"
                    onClick={() => speakPreviewWord(word.en)}
                    className={`absolute z-10 -translate-x-1/2 -translate-y-1/2 bg-transparent text-center transition-all duration-500 ${visible ? 'scale-100 opacity-100' : 'pointer-events-none scale-90 opacity-0'}`}
                    style={{ left: `${word.x}%`, top: `${word.y}%`, fontFamily: PRET }}
                    aria-label={`${word.en}, ${word.ko} 발음 듣기`}
                  >
                    <span
                      className="block text-[#074f3d]"
                      style={{
                        fontWeight: 900,
                        fontSize: 'clamp(20px, 3vw, 38px)',
                        lineHeight: 1,
                        letterSpacing: '-0.035em',
                        textShadow: '-2px -2px 0 #fff, 2px -2px 0 #fff, -2px 2px 0 #fff, 2px 2px 0 #fff, 0 3px 10px rgba(255,255,255,.95)',
                      }}
                    >
                      {word.en}
                    </span>
                    <span
                      className="mt-1 block text-[#315f53]"
                      style={{ fontWeight: 750, fontSize: 'clamp(11px, 1.4vw, 16px)', textShadow: '0 1px 5px #fff, 0 -1px 5px #fff' }}
                    >
                      {word.ko}
                    </span>
                  </button>
                );
              })}
            </div>
            <div className="mt-5 flex items-center justify-between gap-4 text-[#174f3c]">
              <strong style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(16px, 2vw, 20px)' }}>{LEARNING_PREVIEW_VIDEOS[previewIndex].title}</strong>
              <span style={{ fontFamily: PRET, fontWeight: 700, fontSize: 14 }}>{previewIndex + 1} / {LEARNING_PREVIEW_VIDEOS.length}</span>
            </div>
            <div className="mt-4 grid grid-cols-3 gap-3" aria-label="학습 영상 진행 순서">
              {LEARNING_PREVIEW_VIDEOS.map((item, index) => {
                const isCurrent = index === previewIndex;
                const isComplete = index < previewIndex;
                const width = isCurrent ? `${Math.max(2, previewProgress * 100)}%` : isComplete ? '100%' : '0%';
                return (
                  <button key={item.src} type="button" className="group cursor-pointer text-left" onClick={() => { setPreviewIndex(index); setPreviewProgress(0); }} aria-current={isCurrent ? 'step' : undefined} aria-label={`${item.title} 영상 보기`}>
                    <span className="block h-[3px] overflow-hidden rounded-full bg-[#dce6e1]">
                      <span className="block h-full rounded-full bg-[#27765b]" style={{ width }} />
                    </span>
                    <span className={`mt-3 flex items-start gap-2 transition-colors ${isCurrent ? 'text-[#174f3c]' : 'text-[#819087] group-hover:text-[#27765b]'}`} style={{ fontFamily: PRET, fontWeight: isCurrent ? 850 : 650, fontSize: 'clamp(13px, 1.5vw, 16px)', lineHeight: 1.35 }}>
                      <span aria-hidden="true">{isCurrent ? '▶' : `0${index + 1}`}</span>
                      <span>{item.title}</span>
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
          <h2 className="text-center text-[#141414] mb-16" style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(24px, 3.2vw, 36px)', letterSpacing: '-0.01em' }}>
            {metrics.subtitle}
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-14 md:gap-8 text-center items-start">
            {metrics.items.map((m, i) => (
              <motion.div
                key={m.label}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, delay: i * 0.15 }}
                viewport={{ once: true, amount: 0.3 }}
              >
                <div className="whitespace-nowrap text-[#1d3557]" style={{ fontFamily: PRET, fontWeight: 900, fontSize: 'clamp(44px, 6.5vw, 84px)', letterSpacing: '-0.03em', lineHeight: 1 }}>
                  {m.value}
                </div>
                <div className="mt-5 text-[#000000]" style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(16px, 1.8vw, 19.5px)', letterSpacing: '-0.01em', wordBreak: 'keep-all', whiteSpace: 'pre-line' }}>
                  {m.label}
                </div>
                <div className="mt-3.5 text-[#555555]" style={{ fontFamily: PRET, fontWeight: 700, fontSize: 15.5, lineHeight: 1.5, wordBreak: 'keep-all', whiteSpace: 'pre-line' }}>
                  {m.note}
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* ════════════════ SECTION 4: TECHNOLOGY ════════════════ */}
      <section className="relative overflow-hidden bg-white py-24 sm:py-32">
        {/* Background Dot Grid */}
        <div
          className="absolute inset-0 pointer-events-none"
          style={{
            backgroundImage: 'radial-gradient(rgba(0, 0, 0, 0.07) 1px, transparent 1px)',
            backgroundSize: '24px 24px',
          }}
        />

        <div className="relative z-20 px-8 sm:px-12 md:px-16">
          <div className="text-center my-20 sm:my-24">
            <h2 style={{ fontFamily: PRET, fontWeight: 900, fontSize: 'clamp(28px, 7vw, 80px)', letterSpacing: '-0.02em', lineHeight: 1.25, color: '#141414', wordBreak: 'keep-all' }}>단어를 보고 터치하고 듣는다.<br />어느새 외워진다.</h2>
            <p className="mt-5 text-[#222222]" style={{ fontFamily: PRET, fontSize: 'clamp(17px, 2.0vw, 24px)', fontWeight: 900, wordBreak: 'keep-all' }}>네 가지 원리는 전부 이 한 문장을 위해 있습니다</p>
          </div>

          <motion.div
            className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8 md:gap-6"
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ duration: 1.0, delay: 0.3 }}
            viewport={{ once: true, amount: 0.3 }}
          >
            {technology.features.map((f, i) => {
              return (
                <motion.div
                  key={f.title}
                  className="border-t-2 border-[#141414]/12 pt-6 transition-colors duration-300 cursor-default group hover:border-[color:var(--c)]"
                  style={{ ['--c' as string]: CARD_COLORS[i] } as React.CSSProperties}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  whileHover={{ y: -28 }}
                  transition={{ duration: 0.5, delay: i * 0.1, ease: 'easeOut' }}
                  viewport={{ once: true, amount: 0.3 }}
                >
                  <FeatureDoodle index={i} className="w-14 h-14 mb-3" color={CARD_COLORS[i]} />
                  <h3 className="mb-3" style={{ color: '#1a1a1a', fontFamily: PRET, fontWeight: 900, fontSize: 'clamp(24px, 4vw, 36px)', wordBreak: 'keep-all', letterSpacing: '-0.02em', lineHeight: 1.3 }}>
                    {f.title}
                  </h3>
                  <p className="leading-relaxed" style={{ color: CARD_COLORS[i], fontSize: 'clamp(16px, 1.8vw, 19px)', fontWeight: 600, wordBreak: 'keep-all' }}>
                    {f.desc}
                  </p>
                </motion.div>
              );
            })}
          </motion.div>
          
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.5 }}
            viewport={{ once: true, amount: 0.3 }}
          >
            <p className="text-center mt-24 mb-24" style={{fontSize: 'clamp(20px,2.4vw,28px)', letterSpacing: '-0.01em', lineHeight: 1.4}}>
              <span style={{color: '#1a1a1a', fontWeight: 600}}>사진 찍듯 외워지는 경험</span>
              <br className="block sm:hidden" />
              <span className="hidden sm:inline" style={{color: '#6b6b6b', fontWeight: 400}}> — </span>
              <span style={{color: '#6b6b6b', fontWeight: 400}}>그림으로 배우는 영어입니다.</span>
            </p>
          </motion.div>
        </div>
      </section>

      {/* ════════════════ SECTION 5: ARCHITECTURE ════════════════ */}
      <section className="min-h-screen flex items-center justify-center bg-white border-t border-neutral-100">
        <div className="max-w-3xl mx-auto px-6 py-32 text-center">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.0 }}
            viewport={{ once: true, amount: 0.4 }}
          >
            <p className="text-[#c2410c] text-[15px] tracking-[0.25em] uppercase mb-8 font-black">
              {architecture.subtitle}
            </p>
            <h2
              className="text-[#111111] font-gmarket font-black leading-[1.15] tracking-[-0.02em] mb-10"
              style={{ fontSize: 'clamp(32px, 8vw, 80px)' }}
            >
              {architecture.heading}
            </h2>
            <p className="text-[#1a1a1a] text-[17px] sm:text-[19px] leading-relaxed max-w-xl mx-auto font-extrabold">
              {architecture.description}
            </p>
          </motion.div>

          <motion.div
            className="mt-20 flex flex-col items-center gap-4"
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ duration: 1.2, delay: 0.4 }}
            viewport={{ once: true, amount: 0.4 }}
          >
            {architecture.layers.map((l) => (
              <div
                key={l.num}
                className="w-full max-w-md h-[72px] border-2 border-neutral-300 bg-neutral-50 rounded-lg flex items-center justify-between px-6 shadow-sm"
              >
                <span className="text-[#c2410c] text-[13px] sm:text-[14px] tracking-[0.15em] uppercase font-black">
                  Layer {l.num}
                </span>
                <span className="text-[#111111] text-[17px] sm:text-[19px] font-black">
                  {l.name}
                </span>
              </div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* ════════════════ SECTION 5.5: COMPARISON (GEO 비교 유닛) ════════════════ */}
      <section className="bg-neutral-50 py-24 px-6 border-t border-b border-neutral-100">
        <div className="max-w-4xl mx-auto">
          <p className="text-[#c2410c] text-[15px] tracking-[0.25em] uppercase mb-6 text-center font-black">Comparison</p>
          <h2 className="text-[#141414] font-gmarket font-black text-center mb-10" style={{ fontSize: 'clamp(32px, 8vw, 80px)', wordBreak: 'keep-all' }}>
            단어 앱은 많습니다 — 방식이 다릅니다
          </h2>
          {/* 모바일 화면용 카드 레이아웃 (768px 미만) */}
          <div className="block md:hidden mt-6 flex flex-col gap-4">
            {/* 말해보카 */}
            <div className="bg-white rounded-2xl p-5 border border-neutral-200/60 shadow-sm">
              <h3 className="font-bold text-[#666666] text-lg mb-3">말해보카</h3>
              <p className="text-[#777777] text-[15px] mb-2 flex"><span className="font-bold text-neutral-400 w-16 shrink-0">방식</span> <span className="word-break-keep">AI 레벨 퀴즈</span></p>
              <p className="text-[#777777] text-[15px] mb-2 flex"><span className="font-bold text-neutral-400 w-16 shrink-0">가격</span> <span>12개월 ₩119,000</span></p>
              <p className="text-[#777777] text-[15px] flex"><span className="font-bold text-neutral-400 w-16 shrink-0">추천 대상</span> <span className="word-break-keep">스스로 퀴즈 푸는 것이 편한 분</span></p>
            </div>
            {/* 클래스카드 */}
            <div className="bg-white rounded-2xl p-5 border border-neutral-200/60 shadow-sm">
              <h3 className="font-bold text-[#666666] text-lg mb-3">클래스카드</h3>
              <p className="text-[#777777] text-[15px] mb-2 flex"><span className="font-bold text-neutral-400 w-16 shrink-0">방식</span> <span className="word-break-keep">단어장 반복 암기</span></p>
              <p className="text-[#777777] text-[15px] mb-2 flex"><span className="font-bold text-neutral-400 w-16 shrink-0">가격</span> <span>무료+유료</span></p>
              <p className="text-[#777777] text-[15px] flex"><span className="font-bold text-neutral-400 w-16 shrink-0">추천 대상</span> <span className="word-break-keep">성실한 반복 암기가 체질인 분</span></p>
            </div>
            {/* 보는 단어장 */}
            <div className="bg-indigo-50/80 rounded-2xl p-5 border-2 border-indigo-500/80 shadow-md relative">
              <div className="flex items-center gap-2 mb-3">
                <h3 className="font-black text-indigo-900 text-[20px]">보는 단어장</h3>
                <span className="bg-rose-500 text-white text-[10px] font-black tracking-wide px-2 py-0.5 rounded-full shadow-sm animate-pulse">추천 ⭐</span>
              </div>
              <p className="text-indigo-950 font-black text-[16px] mb-3 flex"><span className="font-bold text-indigo-400 w-16 shrink-0">방식</span> <span className="word-break-keep">그림→글자 변신 애니메이션</span></p>
              <div className="text-indigo-950 font-black text-[16px] mb-3 flex items-center">
                <span className="font-bold text-indigo-400 w-16 shrink-0">가격</span>
                <span className="text-rose-600 font-extrabold text-[18px]">완성 코스 ₩9,900</span>
              </div>
              <p className="text-indigo-700 font-black text-[15px] flex"><span className="font-bold text-indigo-400 w-16 shrink-0">추천 대상</span> <span className="word-break-keep">지루한 암기가 힘들고 단어가 안 외워지는 분</span></p>
            </div>
          </div>

          {/* 데스크탑 화면용 테이블 레이아웃 (768px 이상) */}
          <div className="hidden md:block overflow-x-auto mt-6 px-1 py-4">
            <table className="w-full text-left text-[14px] sm:text-[17px] text-[#1a1a1a] border-separate border-spacing-y-3.5 min-w-[600px] sm:min-w-full">
              <thead>
                <tr className="text-[#111111] uppercase text-[14px] sm:text-[15px] tracking-wider font-black">
                  <th className="pb-2 pr-4 pl-5 whitespace-nowrap">서비스</th>
                  <th className="pb-2 pr-4 whitespace-nowrap">방식</th>
                  <th className="pb-2 pr-4 whitespace-nowrap">가격</th>
                  <th className="pb-2 pl-4 whitespace-nowrap">추천 대상</th>
                </tr>
              </thead>
              <tbody>
                {/* ── 말해보카 (경쟁사 1 - 톤다운) ── */}
                <tr className="bg-neutral-50/50 hover:bg-neutral-50 transition-colors duration-200">
                  <td className="py-5 pr-4 pl-5 font-bold text-[#666666] whitespace-nowrap first:rounded-l-2xl border-y border-l border-neutral-200/60">말해보카</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium whitespace-nowrap border-y border-neutral-200/60">AI 레벨 퀴즈</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium whitespace-nowrap border-y border-neutral-200/60">12개월 ₩119,000</td>
                  <td className="py-5 pl-4 pr-5 text-[#777777] font-medium last:rounded-r-2xl border-y border-r border-neutral-200/60" style={{ wordBreak: 'keep-all' }}>스스로 퀴즈 푸는 것이 편한 분</td>
                </tr>

                {/* ── 클래스카드 (경쟁사 2 - 톤다운) ── */}
                <tr className="bg-neutral-50/50 hover:bg-neutral-50 transition-colors duration-200">
                  <td className="py-5 pr-4 pl-5 font-bold text-[#666666] whitespace-nowrap first:rounded-l-2xl border-y border-l border-neutral-200/60">클래스카드</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium whitespace-nowrap border-y border-neutral-200/60">단어장 반복 암기</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium whitespace-nowrap border-y border-neutral-200/60">무료+유료</td>
                  <td className="py-5 pl-4 pr-5 text-[#777777] font-medium last:rounded-r-2xl border-y border-r border-neutral-200/60" style={{ wordBreak: 'keep-all' }}>성실한 반복 암기가 체질인 분</td>
                </tr>

                {/* ── 보는 단어장 (자사 - 초강력 하이라이트 & 3D 입체) ── */}
                <tr className="bg-indigo-50/80 hover:bg-indigo-50 transition-all duration-300 shadow-[0_8px_30px_rgb(0,0,0,0.03)] hover:shadow-[0_15px_40px_rgba(79,70,229,0.12)] transform hover:-translate-y-0.5">
                  <td className="py-6 pr-4 pl-5 font-black text-[16px] sm:text-[19px] text-indigo-900 whitespace-nowrap first:rounded-l-2xl border-y border-l-2 border-indigo-500/80">
                    <div className="flex items-center gap-2">
                      <span>보는 단어장</span>
                      <span className="bg-rose-500 text-white text-[10px] font-black tracking-wide px-2 py-0.5 rounded-full shadow-sm animate-pulse">추천 ⭐</span>
                    </div>
                  </td>
                  <td className="py-6 pr-4 font-black text-[15px] sm:text-[18px] text-indigo-950 whitespace-nowrap border-y border-indigo-500/80">그림→글자 변신 애니메이션</td>
                  <td className="py-6 pr-4 font-black text-[15px] sm:text-[18px] text-indigo-950 whitespace-nowrap border-y border-indigo-500/80">
                    <div className="flex flex-col">
                      <span className="text-rose-600 font-extrabold text-[16px] sm:text-[19px]">완성 코스 ₩9,900</span>
                    </div>
                  </td>
                  <td className="py-6 pl-4 pr-5 font-black text-[15px] sm:text-[18px] text-indigo-700 last:rounded-r-2xl border-y border-r-2 border-indigo-500/80" style={{ wordBreak: 'keep-all' }}>지루한 암기가 힘들고 단어가 안 외워지는 분</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p className="text-[#888888] text-[13px] sm:text-[14px] font-medium text-center mt-10">각 서비스 공식 페이지 기준 (2026-07 확인) · 정직한 비교를 지향합니다</p>
        </div>
      </section>

      {/* ════════════════ SECTION 6: PRICING ════════════════ */}
      <section className="min-h-screen bg-[#f2f4f6] py-32 px-6">
        <div className="max-w-6xl mx-auto">
          <motion.div
            className="text-center mb-20"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.0 }}
            viewport={{ once: true, amount: 0.3 }}
          >
            <p className="text-[#c2410c] text-[15px] tracking-[0.25em] uppercase mb-8 font-black">
              Pricing
            </p>
            <h2
              className="text-[#111111] font-gmarket font-black leading-[1.15] tracking-[-0.02em] mb-6"
              style={{ fontSize: 'clamp(28px, 6vw, 56px)' }}
            >
              플랜 선택
            </h2>
            <p className="text-[#1a1a1a] text-[17px] sm:text-[19px] leading-relaxed max-w-xl mx-auto font-extrabold">
              지루한 암기 대신, 보는 단어장으로 아이에게 새로운 기억을 선물하세요.
            </p>
          </motion.div>

          <div className="max-w-md mx-auto">
            {/* ── 12주 완성 코스 (코스 카드) ── */}
            <motion.div
              className="border-2 border-indigo-600 rounded-[28px] p-8 flex flex-col relative bg-neutral-900 shadow-xl hover:shadow-[0_20px_50px_rgba(0,0,0,0.3)] hover:-translate-y-1.5 transition-all duration-300"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0 }}
              viewport={{ once: true, amount: 0.3 }}
            >
              <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2">
                <span className="bg-[#c2410c] text-white text-[11px] font-black tracking-[0.12em] uppercase px-4 py-1.5 rounded-full shadow-sm">런칭 기념가</span>
              </div>
              <p className="text-white/60 text-[13px] tracking-[0.15em] uppercase mb-4 font-black">코스 (Course)</p>
              
              <div className="flex flex-col items-start mb-6">
                <div className="flex items-baseline gap-1.5">
                  <span className="text-[36px] sm:text-[42px] font-black tracking-tight text-white leading-none">₩9,900</span>
                  <span className="text-white/70 text-[13px] sm:text-[14px] font-bold">/ 평생 소장 · 매주 새 챕터 · 구독 아님</span>
                </div>
              </div>

              <h3 className="text-white font-gmarket font-black text-[22px] mb-4">
                그림 단어 완성 코스
              </h3>
              
              <ul className="flex flex-col gap-4 mb-10 flex-1">
                <li className="flex items-start text-white text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>전체 챕터 월드 맵과 테마별 장면 제공</span>
                </li>
                <li className="flex items-start text-white text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>눈·귀·손으로 동시 각인되는 그림-철자 변신</span>
                </li>
                <li className="flex items-start text-white text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>나의 단어 박물관 내 영구 소장 도감</span>
                </li>
              </ul>
              <div className="mt-auto">
                <TossCheckoutButton
                  product={TOSS_PRODUCTS[0]}
                  onError={(err) => console.error('Toss error:', err)}
                />
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* ════════════════ FOOTER ════════════════ */}
      <footer className="bg-neutral-50 border-t border-neutral-200/80 py-16 px-6 sm:px-10">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-start gap-10 md:gap-6">
          <div>
            <div className="flex items-center gap-2.5 mb-4">
              <ConnectAILabLogo size={20} className="text-[#141414]" />
              <span className="text-[17px] font-black text-[#141414] tracking-tight">
                {SITE_CONFIG.brandName}
              </span>
            </div>
            <p className="text-[#1a1a1a] text-[17px] sm:text-[19px] leading-relaxed max-w-md font-extrabold">
              외우게 하는 앱이 아니라, 보게 만드는 앱.<br />
              단어가 안 외워지는 분들의 첫 3분을 만듭니다.
            </p>
          </div>

          <div className="text-[#333333] text-[14px] sm:text-[15px] leading-6 font-bold">
            <p className="font-bold text-[#141414] mb-1">매또컴퍼니 | 대표: 이미현</p>
            <p className="mb-1">사업자등록번호: 308-15-96097 | 통신판매업신고: 면제 (부가가치세법상 간이과세자)</p>
            <p className="mb-3">주소: 경기도 양주시 고읍로 11-7</p>
            <p className="mt-3.5">
              <span>문의: thot168190@gmail.com</span>
              <span className="mx-2.5 text-neutral-300">|</span>
              <a href="/terms.html" target="_blank" className="text-indigo-600 underline font-extrabold hover:text-indigo-800">이용약관</a>
              <span className="mx-2 text-neutral-300">·</span>
              <a href="/privacy.html" target="_blank" className="text-indigo-600 underline font-extrabold hover:text-indigo-800">개인정보처리방침</a>
              {user && (
                <>
                  <span className="mx-2 text-neutral-300">·</span>
                  <button onClick={handleDeleteAccount} className="text-neutral-400 hover:text-red-500 transition-colors bg-transparent border-none cursor-pointer text-[12px] font-normal underline">회원 탈퇴</button>
                </>
              )}
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

/* ── 결제 성공 화면 ── */
function PaymentSuccessPage() {
  const params = new URLSearchParams(window.location.search);
  const orderId = params.get('orderId') || 'unknown';
  const amount = params.get('amount') ? parseInt(params.get('amount') || '0').toLocaleString() : '0';

  return (
    <div className="min-h-screen bg-[#010103] flex items-center justify-center px-6" style={{ fontFamily: PRET }}>
      <div className="max-w-md w-full border border-white/10 bg-white/[0.02] backdrop-blur-md rounded-2xl p-8 text-center">
        <div className="w-16 h-16 bg-emerald-500/10 text-emerald-400 rounded-full flex items-center justify-center mx-auto mb-6 text-[32px]">
          ✓
        </div>
        <h2 className="text-white font-gmarket font-bold text-[28px] mb-3 tracking-tight">단어장 잠금 해제 완료!</h2>
        <p className="text-white/60 text-[14px] mb-8 leading-relaxed">
          결제가 정상적으로 처리되었습니다. 이제 움직이는 그림 사전과 단어 패키지를 마음껏 이용해 보세요!
        </p>

        <div className="border-y border-white/5 py-4 mb-8 flex flex-col gap-3.5 text-left text-[14px]">
          <div className="flex justify-between">
            <span className="text-white/40">주문 번호</span>
            <span className="text-white/80 font-mono">{orderId}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-white/40">결제 금액</span>
            <span className="text-white font-gmarket font-bold">₩{amount}</span>
          </div>
        </div>

        <a
          href="/"
          className="w-full h-[50px] bg-white text-black font-semibold rounded-lg flex items-center justify-center hover:bg-white/90 transition-colors"
        >
          메인 화면으로 이동
        </a>
      </div>
    </div>
  );
}

/* ── 결제 실패 화면 ── */
function PaymentFailPage() {
  const params = new URLSearchParams(window.location.search);
  const message = params.get('message') || '결제 처리 중 예상치 못한 에러가 발생했습니다.';

  return (
    <div className="min-h-screen bg-[#010103] flex items-center justify-center px-6" style={{ fontFamily: PRET }}>
      <div className="max-w-md w-full border border-white/10 bg-white/[0.02] backdrop-blur-md rounded-2xl p-8 text-center">
        <div className="w-16 h-16 bg-red-500/10 text-red-400 rounded-full flex items-center justify-center mx-auto mb-6 text-[28px]">
          ✗
        </div>
        <h2 className="text-white font-gmarket font-bold text-[28px] mb-3 tracking-tight">결제 실패</h2>
        <p className="text-white/60 text-[14px] mb-8 leading-relaxed">
          {message}
        </p>

        <a
          href="/"
          className="w-full h-[50px] border border-white/20 text-white font-semibold rounded-lg flex items-center justify-center hover:bg-white/5 transition-colors"
        >
          돌아가기
        </a>
      </div>
    </div>
  );
}
