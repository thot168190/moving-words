// ============================================================
// HeroDoodle — 히어로 배경 라이브 드로잉 애니메이션
// 영상 없이도 히어로가 살아 움직인다. 데모 엔진과 같은 원리:
// SVG 스트로크가 순서대로 그려지고, 머문 뒤 사라지고, 다음 그림.
// ============================================================
import { useEffect, useRef } from 'react';

const DOODLES: string[][] = [
  [ // apple
    'M60 40 C42 28 22 38 22 62 C22 86 40 106 60 100 C80 106 98 86 98 62 C98 38 78 28 60 40 Z',
    'M60 40 C59 32 61 26 66 18',
    'M67 27 C73 16 90 15 95 22 C90 32 74 36 67 27 Z',
    'M70 26 C78 23 86 22 92 23',
  ],
  [ // sun
    'M60 38 a22 22 0 1 1 -0.1 0 Z',
    'M60 6 L60 20 M98 22 L88 32 M114 60 L100 60 M98 98 L88 88 M60 114 L60 100 M22 98 L32 88 M6 60 L20 60 M22 22 L32 32',
    'M52 56 a2.5 2.5 0 1 0 0.1 0 M68 56 a2.5 2.5 0 1 0 0.1 0',
    'M50 66 C54 74 66 74 70 66',
  ],
  [ // house
    'M28 106 V62 H92 V106',
    'M20 62 L60 26 L100 62',
    'M78 40 V28 H88 V49',
    'M52 106 V82 H68 V106',
    'M34 70 h16 v14 h-16 Z',
  ],
  [ // fish
    'M16 62 C32 38 72 36 92 60 C74 84 34 84 16 62 Z',
    'M92 60 L110 44 L106 62 L110 78 Z',
    'M76 54 a3 3 0 1 0 0.1 0',
    'M60 46 C56 54 56 68 60 76',
  ],
];

const SPEED = 0.12; // px per ms

export default function HeroDoodle() {
  const svgRef = useRef<SVGSVGElement>(null);
  const runIdRef = useRef(0);

  useEffect(() => {
    const runId = ++runIdRef.current;
    let idx = 0;
    const wait = (ms: number) => new Promise((r) => setTimeout(r, ms));

    const drawPath = (path: SVGPathElement) =>
      new Promise<void>((resolve) => {
        const L = path.getTotalLength();
        path.style.strokeDasharray = `${L}`;
        path.style.strokeDashoffset = `${L}`;
        path.style.opacity = '1';
        const dur = Math.max(400, L / SPEED);
        const t0 = performance.now();
        const step = (t: number) => {
          if (runIdRef.current !== runId) return resolve();
          const p = Math.min(1, (t - t0) / dur);
          path.style.strokeDashoffset = `${L * (1 - p)}`;
          if (p < 1) requestAnimationFrame(step);
          else resolve();
        };
        requestAnimationFrame(step);
      });

    const loop = async () => {
      while (runIdRef.current === runId) {
        const svg = svgRef.current;
        if (!svg) return;
        const doodle = DOODLES[idx % DOODLES.length];
        idx++;
        svg.innerHTML = doodle
          .map(
            (d) =>
              `<path d="${d}" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"/>`
          )
          .join('');
        const paths = Array.from(svg.querySelectorAll('path'));
        for (const p of paths) {
          if (runIdRef.current !== runId) return;
          await drawPath(p as SVGPathElement);
        }
        await wait(1800);
        paths.forEach((p) => {
          (p as SVGPathElement).style.transition = 'opacity 0.8s';
          (p as SVGPathElement).style.opacity = '0';
        });
        await wait(1000);
      }
    };
    loop();

    return () => {
      runIdRef.current++;
    };
  }, []);

  return (
    <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
      <svg
        ref={svgRef}
        viewBox="0 0 120 120"
        className="w-[46vmin] h-[46vmin]"
        style={{ opacity: 0.33 }}
      />
    </div>
  );
}
