import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ConnectAILabLogo } from './ConnectAILabLogo';
import { SquashHamburger } from './SquashHamburger';
import { ScrambleText } from './ScrambleText';
import { AuthModal } from './AuthModal';
import { useAuth } from '../contexts/AuthContext';

interface NavbarProps {
  entranceComplete: boolean;
}

export function Navbar({ entranceComplete }: NavbarProps) {
  const [menuOpen, setMenuOpen] = useState(false);
  const [downloadHovered, setDownloadHovered] = useState(false);
  const [aboutHovered, setAboutHovered] = useState(false);
  const [metricsHovered, setMetricsHovered] = useState(false);
  const [authOpen, setAuthOpen] = useState(false);
  const { user, signOut, deleteAccount } = useAuth();

  const handleDeleteAccount = async () => {
    const isConfirmed = window.confirm(
      '정말로 회원 탈퇴를 진행하시겠습니까?\n탈퇴 시 즉시 모든 학습 기록과 계정 정보가 영구 삭제되며, 이 작업은 복구할 수 없습니다.'
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

  const scrollTo = (y: number) => {
    window.scrollTo({ top: y, behavior: 'smooth' });
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
              <ConnectAILabLogo size={18} className="text-[#141414]" />
              <span className="nav-logo-text text-[17px] text-[#141414]">
                보는 단어장
              </span>
            </motion.div>

            {/* Expanding menu pill */}
            <motion.div
              className="h-12 rounded-[14px] bg-[#141414]/5 backdrop-blur-md flex items-center overflow-hidden"
              animate={{ width: menuOpen ? 290 : 48 }}
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
                    className="flex items-center gap-6 ml-4 whitespace-nowrap"
                    initial={{ opacity: 0, x: 15 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: 15 }}
                    transition={{ duration: 0.25 }}
                  >
                    <button
                      className="text-[16px] font-normal text-[#141414]/85 hover:text-[#141414] transition-colors cursor-pointer bg-transparent border-none"
                      onMouseEnter={() => setAboutHovered(true)}
                      onMouseLeave={() => setAboutHovered(false)}
                      onClick={() => scrollTo(window.innerHeight)}
                    >
                      <ScrambleText text="About" isHovered={aboutHovered} />
                    </button>
                    <button
                      className="text-[16px] font-normal text-[#141414]/85 hover:text-[#141414] transition-colors cursor-pointer bg-transparent border-none"
                      onMouseEnter={() => setMetricsHovered(true)}
                      onMouseLeave={() => setMetricsHovered(false)}
                      onClick={() => scrollTo(window.innerHeight * 2)}
                    >
                      <ScrambleText text="Metrics" isHovered={metricsHovered} />
                    </button>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          </div>

          {/* Right buttons */}
          <div className="flex items-center gap-2">
            {/* Sign In / User button */}
            {user ? (
              <div className="flex items-center gap-2">
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
            ) : (
              <motion.button
                className="h-12 px-5 bg-[#141414]/5 backdrop-blur-md rounded-[14px] flex items-center gap-2 cursor-pointer border-none text-[#141414]/85 text-[15px] font-medium hover:bg-[#141414]/10 transition-colors"
                whileTap={{ scale: 0.97 }}
                onClick={() => setAuthOpen(true)}
              >
                Sign In
              </motion.button>
            )}

            {/* Download button */}
            <motion.a
              href="#course"
              className="h-12 px-6 bg-[#141414] rounded-full flex items-center gap-2.5 cursor-pointer border-none no-underline"
              whileHover={{ scale: 1.03, backgroundColor: '#3a3a3a' }}
              whileTap={{ scale: 0.97 }}
              onMouseEnter={() => setDownloadHovered(true)}
              onMouseLeave={() => setDownloadHovered(false)}
            >
              <span className="text-white text-[16px]">✏️</span>
              <span className="text-white text-[16px] font-medium">
                <ScrambleText text="12주 코스 신청" isHovered={downloadHovered} />
              </span>
            </motion.a>
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
              <ConnectAILabLogo size={14} className="text-[#141414] shrink-0" />
              <span className="text-[13px] font-medium tracking-tight text-[#141414] whitespace-nowrap">
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
                    className="flex items-center gap-4 ml-3 whitespace-nowrap"
                    initial={{ opacity: 0, x: 10 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: 10 }}
                    transition={{ duration: 0.2 }}
                  >
                    <button
                      className="text-[13px] font-normal text-[#141414]/85 cursor-pointer bg-transparent border-none"
                      onClick={() => scrollTo(window.innerHeight)}
                    >
                      About
                    </button>
                    <button
                      className="text-[13px] font-normal text-[#141414]/85 cursor-pointer bg-transparent border-none"
                      onClick={() => scrollTo(window.innerHeight * 2)}
                    >
                      Metrics
                    </button>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          </div>

          {/* Right buttons */}
          <div className="flex items-center gap-1.5 ml-2">
            {/* Sign In / Avatar */}
            {user ? (
              <motion.button
                className="h-9 w-9 rounded-full bg-[#141414]/5 backdrop-blur-md flex items-center justify-center cursor-pointer border-none overflow-hidden"
                whileTap={{ scale: 0.9 }}
                onClick={() => {
                  const isSignOut = window.confirm('로그아웃 하시겠습니까?\n(회원 탈퇴를 진행하시려면 [취소]를 누르고 다음 안내창에서 진행해 주세요.)');
                  if (isSignOut) {
                    signOut();
                  } else {
                    const isDelete = window.confirm('정말 회원 탈퇴를 진행하시겠습니까?\n모든 정보가 영구 파괴됩니다.');
                    if (isDelete) {
                      handleDeleteAccount();
                    }
                  }
                }}
              >
                {user.photoURL ? (
                  <img src={user.photoURL} alt="" className="w-full h-full object-cover" />
                ) : (
                  <span className="text-[#141414] text-[12px] font-bold">
                    {(user.displayName?.[0] || user.email?.[0] || 'U').toUpperCase()}
                  </span>
                )}
              </motion.button>
            ) : (
              <motion.button
                className="h-9 px-3 bg-[#141414]/5 backdrop-blur-md rounded-[10px] flex items-center cursor-pointer border-none text-[#141414]/85 text-[12px] font-medium"
                whileTap={{ scale: 0.95 }}
                onClick={() => setAuthOpen(true)}
              >
                Sign In
              </motion.button>
            )}


          </div>
        </div>
      </motion.nav>

      {/* Auth Modal */}
      <AuthModal isOpen={authOpen} onClose={() => setAuthOpen(false)} />
    </>
  );
}
