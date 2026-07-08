// ============================================================
// HeroWords — 히어로 영상 위 "그림 → 단어" 오버레이
// 콜로세움 그림 위로 단어 가족이 한 글자씩 마커 글씨처럼 튀어나온다.
// 11초 주기로 무한 반복 (10초 영상 루프와 자연스럽게 맞물림).
// ============================================================
import { useEffect, useState, useRef } from 'react';

const WORDS = [
  { en: 'COLOSSEUM', ko: '콜로세움', top: '45%', left: '50%', size: 'clamp(32px,4vw,60px)', rot: -3, delay: 3.2 },
  { en: 'SKY', ko: '하늘', top: '15%', left: '15%', size: 'clamp(24px,3vw,46px)', rot: 2, delay: 4.6 },
  { en: 'ARCH', ko: '아치', top: '65%', left: '35%', size: 'clamp(24px,3vw,46px)', rot: -2, delay: 5.6 },
  { en: 'WALL', ko: '외벽', top: '35%', left: '75%', size: 'clamp(24px,3vw,46px)', rot: 3, delay: 6.6 },
  { en: 'GROUND', ko: '바닥', top: '80%', left: '20%', size: 'clamp(24px,3vw,46px)', rot: -2, delay: 7.6 },
];

const CYCLE_MS = 11000;

export default function HeroWords() {
  const [cycle, setCycle] = useState(0);
  
  useEffect(() => {
    const t = setInterval(() => setCycle((c) => c + 1), CYCLE_MS);
    return () => clearInterval(t);
  }, []);

  const lastPlay = useRef(0);

  const handleHover = (text: string) => {
    const now = Date.now();
    if (now - lastPlay.current < 400) return; // 400ms 이내 중복 실행 방지
    lastPlay.current = now;

    if (typeof window !== 'undefined' && window.speechSynthesis) {
      // iOS 첫 터치 시 cancel()이 먼저 호출되면 음성이 영구 차단되는 버그 방지
      if (window.speechSynthesis.speaking || window.speechSynthesis.pending) {
        window.speechSynthesis.cancel();
      }
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 1.0;
      
      const voices = window.speechSynthesis.getVoices();
      const bestVoice = voices.find(v => v.lang.startsWith('en') && v.name.includes('Samantha')) ||
                        voices.find(v => v.lang.startsWith('en') && v.name.includes('Google US English')) ||
                        voices.find(v => v.lang.startsWith('en') && v.name.includes('Aria')) ||
                        voices.find(v => v.lang === 'en-US');
      if (bestVoice) utterance.voice = bestVoice;
      
      window.speechSynthesis.speak(utterance);
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
      `}</style>
      {WORDS.map((w) => (
        <div
          key={w.en}
          onPointerEnter={(e) => { if (e.pointerType === 'mouse') handleHover(w.en); }}
          onClick={() => handleHover(w.en)}
          onTouchStart={() => handleHover(w.en)}
          className={`hw-word cursor-pointer hover:scale-110 transition-transform`}
          style={{ top: w.top, left: w.left, animationDelay: `${w.delay}s, 9.8s`,
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
                        marginTop: 2, textAlign: 'center',
                        textShadow: '0 0 6px rgba(255,255,255,.9)' }}>{w.ko}</div>
        </div>
      ))}
    </div>
  );
}
