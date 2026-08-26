// cheolmani-flow-bulk-v504 content.js
// 코다리 총괄부장 개수 에디션 - React 입력 & Enter 키 & 상태 폴링 완벽 지원

function setNativeValue(element, value) {
  const valueSetter = Object.getOwnPropertyDescriptor(element, 'value')?.set;
  const prototype = Object.getPrototypeOf(element);
  const prototypeValueSetter = Object.getOwnPropertyDescriptor(prototype, 'value')?.set;
  
  if (prototypeValueSetter && valueSetter !== prototypeValueSetter) {
    prototypeValueSetter.call(element, value);
  } else if (valueSetter) {
    valueSetter.call(element, value);
  } else {
    element.value = value;
  }
}

function findPromptBox() {
  const inputs = Array.from(document.querySelectorAll('textarea, input[type="text"], [contenteditable="true"]'));
  if (inputs.length === 0) return null;

  // 1. Placeholder 우선 탐색
  let target = inputs.find(el => {
    const ph = (el.getAttribute('placeholder') || '').toLowerCase();
    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
    return ph.includes('prompt') || ph.includes('프롬프트') || ph.includes('describe') || ph.includes('입력') ||
           aria.includes('prompt') || aria.includes('프롬프트');
  });

  // 2. 가장 넓은 textarea 또는 contenteditable
  if (!target) {
    target = inputs.reduce((prev, curr) => {
      const prevRect = prev.getBoundingClientRect();
      const currRect = curr.getBoundingClientRect();
      return (currRect.width * currRect.height > prevRect.width * prevRect.height) ? curr : prev;
    }, inputs[0]);
  }

  return target;
}

function findGenerateButton(promptBox) {
  const buttons = Array.from(document.querySelectorAll('button, [role="button"], input[type="submit"]'));
  
  // 1. 텍스트 / aria-label 기반 탐색
  let btn = buttons.find(b => {
    const txt = (b.innerText || b.textContent || '').trim().toLowerCase();
    const aria = (b.getAttribute('aria-label') || '').toLowerCase();
    return txt === 'generate' || txt === '생성' || txt === 'create' || txt === 'run' || txt === 'submit' ||
           aria.includes('generate') || aria.includes('생성') || aria.includes('submit') || aria.includes('send');
  });

  // 2. 입력창 주변의 버튼(SVG 포함)
  if (!btn && promptBox) {
    const container = promptBox.closest('form, div[class*="container"], div[class*="input"], div[class*="prompt"]') || promptBox.parentElement;
    if (container) {
      const nearBtns = container.querySelectorAll('button, [role="button"]');
      if (nearBtns.length > 0) {
        btn = nearBtns[nearBtns.length - 1];
      }
    }
  }

  return btn;
}

function findDownloadButton() {
  const elements = Array.from(document.querySelectorAll('button, a, [role="button"]'));
  return elements.find(el => {
    const txt = (el.innerText || el.textContent || '').toLowerCase();
    const aria = (el.getAttribute('aria-label') || '').toLowerCase();
    const isDownload = el.hasAttribute('download') || 
                       txt.includes('download') || txt.includes('다운로드') || 
                       aria.includes('download') || aria.includes('다운로드') ||
                       el.querySelector('svg path[d*="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"]') ||
                       el.querySelector('svg [class*="download"]');
    return isDownload && el.offsetParent !== null; // 화면에 보이는 요소
  });
}

function isGenerating() {
  // 스피너나 진행 표시 바 탐색
  const spinners = document.querySelectorAll('[class*="spinner"], [class*="loading"], [class*="progress"], [aria-busy="true"]');
  for (const s of spinners) {
    if (s.offsetParent !== null) return true;
  }
  
  // "생성 중" 텍스트 탐색
  const texts = Array.from(document.querySelectorAll('span, div, p'));
  const hasLoadingText = texts.some(t => {
    const txt = (t.innerText || '').toLowerCase();
    return (txt.includes('generating') || txt.includes('생성 중') || txt.includes('creating')) && t.offsetParent !== null;
  });
  
  return hasLoadingText;
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'inject_prompt') {
    (async () => {
      try {
        const promptBox = findPromptBox();
        if (!promptBox) {
          sendResponse({ status: 'error', msg: '프롬프트 입력창을 찾을 수 없습니다.' });
          return;
        }

        promptBox.focus();
        await new Promise(r => setTimeout(r, 150));

        // [중요] 이전 프롬프트 잔여물 완전 청소 (Select All & Clear)
        if (promptBox.tagName === 'TEXTAREA' || promptBox.tagName === 'INPUT') {
          setNativeValue(promptBox, '');
          promptBox.dispatchEvent(new Event('input', { bubbles: true }));
          promptBox.dispatchEvent(new Event('change', { bubbles: true }));
          
          await new Promise(r => setTimeout(r, 100));
          
          // 새 프롬프트 주입
          setNativeValue(promptBox, request.prompt);
          promptBox.dispatchEvent(new Event('input', { bubbles: true }));
          promptBox.dispatchEvent(new Event('change', { bubbles: true }));
        } else {
          // Contenteditable div 청소 및 주입
          promptBox.textContent = '';
          promptBox.dispatchEvent(new Event('input', { bubbles: true }));
          
          await new Promise(r => setTimeout(r, 100));
          
          promptBox.textContent = request.prompt;
          promptBox.dispatchEvent(new Event('input', { bubbles: true }));
          promptBox.dispatchEvent(new Event('change', { bubbles: true }));
        }

        await new Promise(r => setTimeout(r, 300));

        // 1. Enter 키 이벤트 날리기
        const enterDown = new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true });
        const enterPress = new KeyboardEvent('keypress', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true });
        const enterUp = new KeyboardEvent('keyup', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true });
        promptBox.dispatchEvent(enterDown);
        promptBox.dispatchEvent(enterPress);
        promptBox.dispatchEvent(enterUp);

        await new Promise(r => setTimeout(r, 500));

        // 2. 만약 아직 생성이 시작 안 되었다면 생성 버튼 직접 클릭
        const genBtn = findGenerateButton(promptBox);
        if (genBtn && !genBtn.disabled) {
          genBtn.click();
        }

        sendResponse({ status: 'started', msg: '프롬프트 입력 및 생성 트리거 완료' });
      } catch (err) {
        sendResponse({ status: 'error', msg: err.message });
      }
    })();
    return true;
  }

  if (request.action === 'check_status') {
    const generating = isGenerating();
    const dlBtn = findDownloadButton();
    sendResponse({ 
      generating: generating, 
      downloadAvailable: !!dlBtn 
    });
    return true;
  }

  if (request.action === 'trigger_download') {
    const dlBtn = findDownloadButton();
    if (dlBtn) {
      dlBtn.click();
      sendResponse({ status: 'success' });
    } else {
      sendResponse({ status: 'not_found' });
    }
    return true;
  }
});
