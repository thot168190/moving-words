import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ConnectAILabLogo } from './ConnectAILabLogo';
import { SquashHamburger } from './SquashHamburger';
import { ScrambleText } from './ScrambleText';
import { AuthModal } from './AuthModal';
import { useAuth } from '../contexts/AuthContext';
import { APP_ENTRY_URL } from '../config/app';

interface NavbarProps {
  entranceComplete: boolean;
}

export function Navbar({ entranceComplete }: NavbarProps) {
  const [menuOpen, setMenuOpen] = useState(false);
  const [aboutHovered, setAboutHovered] = useState(false);
  const [metricsHovered, setMetricsHovered] = useState(false);
  const [authOpen, setAuthOpen] = useState(false);
  const [progressOpen, setProgressOpen] = useState(false);
  const { user, signOut, learningProgress } = useAuth();

  // 메뉴 문구와 실제 화면 위치를 직접 연결해 사용자가 길을 잃지 않게 합니다.
  const scrollToSection = (selector: string) => {
    document.querySelector(selector)?.scrollIntoView({ behavior: 'smooth' });
    setMenuOpen(false);
  };

  return (
    <>
      <motion.nav
        className="fixed top-0 left-0 right-0 z-50 h-20 flex items-center px-4 sm:px-6 md:px-8"
        initial={{ opacity: 0 }}
        animate={{ opacity: entranceComplete ? 1 : 0 }}
        transition={{ duration: 0.8 }}
      >
        {/* ===== DESKTOP ===== */}
        <div className="hidden sm:flex items-center justify-between w-full">
          {/* Left group */}
          <div className="flex items-center gap-2">
            {/* Logo pill */}
            <motion.div
              className={`h-12 px-5 bg-[#141414]/5 backdrop-blur-md rounded-[14px] flex items-center gap-2.5 cursor-pointer ${
                menuOpen ? 'hidden md:flex' : 'flex'
              }`}
              whileHover={{ scale: 1.02, backgroundColor: 'rgba(20,20,20,0.08)' }}
              whileTap={{ scale: 0.98 }}
            >
              <ConnectAILabLogo size={18} className="text-[#07533f]" />
              <span className="nav-logo-text text-[17px] text-[#07533f]">
                보는 단어장
              </span>
            </motion.div>

            {/* Expanding menu pill */}
            <motion.div
              className="h-12 rounded-[14px] bg-[#141414]/5 backdrop-blur-md flex items-center overflow-hidden"
              animate={{ width: menuOpen ? 380 : 48 }}
              transition={{ type: 'spring', stiffness: 350, damping: 28 }}
            >
              {/* Hamburger button */}
              <motion.button
                className="flex items-center justify-center shrink-0 cursor-pointer border-none"
                style={{
                  width: menuOpen ? 36 : 48,
                  height: menuOpen ? 36 : 48,
                  borderRadius: menuOpen ? 11 : 14,
                  backgroundColor: menuOpen ? 'rgba(20,20,20,0.05)' : 'transparent',
                  marginLeft: menuOpen ? 6 : 0,
                }}
                onClick={() => setMenuOpen(!menuOpen)}
                whileHover={{ backgroundColor: menuOpen ? 'rgba(20,20,20,0.08)' : 'rgba(20,20,20,0.05)' }}
              >
                <SquashHamburger isOpen={menuOpen} />
              </motion.button>

              {/* Nav links */}
              <AnimatePresence>
                {menuOpen && (
                  <motion.div
                    className="flex items-center gap-5 ml-4 whitespace-nowrap"
                    initial={{ opacity: 0, x: 15 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: 15 }}
                    transition={{ duration: 0.25 }}
                  >
                    <button
                      className="text-[15px] font-bold text-[#07533f]/85 hover:text-[#07533f] transition-colors cursor-pointer bg-transparent border-none"
                      onMouseEnter={() => setAboutHovered(true)}
                      onMouseLeave={() => setAboutHovered(false)}
                      onClick={() => scrollToSection('#intro')}
                    >
                      <ScrambleText text="서비스 소개" isHovered={aboutHovered} />
                    </button>
                    <button
                      className="text-[15px] font-bold text-[#07533f]/85 hover:text-[#07533f] transition-colors cursor-pointer bg-transparent border-none"
                      onMouseEnter={() => setMetricsHovered(true)}
                      onMouseLeave={() => setMetricsHovered(false)}
                      onClick={() => scrollToSection('#course')}
                    >
                      <ScrambleText text="학습 방법" isHovered={metricsHovered} />
                    </button>
                    <button
                      className="text-[15px] font-bold text-[#07533f]/85 hover:text-[#07533f] transition-colors cursor-pointer bg-transparent border-none"
                      onClick={() => scrollToSection('#pricing')}
                    >
                      이용 요금
                    </button>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          </div>

          {/* Right buttons */}
          <div className="flex items-center gap-2">
            {/* 로그인한 경우에만 학습 기록과 사용자 정보를 표시합니다. */}
            {user ? (
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => setProgressOpen(true)}
                  className="h-12 px-5 rounded-[14px] bg-[#07533f] text-white text-[14px] font-black border-none cursor-pointer hover:bg-[#0b684f] transition-colors"
                >
                  내 학습
                </button>
                <div className="h-12 px-5 bg-[#141414]/5 backdrop-blur-md rounded-[14px] flex items-center gap-3">
                  {user.photoURL ? (
                    <img
                      src={user.photoURL}
                      alt="Profile"
                      className="w-8 h-8 rounded-full border border-[#141414]/10"
                    />
                  ) : (
                    <div className="w-8 h-8 rounded-full bg-[#141414]/10 flex items-center justify-center text-[13px] font-medium text-[#141414]">
                      {(user.displayName?.[0] || user.email?.[0] || 'U').toUpperCase()}
                    </div>
                  )}
                  <span className="text-[14px] text-[#141414]/80 max-w-[120px] truncate">
                    {user.displayName || user.email?.split('@')[0] || 'User'}
                  </span>
                  <button
                    onClick={signOut}
                    className="text-[12px] text-[#141414]/50 hover:text-[#141414]/80 transition-colors cursor-pointer bg-transparent border-none ml-1 font-bold"
                  >
                    Sign Out
                  </button>
                </div>
              </div>
            ) : null}

            {/* 본문의 '학습 시작'과 겹치지 않도록 상단에는 로그인만 둡니다. */}
            {!user && (
              <motion.button
                type="button"
                className="h-11 px-5 bg-[#07533f] rounded-full cursor-pointer border-none text-white text-[15px] font-bold"
                whileHover={{ scale: 1.03, backgroundColor: '#0b684f' }}
                whileTap={{ scale: 0.97 }}
                onClick={() => setAuthOpen(true)}
              >
                로그인
              </motion.button>
            )}
          </div>
        </div>

        {/* ===== MOBILE ===== */}
        <div className="flex sm:hidden items-center justify-between w-full">
          {/* Left group */}
          <div className="flex items-center gap-1.5 flex-1 min-w-0">
            {/* Logo pill (collapses when menu open) */}
            <motion.div
              className="h-9 px-3 bg-[#141414]/5 backdrop-blur-md rounded-[10px] flex items-center gap-2 overflow-hidden shrink-0"
              animate={{ width: menuOpen ? 0 : 'auto', opacity: menuOpen ? 0 : 1, paddingLeft: menuOpen ? 0 : 12, paddingRight: menuOpen ? 0 : 12 }}
              transition={{ type: 'spring', stiffness: 350, damping: 28 }}
            >
              <ConnectAILabLogo size={14} className="text-[#07533f] shrink-0" />
              <span className="text-[13px] font-medium tracking-tight text-[#07533f] whitespace-nowrap">
                보는 단어장
              </span>
            </motion.div>

            {/* Expanding menu capsule */}
            <motion.div
              className="h-9 rounded-[10px] bg-[#141414]/5 backdrop-blur-md flex items-center overflow-hidden"
              animate={{ width: menuOpen ? '100%' : 36 }}
              transition={{ type: 'spring', stiffness: 350, damping: 28 }}
            >
              <motion.button
                className="flex items-center justify-center shrink-0 cursor-pointer border-none"
                style={{
                  width: menuOpen ? 30 : 36,
                  height: menuOpen ? 30 : 36,
                  borderRadius: menuOpen ? 8 : 10,
                  backgroundColor: menuOpen ? 'rgba(20,20,20,0.05)' : 'transparent',
                  marginLeft: menuOpen ? 4 : 0,
                }}
                onClick={() => setMenuOpen(!menuOpen)}
              >
                <SquashHamburger isOpen={menuOpen} isMobile />
              </motion.button>

              <AnimatePresence>
                {menuOpen && (
                  <motion.div
                    className="flex items-center gap-3 ml-3 whitespace-nowrap"
                    initial={{ opacity: 0, x: 10 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: 10 }}
                    transition={{ duration: 0.2 }}
                  >
                    <button
                      className="text-[12px] font-bold text-[#07533f]/85 cursor-pointer bg-transparent border-none"
                      onClick={() => scrollToSection('#intro')}
                    >
                      소개
                    </button>
                    <button
                      className="text-[12px] font-bold text-[#07533f]/85 cursor-pointer bg-transparent border-none"
                      onClick={() => scrollToSection('#course')}
                    >
                      학습 방법
                    </button>
                    <button
                      className="text-[12px] font-bold text-[#07533f]/85 cursor-pointer bg-transparent border-none"
                      onClick={() => scrollToSection('#pricing')}
                    >
                      이용 요금
                    </button>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          </div>

          {/* Right buttons */}
          <div className="flex items-center gap-1.5 ml-2">
            {/* 로그인한 경우 학습 기록으로 이동 */}
            {user ? (
              <motion.button
                className="h-9 w-9 rounded-full bg-[#141414]/5 backdrop-blur-md flex items-center justify-center cursor-pointer border-none overflow-hidden"
                whileTap={{ scale: 0.9 }}
                onClick={() => setProgressOpen(true)}
              >
                {user.photoURL ? (
                  <img src={user.photoURL} alt="" className="w-full h-full object-cover" />
                ) : (
                  <span className="text-[#141414] text-[12px] font-bold">
                    {(user.displayName?.[0] || user.email?.[0] || 'U').toUpperCase()}
                  </span>
                )}
              </motion.button>
            ) : null}

            {!user && (
              <motion.button
                type="button"
                className="h-9 px-3.5 bg-[#07533f] rounded-full cursor-pointer border-none text-white text-[12px] font-bold whitespace-nowrap"
                whileTap={{ scale: 0.95 }}
                onClick={() => setAuthOpen(true)}
              >
                로그인
              </motion.button>
            )}
          </div>
        </div>
      </motion.nav>

      {/* Auth Modal */}
      <AuthModal
        isOpen={authOpen}
        onClose={() => setAuthOpen(false)}
        onSuccess={() => { window.location.hash = 'learn'; }}
      />

      <AnimatePresence>
        {progressOpen && user && (
          <motion.div
            className="fixed inset-0 z-[80] bg-black/35 backdrop-blur-sm flex items-center justify-center p-5"
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            onClick={() => setProgressOpen(false)}
          >
            <motion.section
              className="w-full max-w-[520px] rounded-[26px] bg-white p-7 sm:p-9 shadow-2xl text-[#07533f]"
              initial={{ opacity: 0, y: 18, scale: 0.98 }} animate={{ opacity: 1, y: 0, scale: 1 }} exit={{ opacity: 0, y: 10 }}
              onClick={(event) => event.stopPropagation()}
              aria-label="나의 학습 기록"
            >
              <div className="flex items-start justify-between gap-5 mb-8">
                <div><p className="text-[12px] tracking-[0.18em] font-black text-[#4f927b] mb-2">MY LEARNING</p><h2 className="text-[30px] font-black tracking-tight">나의 학습 기록</h2></div>
                <button type="button" onClick={() => setProgressOpen(false)} className="text-2xl bg-transparent border-none cursor-pointer text-[#07533f]">×</button>
              </div>
              <div className="grid grid-cols-3 border-y border-[#dcebe5]">
                <div className="py-6 text-center"><strong className="block text-[28px]">{learningProgress.completedSceneIds.length}</strong><span className="text-[13px] text-[#555]">완료 장면</span></div>
                <div className="py-6 text-center border-x border-[#dcebe5]"><strong className="block text-[28px]">{learningProgress.learnedWordIds.length}</strong><span className="text-[13px] text-[#555]">배운 단어</span></div>
                <div className="py-6 text-center"><strong className="block text-[28px]">{learningProgress.collectedCardIds.length}</strong><span className="text-[13px] text-[#555]">수집 카드</span></div>
              </div>
              <p className="mt-6 text-[14px] text-[#4a4a46]">
                {learningProgress.lastSceneId ? `마지막 학습: ${learningProgress.lastSceneId}` : '아직 저장된 학습이 없어요. 첫 장면을 시작해보세요.'}
              </p>
              <div className="flex gap-3 mt-7">
                <a href={APP_ENTRY_URL} className="flex-1 rounded-xl bg-[#07533f] text-white text-center py-4 font-black no-underline">학습 계속</a>
                <button type="button" onClick={signOut} className="rounded-xl border border-[#b9d2c9] bg-white px-5 font-bold text-[#4a4a46] cursor-pointer">로그아웃</button>
              </div>
            </motion.section>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
