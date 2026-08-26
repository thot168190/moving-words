const fs = require('fs');
const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

content = content.replace(
  /let activeWork=works\[0\];renderWords\(activeWork\);/,
  "let activeWork; loadChapter(1);"
);

fs.writeFileSync(path, content, 'utf8');
console.log('Fixed initialization');
