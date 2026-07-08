// ============================================================
// HeroWords — 히어로 영상 위 "그림 → 단어" 오버레이
// 콜로세움 그림 위로 단어 가족이 한 글자씩 마커 글씨처럼 튀어나온다.
// 11초 주기로 무한 반복 (10초 영상 루프와 자연스럽게 맞물림).
// ============================================================
import { useEffect, useState } from 'react';

const WORDS = [
  { en: 'COLOSSEUM', ko: '콜로세움', top: '12%', right: '6%', size: 'clamp(28px,3.4vw,54px)', rot: -3, delay: 3.2 },
  { en: 'ROME', ko: '로마', top: '26%', right: '22%', size: 'clamp(20px,2.4vw,38px)', rot: 2, delay: 4.6 },
  { en: 'ARENA', ko: '경기장', top: '36%', right: '8%', size: 'clamp(20px,2.4vw,38px)', rot: -2, delay: 5.6 },
  { en: 'EMPIRE', ko: '제국', top: '48%', right: '20%', size: 'clamp(20px,2.4vw,38px)', rot: 3, delay: 6.6 },
  { en: 'GLADIATOR', ko: '검투사', top: '58%', right: '5%', size: 'clamp(20px,2.4vw,38px)', rot: -2, delay: 7.6 },
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
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 0.9;
      window.speechSynthesis.speak(utterance);
    }
  };

  return (
    <div key={cycle} className="absolute inset-0 pointer-events-none z-[8]">
      <style>{`
        @keyframes hw-pop {
          0% { opacity: 0; transform: translateY(16px) rotate(var(--rot)) scale(0.3); }
          60% { opacity: 1; transform: translateY(-3px) rotate(var(--rot)) scale(1.12); }
          100% { opacity: 1; transform: translateY(0) rotate(var(--rot)) scale(1); }
        }
        @keyframes hw-out { to { opacity: 0; } }
        .hw-word { position: absolute; opacity: 0;
          animation: hw-pop .5s cubic-bezier(.2,1.6,.4,1) forwards,
                     hw-out .6s ease forwards 9.8s; }
        .hw-letter { display: inline-block; opacity: 0;
          animation: hw-pop .35s cubic-bezier(.2,1.6,.4,1) forwards; }
          @media (max-width: 767px) { .hw-desktop-only { display: none; } }
      `}</style>
      {WORDS.map((w) => (
        <div
          key={w.en}
          onMouseEnter={() => handleHover(w.en)}
          onClick={() => handleHover(w.en)}
          onTouchStart={() => handleHover(w.en)}
          className={`hw-word pointer-events-auto cursor-pointer hover:scale-110 transition-transform ${w.en !== 'COLOSSEUM' ? 'hw-desktop-only' : ''}`}
          style={{ top: w.top, right: w.right, animationDelay: `${w.delay}s, 9.8s`,
                   ['--rot' as string]: `${w.rot}deg` }}
        >
          <div style={{ fontFamily: '"Space Mono", monospace', fontWeight: 700,
                        fontSize: w.size, color: '#111', lineHeight: 1,
                        textShadow: '0 0 6px rgba(255,255,255,.9)' }}>
            {[...w.en].map((c, i) => (
              <span key={i} className="hw-letter"
                    style={{ animationDelay: `${w.delay + i * 0.07}s` }}>{c}</span>
            ))}
          </div>
          <div style={{ fontSize: 'clamp(12px,1.1vw,16px)', color: '#c2410c', fontWeight: 700,
                        marginTop: 2, textAlign: 'right',
                        textShadow: '0 0 6px rgba(255,255,255,.9)' }}>{w.ko}</div>
        </div>
      ))}
    </div>
  );
}
