const fs = require('fs');
const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

// Change FREE_SCENES to 5 so all are open
content = content.replace(/const FREE_SCENES=3;/g, 'const FREE_SCENES=5;');

fs.writeFileSync(path, content, 'utf8');
console.log('Fixed FREE_SCENES');
