import { useEffect, useState, useRef } from 'react';

type PathData = { d: string; t?: string };
type SceneData = {
  id: string;
  vb: string;
  lineart: PathData[];
  img: string;
  en: string;
  ko: string;
  sw?: number;
};

export default function MetricsDoodle() {
  const [scenes, setScenes] = useState<SceneData[]>([]);
  const [idx, setIdx] = useState(0);
  const [act, setAct] = useState(1);
  const svgRef = useRef<SVGSVGElement>(null);
  const drawTokenRef = useRef(0);

  useEffect(() => {
    fetch('/metric-scenes.json?v=3')
      .then((r) => r.json())
      .then((d) => setScenes(d.scenes))
      .catch((e) => console.error('Failed to load metric-scenes:', e));
  }, []);

  const handleHover = (text: string) => {
    if (typeof window !== 'undefined' && window.speechSynthesis) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'en-US';
      utterance.rate = 1.0;
      
      const voices = window.speechSynthesis.getVoices();
      const bestVoice = voices.find(v => v.lang.startsWith('en') && v.name.includes('Samantha')) ||
                        voices.find(v => v.lang.startsWith('en') && v.name.includes('Google US English')) ||
                        voices.find(v => v.lang.startsWith('en') && v.name.includes('Aria')) ||
                        voices.find(v => v.lang === 'en-US');
      if (bestVoice) utterance.voice = bestVoice;
      
      const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || 
                    (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
      if (isIOS) {
        window.speechSynthesis.cancel(); // iOS만 cancel 적용
        setTimeout(() => {
          window.speechSynthesis.speak(utterance);
        }, 50);
      } else {
        // 안드로이드는 cancel() 시 비동기 레이스로 재생 취소되는 버그 예방을 위해 즉시 speak
        window.speechSynthesis.speak(utterance);
      }
    }
  };

  useEffect(() => {
    if (scenes.length === 0) return;
    const token = ++drawTokenRef.current;
    setAct(1);

    const runSequence = async () => {
      if (!svgRef.current) return;
      const paths = Array.from(svgRef.current.querySelectorAll('path'));
      
      if (paths.length > 0) {
        const lengths = paths.map(p => {
          p.style.transition = 'none';
          const L = p.getTotalLength();
          p.style.strokeDasharray = `${L}`;
          p.style.strokeDashoffset = `${L}`;
          return L;
        });
        
        let totalLength = 0;
        lengths.forEach(L => totalLength += L);
        
        const budget = 6000;
        const totalPause = paths.length * 40; // avg 40ms (20~60)
        const speed = totalLength / Math.max(1, budget - totalPause); // px per ms
        
        for (let i = 0; i < paths.length; i++) {
          if (drawTokenRef.current !== token) return;
          const p = paths[i];
          const L = lengths[i];
          const dur = L / speed;
          
          await new Promise<void>((res) => {
            const t0 = performance.now();
            const step = (t: number) => {
              if (drawTokenRef.current !== token) return res();
              const progress = dur > 0 ? Math.min(1, (t - t0) / dur) : 1;
              const ease = progress < 0.5 ? 2 * progress * progress : 1 - Math.pow(-2 * progress + 2, 2) / 2;
              p.style.strokeDashoffset = `${L * (1 - ease)}`;
              
              if (progress < 1) requestAnimationFrame(step);
              else res();
            };
            requestAnimationFrame(step);
          });
          
          if (drawTokenRef.current !== token) return;
          const pause = Math.random() * 40 + 20; // 20~60ms
          await new Promise(r => setTimeout(r, pause));
        }
      }
      
      if (drawTokenRef.current !== token) return;
      setAct(2); // 수채 시작
      
      await new Promise(r => setTimeout(r, 1500));
      if (drawTokenRef.current !== token) return;
      setAct(3); // 글자 뿅
      
      await new Promise(r => setTimeout(r, 2000));
      if (drawTokenRef.current !== token) return;
      setAct(4); // 글자 페이드
      
      await new Promise(r => setTimeout(r, 1000));
      if (drawTokenRef.current !== token) return;
      setIdx(i => (i + 1) % scenes.length); // 다음 장면
    };

    // DOM 마운트 후 안전하게 획 가져오기 위해 짧은 대기
    setTimeout(() => {
      if (drawTokenRef.current === token) runSequence();
    }, 50);

    return () => {
      drawTokenRef.current++;
    };
  }, [idx, scenes]);

  if (scenes.length === 0) return null;
  const sc = scenes[idx];

  return (
    <div className="w-full h-full relative flex items-center justify-center overflow-hidden z-10 pointer-events-none">
      <style>{`
        @keyframes md-pop {
          0% { opacity: 0; transform: translateY(14px) scale(0.3) rotate(-4deg); }
          60% { opacity: 1; transform: translateY(-3px) scale(1.15) rotate(1deg); }
          100% { opacity: 1; transform: translateY(0) scale(1) rotate(0); }
        }
        @keyframes md-fade-in {
          from { opacity: 0; transform: translateY(4px); }
          to { opacity: 1; transform: translateY(0); }
        }
      `}</style>

      <div 
        className="absolute inset-0 flex items-center justify-center transition-opacity duration-[1000ms]"
        style={{ opacity: act >= 3 ? 0 : 1 }}
      >
        <svg
          ref={svgRef}
          viewBox={sc.vb}
          className="absolute max-w-full max-h-full transition-opacity duration-[1500ms]"
          style={{ opacity: act >= 2 ? 0 : 1 }}
          fill="none"
          stroke="#1c1c1c"
          strokeWidth={sc.sw ?? 4}
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          {sc.lineart.map((p, i) => (
            <path key={i} d={p.d} transform={p.t || undefined} />
          ))}
        </svg>

        <img
          src={sc.img}
          alt={sc.ko}
          className="absolute max-w-full max-h-full object-contain"
          style={{ 
            opacity: act >= 2 ? 1 : 0,
            transform: act >= 2 ? 'scale(1)' : 'scale(1.015)',
            filter: act >= 2 ? 'blur(0)' : 'blur(3px)',
            transition: 'opacity 1.5s, transform 1.5s, filter 1.5s',
            transformOrigin: 'center'
          }}
        />
      </div>

      {(act === 3 || act === 4) && (
        <div
          className="absolute inset-0 flex flex-col items-center justify-center text-center transition-opacity duration-[1000ms] cursor-pointer pointer-events-auto hover:scale-110"
          style={{ 
            opacity: act === 4 ? 0 : 1, 
            fontFamily: "'Pretendard Variable', Pretendard, -apple-system, sans-serif",
            transition: 'transform 0.3s ease, opacity 1000ms'
          }}
          onMouseEnter={() => handleHover(sc.en)}
          onClick={() => handleHover(sc.en)}
          onTouchEnd={() => handleHover(sc.en)}
        >
          <div
            className="font-extrabold text-[#141414] leading-none tracking-[-0.02em]"
            style={{ fontSize: 'clamp(40px, 6vw, 76px)' }}
          >
            {[...sc.en].map((char, i) => (
              <span
                key={i}
                className="inline-block opacity-0"
                style={{ animation: `md-pop 0.4s cubic-bezier(0.2, 1.6, 0.4, 1) ${i * 0.05}s forwards` }}
              >
                {char}
              </span>
            ))}
          </div>
          <div 
            className="font-bold text-[#ff6b00] mt-3 opacity-0"
            style={{ 
              fontSize: 'clamp(20px, 3vw, 28px)',
              animation: `md-fade-in 0.4s ease forwards ${sc.en.length * 0.05 + 0.3}s`
            }}
          >
            {sc.ko}
          </div>
        </div>
      )}
    </div>
  );
}
