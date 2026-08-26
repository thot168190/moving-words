const fs = require('fs');

const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

// Inside loadChapter, we need to reset the activeWork and render the player
const loadChapterRegex = /setupWorks\(\);\s*\}/;
const patch = `setupWorks();
      activeWork = works[0];
      if(activeWork) {
        document.querySelectorAll('.work').forEach(x=>x.classList.remove('current'));
        const firstWork = document.querySelector('.work');
        if(firstWork) firstWork.classList.add('current');
        mainVideo.src=activeWork.video;
        mainVideo.load();
        mainPoster.src=activeWork.img;
        document.getElementById('nowLabel').textContent=\`LEARNING · \${activeWork.n}\`;
        document.getElementById('mainTitle').textContent=activeWork.title;
        renderWords(activeWork);
      }
    }`;

content = content.replace(loadChapterRegex, patch);

fs.writeFileSync(path, content, 'utf8');
console.log('Patch applied successfully');
