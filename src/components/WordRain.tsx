import { useState, useEffect, useRef } from 'react';

export default function WordRain() {
  const words = [
    'GALAXY', 'ROCKET', 'STAR', 'ORBIT', 'PLANET', 
    'MOON', 'COMET', 'LAUNCH', 'COSMOS', 'METEOR', 
    'SHINE', 'LIGHT', 'SPACE', 'GRAVITY', 'EARTH', 
    'SUN', 'ASTEROID', 'UNIVERSE', 'NEBULA', 'ECLIPSE'
  ];
  const colors = ['#9aa7d4','#c6a3cf','#a3c4d4','#b7a9d9','#cfb0c4'];
  const [drops, setDrops] = useState<{key:number;word:string;left:number;size:number;color:string;rot:number;dur:number}[]>([]);
  const idRef = useRef(0);
  
  useEffect(() => {
    let lastIndex = -1;
    const add = () => {
      let nextIndex = Math.floor(Math.random() * words.length);
      while (nextIndex === lastIndex) {
        nextIndex = Math.floor(Math.random() * words.length);
      }
      lastIndex = nextIndex;
      
      const d = { key:idRef.current++, word:words[nextIndex],
        left:Math.random()*92+2, size:32+Math.random()*48,
        color:colors[Math.floor(Math.random()*colors.length)],
        rot:Math.random()*12-6, dur:16+Math.random()*10 };
      setDrops(p => [...p, d]);
      setTimeout(() => setDrops(p => p.filter(x => x.key !== d.key)), d.dur*1000+400);
    };
    for (let i=0;i<6;i++) setTimeout(add, i*1800);
    const t = setInterval(add, 2200);
    return () => clearInterval(t);
  }, []);
  
  return (
    <div className="absolute inset-0 z-[1] overflow-hidden pointer-events-none hidden md:block">
      <style>{`@keyframes wr-fall{0%{transform:translateY(-8vh) rotate(var(--r));opacity:0}12%{opacity:.55}88%{opacity:.55}100%{transform:translateY(112vh) rotate(var(--r));opacity:0}}`}</style>
      {drops.map(d => (
        <div key={d.key} style={{
          position:'absolute', top:'-8%', left:d.left+'%', fontSize:d.size,
          fontWeight:900, color:d.color, whiteSpace:'nowrap',
          fontFamily:'"Space Grotesk", monospace',
          ['--r' as never]: d.rot+'deg',
          animation:`wr-fall ${d.dur}s linear forwards`,
        }}>{d.word}</div>
      ))}
    </div>
  );
}
