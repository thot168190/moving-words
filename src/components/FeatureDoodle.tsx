// ============================================================
// FeatureDoodle — 기술 섹션 카드용 "그려지는 미니 아이콘"
// 스크롤로 카드가 보이는 순간 잉크 선이 아이콘을 그린다.
// 순서: 눈(본다) → 손(만진다) → 소리(듣는다) → 고리(묶는다)
// ============================================================
import { useEffect, useRef } from 'react';

const ICONS: string[][] = [
  [ // 0: 눈 — 그려지는 과정을 본다
    'M6 30 C20 12 44 12 58 30 C44 48 20 48 6 30 Z',
    'M32 22 a8 8 0 1 0 0.1 0',
    'M32 27 a3 3 0 1 0 0.1 0',
  ],
  [ // 1: 손가락 터치 — 만지면 변신
    'M32 8 v20',
    'M32 28 c0 -4 8 -4 8 0 v4 c0 -4 8 -4 8 0 v4 c0 -4 7 -3 7 1 v6 c0 8 -6 14 -14 14 h-6 c-5 0 -9 -2 -12 -6 l-8 -11 c-3 -4 2 -8 6 -5 l5 4 v-27 c0 -5 6 -5 6 0',
    'M24 12 a11 11 0 0 1 16 0',
  ],
  [ // 2: 스피커 — 발음까지 한 번에
    'M10 26 h8 l10 -9 v30 l-10 -9 h-8 Z',
    'M36 22 c4 4 4 12 0 16',
    'M42 17 c7 7 7 19 0 26',
    'M48 12 c10 10 10 26 0 36',
  ],
  [ // 3: 사슬 고리 — 장면=단어 가족으로 묶는다
    'M20 34 a10 10 0 0 1 0 -14 l8 -8 a10 10 0 0 1 14 14 l-4 4',
    'M44 30 a10 10 0 0 1 0 14 l-8 8 a10 10 0 0 1 -14 -14 l4 -4',
  ],
];

export default function FeatureDoodle({ index, className, color = '#141414' }: { index: number; className?: string; color?: string }) {
  const svgRef = useRef<SVGSVGElement>(null);
  const doneRef = useRef(false);

  useEffect(() => {
    const svg = svgRef.current;
    if (!svg) return;
    const paths = Array.from(svg.querySelectorAll('path')) as SVGPathElement[];
    paths.forEach((p) => {
      const L = p.getTotalLength();
      p.style.strokeDasharray = `${L}`;
      p.style.strokeDashoffset = `${L}`;
    });
    const io = new IntersectionObserver(
      (entries) => {
        if (!entries[0].isIntersecting || doneRef.current) return;
        doneRef.current = true;
        let delay = index * 250; // 카드 순서대로 시차
        paths.forEach((p) => {
          const L = p.getTotalLength();
          const dur = Math.max(250, L * 6);
          p.style.transition = `stroke-dashoffset ${dur}ms ease ${delay}ms`;
          requestAnimationFrame(() => { p.style.strokeDashoffset = '0'; });
          delay += dur * 0.7;
        });
        io.disconnect();
      },
      { threshold: 0.4 }
    );
    io.observe(svg);
    return () => io.disconnect();
  }, [index]);

  return (
    <svg
      ref={svgRef}
      viewBox="0 0 64 64"
      className={className || "w-10 h-10 sm:w-12 sm:h-12 mb-3"}
      fill="none"
      stroke={color}
      strokeWidth="2.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      {ICONS[index % ICONS.length].map((d, i) => (
        <path key={i} d={d} />
      ))}
    </svg>
  );
}
