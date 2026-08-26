const fs=require('fs');const {JSDOM}=require('jsdom');
const html=fs.readFileSync('public/learning/index.html','utf8');
const errs=[];
const vc=new (require('jsdom').VirtualConsole)();
vc.on('jsdomError',e=>errs.push('JSDOM: '+(e.stack||e.message)));
vc.on('error',(...a)=>errs.push('console.error: '+a.join(' ')));
const dom=new JSDOM(html,{runScripts:'dangerously',resources:undefined,virtualConsole:vc,url:'http://localhost:8080/learning/index.html'});
setTimeout(()=>{
  if(errs.length){console.log('★ 오류 '+errs.length+'건\n');errs.slice(0,4).forEach(e=>console.log(e.slice(0,1400)+'\n---'));}
  else console.log('오류 없음 (렌더 확인)');
  const d=dom.window.document;
  console.log('\n[렌더 결과]');
  console.log('  .work 카드:', d.querySelectorAll('.work').length);
  console.log('  .chapter-card:', d.querySelectorAll('.chapter-card').length);
  console.log('  subChapterTabs:', d.getElementById('subChapterTabs')? '있음':'없음');
  process.exit(0);
},2500);
