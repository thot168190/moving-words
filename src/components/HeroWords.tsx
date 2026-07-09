// ============================================================
// HeroWords — 히어로 영상 위 "그림 → 단어" 오버레이
// 콜로세움 그림 위로 단어 가족이 한 글자씩 마커 글씨처럼 튀어나온다.
// 11초 주기로 무한 반복 (10초 영상 루프와 자연스럽게 맞물림).
// ============================================================
import { useEffect, useState } from 'react';

const WORDS = [
  { en: 'COLOSSEUM', ko: '콜로세움', top: '45%', left: '50%', type: 'main', rot: -3, delay: 3.2 },
  { en: 'SKY', ko: '하늘', top: '15%', left: '15%', type: 'sub', rot: 2, delay: 4.6 },
  { en: 'ARCH', ko: '아치', top: '65%', left: '35%', type: 'sub', rot: -2, delay: 5.6 },
  { en: 'WALL', ko: '외벽', top: '35%', left: '75%', type: 'sub', rot: 3, delay: 6.6 },
  { en: 'GROUND', ko: '바닥', top: '80%', left: '20%', type: 'sub', rot: -2, delay: 7.6 },
];

const CYCLE_MS = 11000;

export default function HeroWords() {
  const [cycle, setCycle] = useState(0);
  
  useEffect(() => {
    const t = setInterval(() => setCycle((c) => c + 1), CYCLE_MS);
    return () => clearInterval(t);
  }, []);

  const handleHover = (text: string) => {
    if (typeof window !== 'undefined' && window.speechSynthesis) {
      window.speechSynthesis.cancel(); // 진행 중인 TTS 즉시 취소
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 1.0;
      
      const voices = window.speechSynthesis.getVoices();
      const bestVoice = voices.find(v => v.lang.startsWith('en') && v.name.includes('Samantha')) ||
                        voices.find(v => v.lang.startsWith('en') && v.name.includes('Google US English')) ||
                        voices.find(v => v.lang.startsWith('en') && v.name.includes('Aria')) ||
                        voices.find(v => v.lang === 'en-US');
      if (bestVoice) utterance.voice = bestVoice;
      
      // iOS는 cancel() 버그 방지를 위해 50ms 딜레이를 주고, 안드로이드/PC는 동기식으로 즉시 실행하여 user gesture 블로킹 방지
      const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || 
                    (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
      if (isIOS) {
        setTimeout(() => {
          window.speechSynthesis.speak(utterance);
        }, 50);
      } else {
        window.speechSynthesis.speak(utterance);
      }
    }
  };

  return (
    <div key={cycle} className="absolute inset-0 z-[8]">
      <style>{`
        @keyframes hw-pop {
          0% { opacity: 0; transform: translateY(16px) rotate(var(--rot)) scale(0.3); }
          60% { opacity: 1; transform: translateY(-3px) rotate(var(--rot)) scale(1.12); }
          100% { opacity: 1; transform: translateY(0) rotate(var(--rot)) scale(1); }
        }
        @keyframes hw-out { to { opacity: 0; } }
        .hw-word { position: absolute; opacity: 0; white-space: nowrap;
          animation: hw-pop .5s cubic-bezier(.2,1.6,.4,1) forwards,
                     hw-out .6s ease forwards 9.8s; }
        .hw-letter { display: inline-block; opacity: 0;
          animation: hw-pop .35s cubic-bezier(.2,1.6,.4,1) forwards; }
        
        /* 100% Guaranteed Sizes */
        .hw-main-en { font-size: 36px; }
        .hw-main-ko { font-size: 16px; }
        .hw-sub-en { font-size: 24px; }
        .hw-sub-ko { font-size: 14px; }
        @media (min-width: 768px) {
          .hw-main-en { font-size: 56px; }
          .hw-main-ko { font-size: 24px; }
          .hw-sub-en { font-size: 36px; }
          .hw-sub-ko { font-size: 18px; }
        }
      `}</style>
      {WORDS.map((w) => (
        <div
          key={w.en}
          onMouseEnter={() => handleHover(w.en)}
          onClick={() => handleHover(w.en)}
          onTouchEnd={() => handleHover(w.en)}
          className="hw-word cursor-pointer hover:scale-110 transition-transform"
          style={{ top: w.top, left: w.left, animationDelay: `${w.delay}s, 9.8s`,
                   ['--rot' as string]: `${w.rot}deg` }}
        >
          <div className={w.type === 'main' ? 'hw-main-en' : 'hw-sub-en'}
               style={{ fontFamily: '"Space Mono", monospace', fontWeight: 900,
                        color: '#111', lineHeight: 1,
                        textShadow: '-1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff, 0 0 8px rgba(255,255,255,0.9), 0 0 12px rgba(255,255,255,0.8)' }}>
            {[...w.en].map((c, i) => (
              <span key={i} className="hw-letter"
                    style={{ animationDelay: `${w.delay + i * 0.07}s` }}>{c}</span>
            ))}
          </div>
          <div className={w.type === 'main' ? 'hw-main-ko' : 'hw-sub-ko'}
               style={{ color: '#c2410c', fontWeight: 900,
                        marginTop: 4, textAlign: 'center',
                        textShadow: '-1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff, 0 0 6px rgba(255,255,255,1)' }}>{w.ko}</div>
        </div>
      ))}
    </div>
  );
}
