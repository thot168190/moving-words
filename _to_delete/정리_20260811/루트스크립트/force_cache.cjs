const fs = require('fs');
const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

content = content.replace(/scene-ch1-10-poster\.jpg(\?v=\d+)?/g, 'scene-ch1-10-poster.jpg?v=4');
content = content.replace(/scene-ch1-10\.mp4(\?v=\d+)?/g, 'scene-ch1-10.mp4?v=4');

fs.writeFileSync(path, content, 'utf8');
console.log('Added cache buster v4');
