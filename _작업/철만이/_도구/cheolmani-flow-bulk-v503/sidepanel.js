let isRunning = false;

function log(msg, type = '') {
  const logEl = document.getElementById('log');
  const time = new Date().toLocaleTimeString('ko-KR', { hour12: false });
  let colorClass = '';
  if (type === 'error') colorClass = 'log-err';
  else if (type === 'success') colorClass = 'log-ok';
  else if (type === 'warn') colorClass = 'log-warn';
  
  logEl.innerHTML += `<div><span class="log-time">[${time}]</span> <span class="${colorClass}">${msg}</span></div>`;
  logEl.scrollTop = logEl.scrollHeight;
}

document.getElementById('btn-start').addEventListener('click', async () => {
  if (isRunning) return;
  const input = document.getElementById('bulk-input').value;
  const lines = input.split('\n').filter(l => l.includes('|'));
  
  if (lines.length === 0) {
    log('올바른 프롬프트 라인( | 포함)을 찾을 수 없습니다.', 'error');
    return;
  }
  
  isRunning = true;
  document.getElementById('btn-start').disabled = true;
  document.getElementById('bulk-input').disabled = true;
  log(`총 ${lines.length}개 컷 스케줄 시작...`, 'success');
  
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab || !tab.url.includes('labs.google/fx')) {
    log('오류: 활성화된 탭이 Google Labs Flow 사이트가 아닙니다.', 'error');
    isRunning = false;
    document.getElementById('btn-start').disabled = false;
    document.getElementById('bulk-input').disabled = false;
    return;
  }

  for (let i = 0; i < lines.length; i++) {
    if (!isRunning) break;
    document.getElementById('progress-status').textContent = `${i + 1} / ${lines.length}`;
    
    const line = lines[i].trim();
    const splitIdx = line.indexOf('|');
    const cutNo = line.substring(0, splitIdx).trim();
    let promptText = line.substring(splitIdx + 1).trim();
    
    log(`-----------------------------------`);
    log(`[${cutNo}] 컷 작업 시작...`);
    
    try {
      let result = await chrome.tabs.sendMessage(tab.id, { 
        action: 'run_prompt', 
        prompt: promptText
      });
      
      if (result && result.status === 'error') {
        log(`[${cutNo}] 1차 시도 실패: ${result.msg}`, 'error');
        log(`[${cutNo}] 1회 재시도 진입...`, 'warn');
        
        await new Promise(r => setTimeout(r, 2000));
        result = await chrome.tabs.sendMessage(tab.id, { 
          action: 'run_prompt', 
          prompt: promptText
        });
        
        if (result && result.status === 'success') {
          log(`[${cutNo}] 재시도 성공!`, 'success');
        } else {
          log(`[${cutNo}] 재시도 실패. 다음 컷으로 건너뜁니다. (${result?.msg})`, 'error');
        }
      } else if (result && result.status === 'success') {
        log(`[${cutNo}] 다운로드 완료! (수확 폴더 확인 요망)`, 'success');
      } else {
         log(`[${cutNo}] 알 수 없는 응답입니다.`, 'warn');
      }
      
    } catch (e) {
      log(`연결 오류: 페이지를 새로고침하고 다시 시도하세요. (${e.message})`, 'error');
      break;
    }
    
    // 다음 컷 전에 짧은 대기
    if (i < lines.length - 1 && isRunning) {
      log('다음 컷 준비 중 (5초 대기)...');
      await new Promise(r => setTimeout(r, 5000));
    }
  }
  
  log('===================================');
  log('배치 작업이 종료되었습니다.', 'success');
  isRunning = false;
  document.getElementById('btn-start').disabled = false;
  document.getElementById('bulk-input').disabled = false;
});

document.getElementById('btn-stop').addEventListener('click', () => {
  if (isRunning) {
    isRunning = false;
    log('긴급 정지: 사용자에 의해 작업이 중단되었습니다.', 'error');
    document.getElementById('btn-start').disabled = false;
    document.getElementById('bulk-input').disabled = false;
  }
});
