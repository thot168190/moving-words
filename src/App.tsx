import { useState, useEffect, useRef } from 'react';
import {
  motion,
} from 'framer-motion';
import { Navbar } from './components/Navbar';
import { ScrambleIn } from './components/ScrambleText';
import { ConnectAILabLogo } from './components/ConnectAILabLogo';
import HeroDoodle from './components/HeroDoodle';
import HeroWords from './components/HeroWords';
import MetricsDoodle from './components/MetricsDoodle';
import FeatureDoodle from './components/FeatureDoodle';
import WordRain from './components/WordRain';
import TossCheckoutButton from './components/payment/TossCheckoutButton';
import { useAuth } from './contexts/AuthContext';
import { TOSS_PRODUCTS } from './lib/toss';
import { VIDEO_URLS } from './config/videos';
import { SITE_CONFIG } from './config/content';

const PRET = "'Pretendard Variable', Pretendard, -apple-system, sans-serif";
const CARD_COLORS = ['#3b6ba5', '#c2410c', '#2f8f83', '#b98a2f'];

export default function App() {
  const [entranceComplete, setEntranceComplete] = useState(false);
  const { user, deleteAccount } = useAuth();

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

  /* ── Section 2 scroll-driven 3D text ── */
  const section2Ref = useRef<HTMLDivElement>(null);


  /* ── Destructure config for readability ── */
  const { hero, cinematic, metrics, technology, architecture } = SITE_CONFIG; // brand name updated

  return (
    <div style={{ fontFamily: PRET, overflowX: 'hidden' }}>
      <Navbar entranceComplete={entranceComplete} />

      {/* ════════════════ SECTION 1: HERO ════════════════ */}
      <section className="relative h-screen h-[100dvh] overflow-hidden bg-white flex flex-col md:flex-row">
        {/* 오른쪽: 콜로세움 그림 */}
        <div className="hidden md:block absolute right-0 top-0 h-full w-full md:w-[58%]">
          {VIDEO_URLS.hero ? (
            <video src={VIDEO_URLS.hero}
              className="absolute inset-0 w-full h-full object-cover" playsInline muted autoPlay loop preload="auto" />
          ) : <HeroDoodle />}
          {VIDEO_URLS.hero && <HeroWords />}
          {/* 왼쪽으로 부드럽게 흰 페이드 */}
          <div className="absolute inset-y-0 left-0 w-1/3 bg-gradient-to-r from-white to-transparent pointer-events-none" />
        </div>

        {/* 왼쪽: 카피 */}
        <motion.div
          className="relative z-20 h-full flex flex-col justify-center max-w-3xl w-full md:w-[50%] px-6 sm:px-10 lg:px-16"
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
            href="/demo.html"
            className="inline-flex items-center gap-2 self-start border-2 border-[#141414] bg-[#141414] hover:bg-white hover:text-[#141414] text-white font-black text-[15px] sm:text-[17px] tracking-wide px-7 py-3.5 rounded-full transition-colors mt-8"
            initial={{ opacity: 0, y: 25 }} animate={entranceComplete ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.9, delay: 0.35 }}
          >
            ✏️ 30초면 압니다 · 무료 체험 →
          </motion.a>
        </motion.div>
        <div className="block md:hidden relative w-full h-[45vh]">
          <video src={VIDEO_URLS.hero} className="absolute inset-0 w-full h-full object-cover" playsInline muted autoPlay loop preload="auto" />
        {VIDEO_URLS.hero && <HeroWords />}
        </div>
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

      {/* ════════════════ SECTION 3: METRICS ════════════════ */}
      <section className="relative overflow-hidden bg-white py-24 sm:py-28">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-center text-[#141414]" style={{ fontFamily: PRET, fontWeight: 800, fontSize: 'clamp(24px, 3.2vw, 36px)', letterSpacing: '-0.01em' }}>
            {metrics.subtitle}
          </h2>
          <div className="hidden md:block relative mx-auto mt-10" style={{ height: '46vh', maxHeight: 520, width: 'min(860px, 92%)' }}>
            <MetricsDoodle />
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-14 md:gap-8 text-center mt-14 items-start">
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
            <h2 style={{ fontFamily: PRET, fontWeight: 900, fontSize: 'clamp(32px, 8vw, 80px)', letterSpacing: '-0.02em', lineHeight: 1.25, color: '#141414', wordBreak: 'keep-all' }}>단어를 보고 터치하고 듣는다.<br />어느새 외워진다.</h2>
            <p className="mt-5 text-[#222222]" style={{ fontFamily: PRET, fontSize: 'clamp(19px, 2.0vw, 24px)', fontWeight: 900 }}>네 가지 원리는 전부 이 한 문장을 위해 있습니다</p>
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
                  <h3 className="mb-2" style={{ color: CARD_COLORS[i], fontFamily: PRET, fontWeight: 900, fontSize: 20, wordBreak: 'keep-all' }}>
                    {f.title}
                  </h3>
                  <p className="text-[#000000] leading-relaxed" style={{ fontSize: 'clamp(21px, 2.2vw, 26px)', fontWeight: 900, wordBreak: 'keep-all' }}>
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
            className="global-box"
          >
            <p className="text-center mt-20" style={{fontSize: 'clamp(20px,2.4vw,28px)', lineHeight: 1.4, fontWeight: 800}}>
              <span style={{color: '#111111'}}>사진 찍듯 외워지는 경험 </span>
              <span style={{color: '#333333'}}>— 그림으로 배우는 영어입니다.</span>
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
              style={{ fontSize: 'clamp(28px, 6vw, 56px)' }}
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
          <h2 className="text-[#141414] font-gmarket font-black text-center mb-10" style={{ fontSize: 'clamp(24px,4.5vw,40px)' }}>
            단어 앱은 많습니다 — 방식이 다릅니다
          </h2>
          <div className="overflow-x-auto mt-6 px-1 py-4">
            <table className="w-full text-left text-[14px] sm:text-[17px] text-[#1a1a1a] border-separate border-spacing-y-3.5 min-w-[700px]">
              <thead>
                <tr className="text-[#111111] uppercase text-[14px] sm:text-[15px] tracking-wider font-black">
                  <th className="pb-2 pr-4 pl-5">서비스</th>
                  <th className="pb-2 pr-4">방식</th>
                  <th className="pb-2 pr-4">가격</th>
                  <th className="pb-2 pl-4">추천 대상</th>
                </tr>
              </thead>
              <tbody>
                {/* ── 말해보카 (경쟁사 1 - 톤다운) ── */}
                <tr className="bg-neutral-50/50 hover:bg-neutral-50 transition-colors duration-200">
                  <td className="py-5 pr-4 pl-5 font-bold text-[#666666] first:rounded-l-2xl border-y border-l border-neutral-200/60">말해보카</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium border-y border-neutral-200/60">AI 레벨 퀴즈</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium border-y border-neutral-200/60">12개월 ₩119,000</td>
                  <td className="py-5 pl-4 pr-5 text-[#777777] font-medium last:rounded-r-2xl border-y border-r border-neutral-200/60">스스로 퀴즈 푸는 것이 편한 분</td>
                </tr>

                {/* ── 클래스카드 (경쟁사 2 - 톤다운) ── */}
                <tr className="bg-neutral-50/50 hover:bg-neutral-50 transition-colors duration-200">
                  <td className="py-5 pr-4 pl-5 font-bold text-[#666666] first:rounded-l-2xl border-y border-l border-neutral-200/60">클래스카드</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium border-y border-neutral-200/60">단어장 반복 암기</td>
                  <td className="py-5 pr-4 text-[#777777] font-medium border-y border-neutral-200/60">무료+유료</td>
                  <td className="py-5 pl-4 pr-5 text-[#777777] font-medium last:rounded-r-2xl border-y border-r border-neutral-200/60">성실한 반복 암기가 체질인 분</td>
                </tr>

                {/* ── 보는 단어장 (자사 - 초강력 하이라이트 & 3D 입체) ── */}
                <tr className="bg-indigo-50/80 hover:bg-indigo-50 transition-all duration-300 shadow-[0_8px_30px_rgb(0,0,0,0.03)] hover:shadow-[0_15px_40px_rgba(79,70,229,0.12)] transform hover:-translate-y-0.5">
                  <td className="py-6 pr-4 pl-5 font-black text-[16px] sm:text-[19px] text-indigo-900 first:rounded-l-2xl border-y border-l-2 border-indigo-500/80">
                    <div className="flex items-center gap-2">
                      <span>보는 단어장</span>
                      <span className="bg-rose-500 text-white text-[10px] font-black tracking-wide px-2 py-0.5 rounded-full shadow-sm animate-pulse">추천 ⭐</span>
                    </div>
                  </td>
                  <td className="py-6 pr-4 font-black text-[15px] sm:text-[18px] text-indigo-950 border-y border-indigo-500/80">그림→글자 변신 애니메이션</td>
                  <td className="py-6 pr-4 font-black text-[15px] sm:text-[18px] text-indigo-950 border-y border-indigo-500/80">
                    <div className="flex flex-col">
                      <span className="text-[12px] text-neutral-400 line-through font-bold">₩9,900</span>
                      <span className="text-rose-600 font-extrabold text-[16px] sm:text-[19px]">₩4,900 원샷</span>
                    </div>
                  </td>
                  <td className="py-6 pl-4 pr-5 font-black text-[15px] sm:text-[18px] text-indigo-700 last:rounded-r-2xl border-y border-r-2 border-indigo-500/80">지루한 암기가 힘들고 단어가 안 외워지는 분</td>
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
              어떻게 외워지는지 직접 확인해 보세요. 데모는 무료, 회원가입도 없습니다.
            </p>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-10">
            {/* ── Basic (Starter) ── */}
            <motion.div
              className="border border-neutral-200/90 rounded-[28px] p-8 flex flex-col relative bg-white shadow-[0_8px_30px_rgb(0,0,0,0.02)] hover:shadow-[0_20px_50px_rgba(0,0,0,0.07)] hover:-translate-y-1 transition-all duration-300"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0 }}
              viewport={{ once: true, amount: 0.3 }}
            >
              <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2">
                <span className="bg-[#c2410c] text-white text-[11px] font-black tracking-[0.12em] uppercase px-4 py-1.5 rounded-full shadow-sm">런칭 기념가</span>
              </div>
              <p className="text-[#555555] text-[13px] tracking-[0.15em] uppercase mb-4 font-black">스타터 (Starter)</p>
              
              <div className="flex flex-col items-start mb-6">
                <span className="text-[#888888] text-[16px] line-through font-bold mb-1">₩9,900</span>
                <div className="flex items-baseline gap-1.5">
                  <span className="text-[36px] sm:text-[42px] font-black tracking-tight text-[#111111] leading-none">₩4,900</span>
                  <span className="text-[#444444] text-[13px] sm:text-[14px] font-bold">/ 평생 소장</span>
                </div>
              </div>

              <p className="text-[#333333] text-[14.5px] leading-relaxed mb-8 font-bold">
                중등 필수 800단어 전권. 구독 아님 — 한 번 결제로 평생.
              </p>
              
              <ul className="flex flex-col gap-4 mb-10 flex-1">
                <li className="flex items-start text-[#111111] text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-orange-100 text-[#c2410c] flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>움직이는 단어 800개 전권</span>
                </li>
                <li className="flex items-start text-[#111111] text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-orange-100 text-[#c2410c] flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>터치 변신 + 원어민 발음 무제한</span>
                </li>
                <li className="flex items-start text-[#111111] text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-orange-100 text-[#c2410c] flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>모든 기기 지원 · 광고 없음</span>
                </li>
              </ul>
              <div className="mt-auto">
                <TossCheckoutButton
                  product={TOSS_PRODUCTS[0]}
                  onError={(err) => console.error('Toss error:', err)}
                />
              </div>
            </motion.div>

            {/* ── Pro (Premium) ── */}
            <motion.div
              className="border-2 border-indigo-600 rounded-[28px] p-8 flex flex-col relative bg-neutral-900 shadow-xl hover:shadow-[0_20px_50px_rgba(0,0,0,0.3)] hover:-translate-y-1.5 transition-all duration-300"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.1 }}
              viewport={{ once: true, amount: 0.3 }}
            >
              <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2">
                <span className="bg-indigo-600 text-white text-[11px] font-black tracking-[0.12em] uppercase px-4 py-1.5 rounded-full shadow-md">
                  가장 인기있는 플랜
                </span>
              </div>
              <p className="text-white/60 text-[13px] tracking-[0.15em] uppercase mb-4 font-black">프리미엄 (Premium)</p>
              
              <div className="flex flex-col items-start mb-6">
                <span className="text-white/30 text-[16px] font-bold mb-1 select-none opacity-0">-</span>
                <div className="flex items-baseline gap-1.5">
                  <span className="text-[36px] sm:text-[42px] font-black tracking-tight text-white leading-none">₩49,000</span>
                  <span className="text-white/70 text-[13px] sm:text-[14px] font-bold">/ 12개월</span>
                </div>
              </div>

              <p className="text-white/80 text-[14.5px] leading-relaxed mb-8 font-bold">
                매달 새 시리즈가 추가되는 플랜. 수학·과학 확장 시리즈 포함.
              </p>
              
              <ul className="flex flex-col gap-4 mb-10 flex-1">
                <li className="flex items-start text-white text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>스타터 플랜 혜택 전체 포함</span>
                </li>
                <li className="flex items-start text-white text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>매달 새 단어 시리즈 자동 추가</span>
                </li>
                <li className="flex items-start text-white text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>수학·과학 개념 시리즈 포함</span>
                </li>
                <li className="flex items-start text-white text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>컬러 시네마틱판 우선 이용 (준비중)</span>
                </li>
              </ul>
              <div className="mt-auto">
                <TossCheckoutButton
                  product={TOSS_PRODUCTS[1]}
                  onError={(err) => console.error('Toss error:', err)}
                />
              </div>
            </motion.div>

            {/* ── Enterprise (Lifetime) ── */}
            <motion.div
              className="border border-neutral-200/90 rounded-[28px] p-8 flex flex-col bg-neutral-50/20 hover:shadow-[0_20px_50px_rgba(0,0,0,0.07)] hover:-translate-y-1 transition-all duration-300"
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              viewport={{ once: true, amount: 0.3 }}
            >
              <p className="text-[#555555] text-[13px] tracking-[0.15em] uppercase mb-4 font-black">평생 소장판 (Lifetime)</p>
              
              <div className="flex flex-col items-start mb-6">
                <span className="text-[#888888] text-[16px] font-bold mb-1 select-none opacity-0">-</span>
                <div className="flex items-baseline gap-1.5">
                  <span className="text-[36px] sm:text-[42px] font-black tracking-tight text-[#111111] leading-none">₩99,000</span>
                  <span className="text-[#444444] text-[13px] sm:text-[14px] font-bold">/ 평생 소장</span>
                </div>
              </div>

              <p className="text-[#333333] text-[14.5px] leading-relaxed mb-8 font-bold">
                앞으로 나올 모든 시리즈와 언어팩까지, 단 한 번 결제로 평생.
              </p>
              
              <ul className="flex flex-col gap-4 mb-10 flex-1">
                <li className="flex items-start text-[#111111] text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>프리미엄 혜택 전체 포함</span>
                </li>
                <li className="flex items-start text-[#111111] text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>향후 출시 시리즈 전부 포함</span>
                </li>
                <li className="flex items-start text-[#111111] text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>다국어 언어팩 (영어 외 추가 언어)</span>
                </li>
                <li className="flex items-start text-[#111111] text-[14px] font-bold">
                  <span className="flex-shrink-0 w-5 h-5 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mr-3 mt-0.5">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </span>
                  <span>얼리버드 신기능 우선 체험</span>
                </li>
              </ul>
              <div className="mt-auto">
                <TossCheckoutButton
                  product={TOSS_PRODUCTS[2]}
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
            <p className="mb-1">사업자등록번호: 308-15-96097 | 통신판매업신고: 신고 예정</p>
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

