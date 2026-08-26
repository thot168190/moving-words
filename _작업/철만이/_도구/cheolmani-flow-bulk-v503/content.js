chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'run_prompt') {
    (async () => {
      try {
        // 1. Find the prompt input box
        // Check for textareas or contenteditable divs
        const inputs = Array.from(document.querySelectorAll('textarea, [contenteditable="true"]'));
        
        // Usually the largest textarea is the prompt box, or the one with specific placeholder
        let promptBox = inputs.find(el => {
          const ph = el.getAttribute('placeholder') || '';
          return ph.toLowerCase().includes('prompt') || ph.includes('프롬프트') || ph.includes('입력');
        }) || inputs[0];

        if (!promptBox) throw new Error('프롬프트 입력창을 찾을 수 없습니다.');
        
        // 2. Paste the prompt
        if (promptBox.tagName === 'TEXTAREA' || promptBox.tagName === 'INPUT') {
          promptBox.value = request.prompt;
          promptBox.dispatchEvent(new Event('input', { bubbles: true }));
          promptBox.dispatchEvent(new Event('change', { bubbles: true }));
        } else {
          promptBox.textContent = request.prompt;
          promptBox.dispatchEvent(new Event('input', { bubbles: true }));
        }
        
        // Wait for UI to update
        await new Promise(r => setTimeout(r, 1000));
        
        // 3. Find and click the Generate button
        // Buttons might be <button> or <div> with role="button"
        const buttons = Array.from(document.querySelectorAll('button, [role="button"]'));
        
        let generateBtn = buttons.find(b => {
          const text = b.innerText.toLowerCase();
          return text.includes('생성') || 
                 text.includes('generate') || 
                 text.includes('create') ||
                 text.includes('run') ||
                 b.querySelector('svg'); // Sometimes it's just an icon next to the input
        });
        
        // If not found by text, try to find a button near the prompt box
        if (!generateBtn && buttons.length > 0) {
          generateBtn = buttons[buttons.length - 1]; // fallback heuristic
        }

        if (!generateBtn) throw new Error('생성 버튼을 찾을 수 없습니다.');
        
        generateBtn.click();
        
        // 4. Wait for 120 seconds (as per instructions)
        await new Promise(r => setTimeout(r, 120000));
        
        // 5. Find and click the Download button
        const downloadButtons = Array.from(document.querySelectorAll('button, a'));
        const downloadBtn = downloadButtons.find(b => {
          const text = b.innerText.toLowerCase();
          return text.includes('다운로드') || 
                 text.includes('download') || 
                 b.getAttribute('download') !== null ||
                 b.querySelector('svg path[d*="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"]'); // generic download icon path
        });
        
        if (downloadBtn) {
          downloadBtn.click();
          await new Promise(r => setTimeout(r, 2000)); // wait for download to start
        } else {
          console.warn('다운로드 버튼을 찾지 못했습니다.');
        }

        // Return success
        sendResponse({ status: 'success' });
        
      } catch (err) {
        console.error('Content Script Error:', err);
        sendResponse({ status: 'error', msg: err.message });
      }
    })();
    return true; // Keep channel open for async response
  }
});
