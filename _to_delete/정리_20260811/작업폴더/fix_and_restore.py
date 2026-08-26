import re

with open('_to_delete/learning_index_백업_20260810/index.html', 'r', encoding='utf-8') as f:
    backup_content = f.read()

# 1. Update the click handler in backup_content to the new logic:
old_click = """    document.querySelectorAll('.chapter-card').forEach(card=>card.onclick=()=>{
      const ch = Number(card.dataset.chapter);
      if([1,2,3].includes(ch)){
        if (!isPaid && ch !== 1) {
          openGate();
          return;
        }
        loadChapter(ch);
        const chapterTitle = chapters[ch-1]; document.getElementById('chapterDetail').querySelector('.section-head h2').textContent = `챕터 ${ch} · ${chapterTitle}`;
        enterChapter();
      } else {
        notify(`${card.querySelector('h3').textContent} 챕터는 아직 준비중입니다.`);
      }
    });"""

new_click = """    document.querySelectorAll('.chapter-card').forEach(card=>card.onclick=()=>{
      const ch = Number(card.dataset.chapter);
      if (!isPaid && ch !== 1) {
        try{window.parent.postMessage({type:'inkword:need-purchase'},location.origin)}catch(e){}
        openGate();
        return;
      }
      if(chapterData[ch]){
        loadChapter(ch);
        const chapterTitle = chapters[ch-1]; document.getElementById('chapterDetail').querySelector('.section-head h2').textContent = `챕터 ${ch} · ${chapterTitle}`;
        enterChapter();
      } else {
        notify(`챕터 ${ch} · ${chapters[ch-1]} 장소는 순차 오픈 예정입니다.`);
      }
    });"""

content = backup_content.replace(old_click, new_click)

# Now read the 30-scene chapterData from public/learning/index.html
with open('public/learning/index.html', 'r', encoding='utf-8') as f:
    pub_content = f.read()

match = re.search(r'const chapterData = (\{.*?\n    \};)', pub_content, re.DOTALL)
if not match:
    print("Error: Could not find 30-scene chapterData in public/learning/index.html")
    exit(1)

ch30_data_str = "const chapterData = " + match.group(1)

# In backup content, find the EXACT bounds of const chapterData = { ... };
# From "const chapterData = {" to "};\n    document.querySelectorAll('.level-switch"
pattern = r'const chapterData = \{.*?\};\n    document\.querySelectorAll\(\'\.level-switch'
replacement = ch30_data_str + "\n    document.querySelectorAll('.level-switch"

restored_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('public/learning/index.html', 'w', encoding='utf-8') as f:
    f.write(restored_content)

with open('dist/learning/index.html', 'w', encoding='utf-8') as f:
    f.write(restored_content)

print("SUCCESSFULLY RESTORED AND INTEGRATED 30 SCENES IN public AND dist index.html!")
