const fs = require('fs');

const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

// The replacement code:
const targetToReplace = `document.getElementById('chapterDetail').querySelector('.header h2').textContent = \\\`CHAPTER \\\${String(ch).padStart(2,'0')}\\\`;`;
const newContent = `const chapterTitle = chapters[ch-1];
        document.getElementById('chapterDetail').querySelector('.section-head h2').textContent = \`챕터 \${ch} · \${chapterTitle}\`;`;

content = content.replace(targetToReplace, newContent);

fs.writeFileSync(path, content, 'utf8');
console.log('Update successful');
