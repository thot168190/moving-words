const fs = require('fs');

const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

// Fix 1: The click handler error
content = content.replace(
  /document\.getElementById\('chapterDetail'\)\.querySelector\('\.header h2'\)\.textContent = `CHAPTER \$\{String\(ch\)\.padStart\(2,'0'\)\}`;/g,
  "const chapterTitle = chapters[ch-1]; document.getElementById('chapterDetail').querySelector('.section-head h2').textContent = `챕터 ${ch} · ${chapterTitle}`;"
);

// Fix 2: The chapter map rendering (making 3 and 4 look open)
// Original: chapterGrid.innerHTML=chapters.map((name,i)=>\`<button class="chapter-card \${i===0?'open':'locked-chapter'}"
content = content.replace(
  /class="chapter-card \$\{i===0\?'open':'locked-chapter'\}"/g,
  'class="chapter-card ${[0,2,3].includes(i)?\'open\':\'locked-chapter\'}"'
);
content = content.replace(
  /\$\{i===0\?'':\'<i class="key" aria-hidden="true"><\/i>'\}/g,
  '${[0,2,3].includes(i)?\'\':\'<i class="key" aria-hidden="true"></i>\'}'
);

fs.writeFileSync(path, content, 'utf8');
console.log('Final fix applied');
