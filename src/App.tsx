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
import TossCheckoutButton from './components/payment/TossCheckoutButton';
import { useAuth } from './contexts/AuthContext';
import { TOSS_PRODUCTS } from './lib/toss';
import { VIDEO_URLS } from './config/videos';
import { SITE_CONFIG } from './config/content';
import { APP_ENTRY_URL } from './config/app';
import LearningPage from './components/LearningPage';

const PRET = "'Pretendard Variable', Pretendard, -apple-system, sans-serif";
// 네 가지 학습 원리를 빠르게 구분하도록 브랜드 녹색과 조화되는 보조색을 사용합니다.
// 모두 흰 배경에서 읽기 쉬운 명도 대비를 유지합니다.
const CARD_COLORS = ['#07533F', '#B46F00', '#315C9B', '#A34F32'];

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

function LandingPage() {
  const [entranceComplete, setEntranceComplete] = useState(false);
  const [previewIndex, setPreviewIndex] = useState(0);
  const [previewProgress, setPreviewProgress] = useState(0);
  const lastSpokenRef = useRef({ word: '', at: 0 });
  const { user, deleteAccount } = useAuth();

  // PC에서는 마우스를 올리면, 모바일에서는 터치하면 영어 발음을 들려줍니다.
  const speakPreviewWord = (word: string) => {
    if (!window.speechSynthesis) return;
    const now = Date.now();
    if (lastSpokenRef.current.word === word && now - lastSpokenRef.current.at < 900) return;
    lastSpokenRef.current = { word, at: now };
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(word);
    utterance.lang = 'en-US';
    utterance.rate = 0.92;
    utterance.pitch = 1.0;
    utterance.volume = 1.0;

    // 첫 화면 콜로세움과 같은 우선순위로 자연스러운 영어 음성을 선택합니다.
    // 브라우저 기본 음성을 그대로 쓰면 기기마다 지나치게 느리거나 울리는 목소리가 나올 수 있습니다.
    const voices = window.speechSynthesis.getVoices();
    const bestVoice = voices.find(v => v.lang.startsWith('en') && v.name.includes('Google US English')) ||
                      voices.find(v => v.lang.startsWith('en') && v.name.includes('Samantha')) ||
                      voices.find(v => v.lang.startsWith('en') && v.name.includes('Aria')) ||
                      voices.find(v => v.lang === 'en-US');
    if (bestVoice) utterance.voice = bestVoice;

    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) ||
                  (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    if (isIOS) {
      setTimeout(() => window.speechSynthesis.speak(utterance), 50);
    } else {
      window.speechSynthesis.speak(utterance);
    }
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
  const { hero, cinematic, metrics, technology } = SITE_CONFIG; // brand name updated

  return (
    <div style={{ fontFamily: PRET, overflowX: 'hidden' }}>
      <Navbar entranceComplete={entranceComplete} />

      {/* ════════════════ SECTION 1: HERO ════════════════ */}
      <section className="relative min-h-[100dvh] md:h-screen md:h-[100dvh] overflow-hidden bg-white flex flex-col md:flex-row">
        {/* 모바일 최상단 카피 (텍스트가 흰 배경 위에만 얹히도록 보증) */}
        <div className="block md:hidden w-full bg-white pt-24 pb-8 px-6">
          <h1 className="text-[#07533f] font-gmarket font-black leading-[1.08] tracking-[-0.035em]" style={{ fontSize: 'clamp(36px, 8vw, 48px)', wordBreak: 'keep-all' }}>
            <ScrambleIn text={hero.titleLeft[0]} delay={200} triggered={entranceComplete} />
            <br />
            <ScrambleIn text={hero.titleLeft[1]} delay={500} triggered={entranceComplete} />
          </h1>
          <motion.p
            className="max-w-[34rem] text-[16px] text-[#454542] leading-[1.75] font-bold mt-4 whitespace-pre-line break-keep"
            style={{ wordBreak: 'keep-all', overflowWrap: 'break-word' }}
            initial={{ opacity: 0, y: 15 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.2 }}
          >
            {hero.description}
          </motion.p>
          <motion.a
            href={APP_ENTRY_URL}
            className="inline-flex items-center gap-2 border-2 border-[#07533f] bg-[#07533f] hover:bg-white hover:text-[#07533f] text-white font-black text-[15px] tracking-wide px-6 py-3 rounded-full transition-colors mt-6"
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
          <h1 className="text-[#07533f] font-gmarket font-black leading-[1.08] tracking-[-0.035em]" style={{ fontSize: 'clamp(42px, 5vw, 72px)', wordBreak: 'keep-all' }}>
            <ScrambleIn text={hero.titleLeft[0]} delay={200} triggered={entranceComplete} />
            <br />
            <ScrambleIn text={hero.titleLeft[1]} delay={500} triggered={entranceComplete} />
          </h1>
          <motion.p
            className="max-w-[36rem] text-[16px] lg:text-[18px] text-[#454542] leading-[1.75] font-bold mt-6 whitespace-pre-line break-keep"
            style={{ wordBreak: 'keep-all', overflowWrap: 'break-word' }}
            initial={{ opacity: 0, y: 25 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.2 }}
          >
            {hero.description}
          </motion.p>
          <motion.a
            href={APP_ENTRY_URL}
            className="inline-flex items-center gap-2 self-start border-2 border-[#07533f] bg-[#07533f] hover:bg-white hover:text-[#07533f] text-white font-black text-[15px] sm:text-[17px] tracking-wide px-7 py-3.5 rounded-full transition-colors mt-8"
            initial={{ opacity: 0, y: 25 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.35 }}
          >
            학습 시작 →
          </motion.a>
        </motion.div>
      </section>

      {/* ════════════════ SECTION 2: 핵심 문장 스크롤 ════════════════ */}
      <section id="intro" ref={section2Ref} className="relative h-screen h-[100dvh] overflow-hidden bg-white flex items-center justify-center">
        {/* 위/아래 흰 그라디언트로 텍스트가 부드럽게 나타나고 사라지도록 */}
        <div className="absolute inset-x-0 top-0 h-32 bg-gradient-to-b from-white to-transparent z-10 pointer-events-none" />
        <div className="absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-white to-transparent z-10 pointer-events-none" />
        
        {/* 스타워즈 크롤 (Pretendard 서체) */}
        <div className="absolute inset-0 flex justify-center overflow-hidden z-[5] pointer-events-none" style={{ perspective: '340px' }}>
          <div
            className="sw-crawl text-center font-black text-[#07533f] text-[26px] sm:text-[48px] md:text-[64px] leading-[1.8] w-full px-6"
            style={{ whiteSpace: 'pre', fontFamily: 'Pretendard, sans-serif' }}
          >
            {cinematic.text}
          </div>
        </div>
        <style>{`.sw-crawl{transform-origin:50% 100%;animation:sw-crawl 30s linear infinite}@keyframes sw-crawl{0%{transform:rotateX(22deg) translateY(95vh)}100%{transform:rotateX(22deg) translateY(-170%)}}`}</style>
      </section>

      {/* ════════════════ SECTION 3: INTERACTIVE DEMO & METRICS ════════════════ */}
      <section id="learning-preview" className="relative overflow-hidden bg-white py-16 sm:py-20">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-center text-[#07533f] mb-4" style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(26px, 3.2vw, 40px)', letterSpacing: '-0.025em' }}>
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
                    onMouseEnter={() => speakPreviewWord(word.en)}
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
          <h2 className="text-center text-[#07533f] mb-16" style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(24px, 3.2vw, 36px)', letterSpacing: '-0.01em' }}>
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
                <div className="whitespace-nowrap text-[#07533f]" style={{ fontFamily: PRET, fontWeight: 900, fontSize: 'clamp(44px, 6.5vw, 84px)', letterSpacing: '-0.03em', lineHeight: 1 }}>
                  {m.value}
                </div>
                <div className="mt-5 text-[#07533f]" style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(16px, 1.8vw, 19.5px)', letterSpacing: '-0.01em', wordBreak: 'keep-all', whiteSpace: 'pre-line' }}>
                  {m.label}
                </div>
                <div className="mt-3.5 text-[#454542]" style={{ fontFamily: PRET, fontWeight: 700, fontSize: 15.5, lineHeight: 1.5, wordBreak: 'keep-all', whiteSpace: 'pre-line' }}>
                  {m.note}
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* ════════════════ SECTION 4: TECHNOLOGY ════════════════ */}
      <section className="relative overflow-hidden bg-white py-14 sm:py-16">
        {/* Background Dot Grid */}
        <div
          className="absolute inset-0 pointer-events-none"
          style={{
            backgroundImage: 'radial-gradient(rgba(7, 83, 63, 0.10) 1px, transparent 1px)',
            backgroundSize: '24px 24px',
          }}
        />

        <div className="relative z-20 px-8 sm:px-12 md:px-16">
          <div className="text-center mt-6 mb-14 sm:mt-8 sm:mb-16">
            <h2 style={{ fontFamily: PRET, fontWeight: 900, fontSize: 'clamp(28px, 7vw, 80px)', letterSpacing: '-0.02em', lineHeight: 1.3, color: '#07533f', wordBreak: 'keep-all' }}>그림이 그려지는 과정을 보고 있으면<br />어느새 외워진다.</h2>
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
                  className="border-t-2 border-[#07533f]/15 pt-6 transition-colors duration-300 cursor-default group hover:border-[color:var(--c)]"
                  style={{ ['--c' as string]: CARD_COLORS[i] } as React.CSSProperties}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  whileHover={{ y: -28 }}
                  transition={{ duration: 0.5, delay: i * 0.1, ease: 'easeOut' }}
                  viewport={{ once: true, amount: 0.3 }}
                >
                  <FeatureDoodle index={i} className="w-14 h-14 mb-3" color={CARD_COLORS[i]} />
                  <h3 className="mb-3" style={{ color: CARD_COLORS[i], fontFamily: PRET, fontWeight: 900, fontSize: 'clamp(24px, 4vw, 36px)', wordBreak: 'keep-all', letterSpacing: '-0.02em', lineHeight: 1.3 }}>
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
              <span style={{color: '#07533f', fontWeight: 700}}>사진 찍듯 외워지는 경험</span>
              <br className="block sm:hidden" />
              <span className="hidden sm:inline" style={{color: '#6b6b6b', fontWeight: 400}}> — </span>
              <span style={{color: '#6b6b6b', fontWeight: 400}}>그림으로 배우는 영어입니다.</span>
            </p>
          </motion.div>
        </div>
      </section>

      {/* 학습·게임·AI 생성·박물관까지 제품의 핵심 기능을 한눈에 소개합니다. */}
      <section id="course" className="bg-[#f7fbf9] border-t border-[#dcebe5] px-6 py-16 sm:py-24">
        <div className="max-w-6xl mx-auto">
          <p className="text-[#c94f3d] text-[13px] tracking-[0.2em] uppercase mb-4 font-black">More than a wordbook</p>
          <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-5 mb-10 sm:mb-14">
            <h2 className="text-[#07533f] font-gmarket font-black tracking-[-0.035em] leading-[1.18]" style={{ fontSize: 'clamp(34px, 5vw, 64px)' }}>
              보고 끝나는 단어장이<br />아닙니다.
            </h2>
            <p className="max-w-md text-[#45665d] text-[18px] sm:text-[21px] font-bold leading-relaxed">
              그림으로 배우고, 게임으로 확인하고,<br className="hidden sm:block" /> 원하는 단어는 AI로 직접 만드세요.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 gap-4 sm:gap-5">
            {[
              ['01', '움직이는 그림 학습', '그림이 완성되는 과정을 보며 단어의 위치와 장면을 함께 기억합니다.', 'LEARN', '/learning/챕터1_완성동영상/scene-ch1-01-poster.jpg'],
              ['02', '거꾸로 퀴즈', '사라진 영어 단어를 그림 속 제자리로 돌려놓으며 기억을 게임처럼 확인합니다.', 'PLAY', '/learning/챕터1_완성동영상/scene-ch1-02-poster.jpg'],
              ['03', '내 단어 AI 그림 생성', '제시된 단어만 배우지 않습니다. 원하는 영어 단어와 장면을 직접 그림 카드로 만듭니다.', 'CREATE', '/metric-whale.jpeg'],
              ['04', '나만의 단어 박물관', '배운 카드와 직접 만든 그림 단어를 한곳에 모아 언제든 다시 꺼내봅니다.', 'COLLECT', '/metric-lighthouse.jpeg'],
            ].map(([num, title, desc, label, image], index) => (
              <motion.article
                key={num}
                className="group overflow-hidden rounded-[24px] border border-[#cfe2db] bg-white shadow-[0_10px_30px_rgba(7,83,63,0.05)] transition-all hover:-translate-y-1 hover:border-[#2f9c75] hover:shadow-[0_18px_38px_rgba(7,83,63,0.11)]"
                initial={{ opacity: 0, y: 24 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.55, delay: index * 0.08 }}
                viewport={{ once: true, amount: 0.2 }}
              >
                <div className="relative aspect-[16/8.5] overflow-hidden bg-[#edf5f1]">
                  <img src={image} alt={`${title} 실제 화면`} className="h-full w-full object-cover transition-transform duration-700 group-hover:scale-[1.03]" />
                  <div className="absolute inset-0 bg-gradient-to-t from-[#062f26]/45 via-transparent to-transparent" />
                  {index === 0 && (
                    <div className="absolute inset-0">
                      <span className="absolute left-[13%] top-[28%] text-white text-[20px] sm:text-[28px] font-black [text-shadow:0_2px_8px_#07533f]">whale</span>
                      <span className="absolute right-[13%] bottom-[22%] text-white text-[18px] sm:text-[25px] font-black [text-shadow:0_2px_8px_#07533f]">ocean</span>
                    </div>
                  )}
                  {index === 1 && (
                    <div className="absolute inset-0">
                      <span className="absolute left-[16%] top-[35%] grid h-12 w-12 place-items-center rounded-full bg-white text-[#07533f] text-2xl font-black shadow-lg">?</span>
                      <div className="absolute inset-x-4 bottom-4 flex gap-2">
                        {['light', 'beam', 'coast'].map((word) => <span key={word} className="rounded-full bg-white px-3 py-1.5 text-[13px] sm:text-[15px] font-black text-[#07533f] shadow">{word}</span>)}
                      </div>
                    </div>
                  )}
                  {index === 2 && (
                    <div className="absolute inset-x-5 bottom-4 rounded-xl bg-white/95 p-3 shadow-lg backdrop-blur">
                      <span className="block text-[#07533f] text-[18px] sm:text-[22px] font-black">whale · 고래</span>
                      <span className="text-[#527067] text-[12px] sm:text-[14px] font-bold">내가 원하는 장면으로 AI 그림 생성 중…</span>
                    </div>
                  )}
                  {index === 3 && (
                    <div className="absolute inset-x-4 bottom-4 grid grid-cols-3 gap-2">
                      {['whale', 'light', 'ocean'].map((word) => <span key={word} className="rounded-lg border border-white/60 bg-white/95 px-2 py-3 text-center text-[13px] sm:text-[16px] font-black text-[#07533f] shadow">{word}</span>)}
                    </div>
                  )}
                </div>
                <div className="p-7 sm:p-8">
                  <div className="mb-7 flex items-center justify-between">
                    <span className="text-[#c94f3d] text-[15px] font-black tracking-[0.12em]">{num}</span>
                    <span className="rounded-full bg-[#edf7f2] px-4 py-2 text-[#24765a] text-[12px] font-black tracking-[0.14em]">{label}</span>
                  </div>
                  <h3 className="text-[#07533f] font-gmarket font-black text-[27px] sm:text-[34px] tracking-[-0.03em] mb-4">{title}</h3>
                  <p className="text-[#45665d] text-[16px] sm:text-[18px] font-semibold leading-[1.7] break-keep">{desc}</p>
                </div>
              </motion.article>
            ))}
          </div>

          <div className="mt-8 flex justify-center">
            <a href={APP_ENTRY_URL} className="inline-flex min-h-14 items-center justify-center rounded-full bg-[#07533f] px-8 text-white text-[17px] font-black shadow-[0_10px_24px_rgba(7,83,63,0.18)] transition-transform hover:-translate-y-0.5">
              학습 기능 둘러보기 →
            </a>
          </div>
        </div>
      </section>

      {/* ════════════════ SECTION 5.5: COMPARISON (GEO 비교 유닛) ════════════════ */}
      <section className="bg-[#f8fbf9] py-24 px-6 border-t border-b border-[#dcebe5]">
        <div className="max-w-4xl mx-auto">
          <p className="text-[#34866b] text-[15px] tracking-[0.25em] uppercase mb-6 text-center font-black">Comparison</p>
          <h2 className="text-[#07533f] font-gmarket font-black text-center mb-10" style={{ fontSize: 'clamp(32px, 8vw, 80px)', wordBreak: 'keep-all' }}>
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
              <p className="text-[#777777] text-[15px] mb-2 flex"><span className="font-bold text-neutral-400 w-16 shrink-0">가격</span> <span>출시 기념가 ₩9,900</span></p>
              <p className="text-[#777777] text-[15px] flex"><span className="font-bold text-neutral-400 w-16 shrink-0">추천 대상</span> <span className="word-break-keep">성실한 반복 암기가 체질인 분</span></p>
            </div>
            {/* 보는 단어장 */}
            <div className="bg-[#eef7f3] rounded-2xl p-5 border-2 border-[#2f9c75] shadow-md relative">
              <div className="flex items-center gap-2 mb-3">
                <h3 className="font-black text-[#07533f] text-[20px]">보는 단어장</h3>
                <span className="bg-rose-500 text-white text-[10px] font-black tracking-wide px-2 py-0.5 rounded-full shadow-sm animate-pulse">추천 ⭐</span>
              </div>
              <p className="text-indigo-950 font-black text-[16px] mb-3 flex"><span className="font-bold text-indigo-400 w-16 shrink-0">방식</span> <span className="word-break-keep">그림→글자 변신 애니메이션</span></p>
              <div className="text-indigo-950 font-black text-[16px] mb-3 flex items-center">
                <span className="font-bold text-indigo-400 w-16 shrink-0">가격</span>
                <span className="flex flex-col">
                  <span className="text-[#6f756f] text-[13px] line-through">6개월 후 정상가 ₩19,800</span>
                  <span className="text-[#087052] font-extrabold text-[18px]">출시 기념가 ₩9,900</span>
                </span>
              </div>
              <p className="text-indigo-700 font-black text-[15px] flex"><span className="font-bold text-indigo-400 w-16 shrink-0">추천 대상</span> <span className="word-break-keep">지루한 암기가 힘들고 단어가 안 외워지는 분</span></p>
            </div>
          </div>

          {/* 데스크탑 화면용 테이블 레이아웃 (768px 이상) */}
          <div className="hidden md:block overflow-x-auto mt-6 px-1 py-4">
            <table className="w-full text-left text-[20px] text-[#1a1a1a] border-separate border-spacing-y-4 min-w-[900px]">
              <thead>
                <tr className="text-[#111111] uppercase text-[18px] tracking-wider font-black">
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
                <tr className="bg-[#f1f8f5] hover:bg-[#e8f4ef] transition-all duration-300 shadow-[0_8px_30px_rgb(0,0,0,0.03)] hover:shadow-[0_15px_40px_rgba(7,83,63,0.12)] transform hover:-translate-y-0.5">
                  <td className="py-8 pr-5 pl-7 font-black text-[22px] text-[#07533f] whitespace-nowrap first:rounded-l-2xl border-y border-l-2 border-[#4f927b]">
                    <div className="flex items-center gap-2">
                      <span>보는 단어장</span>
                      <span className="bg-[#4f927b] text-white text-[10px] font-black tracking-wide px-2 py-0.5 rounded-full shadow-sm">추천</span>
                    </div>
                  </td>
                  <td className="py-8 pr-5 font-black text-[21px] text-[#163f34] whitespace-nowrap border-y border-[#4f927b]">그림 학습·퀴즈·AI 이미지 생성</td>
                  <td className="py-8 pr-5 font-black text-[21px] text-[#163f34] whitespace-nowrap border-y border-[#4f927b]">
                    <div className="flex flex-col">
                      <span className="text-[#6f756f] text-[12px] sm:text-[13px] line-through">6개월 후 정상가 ₩19,800</span>
                      <span className="text-[#087052] font-extrabold text-[22px]">출시 기념가 ₩9,900</span>
                    </div>
                  </td>
                  <td className="py-8 pl-6 pr-7 font-black text-[21px] text-[#07533f] last:rounded-r-2xl border-y border-r-2 border-[#4f927b]" style={{ wordBreak: 'keep-all' }}>지루한 암기가 힘들고 단어가 안 외워지는 분</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p className="text-[#888888] text-[13px] sm:text-[14px] font-medium text-center mt-10">각 서비스 공식 페이지 기준 (2026-07 확인) · 정직한 비교를 지향합니다</p>
        </div>
      </section>

      {/* ════════════════ SECTION 6: PRICING ════════════════ */}
      <section id="pricing" className="bg-white py-14 sm:py-16 px-6 text-[#07533f] border-t border-[#dcebe5]">
        <div className="max-w-6xl mx-auto">
          <motion.div
            className="text-center mb-8"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 1.0 }}
            viewport={{ once: true, amount: 0.3 }}
          >
            <p className="text-[#34866b] text-[12px] tracking-[0.2em] uppercase mb-3 font-black">
              Pricing
            </p>
            <h2
              className="text-[#07533f] font-gmarket font-black leading-[1.15] tracking-[-0.02em] mb-5"
              style={{ fontSize: 'clamp(26px, 4vw, 40px)' }}
            >
              출시 기념가로 시작하세요.
            </h2>
            <p className="text-[#4a4a46] text-[16px] sm:text-[18px] leading-relaxed max-w-xl mx-auto font-semibold">
              한 번의 결제로 보는 단어장의 모든 학습 기능을 이용하세요.
            </p>
          </motion.div>

          <div className="max-w-xl mx-auto">
            {/* 출시 기념 이용권: 현재 공개된 콘텐츠와 이후 완성되는 챕터를 이용합니다. */}
            <motion.div
              className="border-2 border-[#2f9c75] rounded-[24px] p-7 sm:p-9 flex flex-col relative bg-[#fbfefc] shadow-[0_12px_28px_rgba(7,83,63,0.08)]"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.08 }}
              viewport={{ once: true, amount: 0.3 }}
            >
              <span className="absolute right-7 top-0 -translate-y-1/2 bg-[#d7f580] text-[#07533f] text-[13px] font-black tracking-[0.08em] px-5 py-2.5 rounded-full">출시 기념가</span>
              <h3 className="font-gmarket font-black text-[34px] sm:text-[40px] mb-3">
                출시 기념 이용권
              </h3>
              <p className="text-[#4a4a46] text-[18px] sm:text-[20px] font-semibold mb-7">12개 챕터의 학습 콘텐츠를 이용합니다.</p>
              <div className="mb-5">
                <div className="text-[#6f756f] text-[17px] sm:text-[19px] font-semibold line-through mb-2">6개월 후 정상가 ₩19,800</div>
                <div className="text-[46px] sm:text-[56px] font-black tracking-tight">₩9,900</div>
              </div>
              <ul className="divide-y divide-[#e2eee9] mb-7 flex-1">
                {['총 12개 챕터 학습', '학습 어휘를 모으는 나만의 카드 박물관', '학습 내용을 확인하는 퀴즈', '수학·과학 전문 어휘와 중국어 어휘 학습 순차 공개'].map((item) => (
                  <li key={item} className="py-5 flex items-center gap-4 text-[#353532] text-[18px] sm:text-[20px] font-bold leading-relaxed">
                    <span className="text-[#2f9c75] text-2xl">✓</span>{item}
                  </li>
                ))}
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
      <footer className="bg-[#f8fbf9] border-t border-[#dcebe5] py-16 px-6 sm:px-10">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-start gap-10 md:gap-6">
          <div>
            <div className="flex items-center gap-2.5 mb-4">
              <ConnectAILabLogo size={20} className="text-[#07533f]" />
              <span className="text-[17px] font-black text-[#07533f] tracking-tight">
                {SITE_CONFIG.brandName}
              </span>
            </div>
            <p className="text-[#454542] text-[17px] sm:text-[19px] leading-relaxed max-w-md font-extrabold">
              외우게 하는 앱이 아니라, 보게 만드는 앱.<br />
              단어가 안 외워지는 분들의 첫 3분을 만듭니다.
            </p>
          </div>

          <div className="text-[#333333] text-[14px] sm:text-[15px] leading-6 font-bold">
            <p className="font-bold text-[#07533f] mb-1">매또컴퍼니 | 대표: 이미현</p>
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

export default function App() {
  const [hash, setHash] = useState(window.location.hash);

  useEffect(() => {
    const syncHash = () => setHash(window.location.hash);
    window.addEventListener('hashchange', syncHash);
    return () => window.removeEventListener('hashchange', syncHash);
  }, []);

  // 랜딩은 그대로 두고, 로그인 뒤 실제 학습장만 해시 주소로 분리합니다.
  // GitHub Pages에서도 새 라우터 설정 없이 /#learn 주소가 안전하게 동작합니다.
  return hash === '#learn' ? <LearningPage /> : <LandingPage />;
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
