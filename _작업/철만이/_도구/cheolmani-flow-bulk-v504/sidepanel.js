// cheolmani-flow-bulk-v504 sidepanel.js
// 코다리 총괄부장 개수 에디션 - 타임아웃 방지 & 실시간 상태 폴링

let isRunning = false;

function log(msg, type = '') {
  const logEl = document.getElementById('log');
  const time = new Date().toLocaleTimeString('ko-KR', { hour12: false });
  let colorClass = '';
  if (type === 'error') colorClass = 'log-err';
  else if (type === 'success') colorClass = 'log-ok';
  else if (type === 'warn') colorClass = 'log-warn';
  else if (type === 'info') colorClass = 'log-info';
  
  logEl.innerHTML += `<div><span class="log-time">[${time}]</span> <span class="${colorClass}">${msg}</span></div>`;
  logEl.scrollTop = logEl.scrollHeight;
}

async function sendTabMessage(tabId, message) {
  return new Promise((resolve) => {
    chrome.tabs.sendMessage(tabId, message, (response) => {
      if (chrome.runtime.lastError) {
        resolve({ status: 'error', msg: chrome.runtime.lastError.message });
      } else {
        resolve(response);
      }
    });
  });
}

document.getElementById('btn-start').addEventListener('click', async () => {
  if (isRunning) return;
  const input = document.getElementById('bulk-input').value;
  const lines = input.split('\n').filter(l => l.includes('|'));
  
  if (lines.length === 0) {
    log('올바른 프롬프트 라인(| 구분자 포함)을 찾을 수 없습니다.', 'error');
    return;
  }
  
  isRunning = true;
  document.getElementById('btn-start').disabled = true;
  document.getElementById('bulk-input').disabled = true;
  log(`총 ${lines.length}개 컷 자동화 스케줄 시작...`, 'success');
  
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab || !tab.url.includes('labs.google')) {
    log('오류: 현재 활성화된 탭이 Google Labs Flow 사이트가 아닙니다.', 'error');
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
    
    document.getElementById('current-cut').textContent = cutNo;
    log(`-----------------------------------`);
    log(`[${cutNo}] 프롬프트 주입 및 생성 시작...`);
    
    try {
      // 1. 프롬프트 주입 및 생성 트리거 (즉시 응답)
      let res = await sendTabMessage(tab.id, { 
        action: 'inject_prompt', 
        prompt: promptText
      });
      
      if (res.status === 'error') {
        log(`[${cutNo}] 프롬프트 입력 실패: ${res.msg}`, 'warn');
        log(`[${cutNo}] 2초 후 재시도...`, 'warn');
        await new Promise(r => setTimeout(r, 2000));
        res = await sendTabMessage(tab.id, { action: 'inject_prompt', prompt: promptText });
      }

      if (res.status === 'error') {
        log(`[${cutNo}] 최종 실패. 다음 컷으로 건너뜁니다.`, 'error');
        continue;
      }

      log(`[${cutNo}] 생성 트리거 성공. 영상 생성 대기 중...`, 'info');

      // 2. 실시간 상태 폴링 (최대 140초 대기, 4초 간격 확인)
      let elapsed = 0;
      const maxWait = 140;
      let completed = false;

      // 최초 20초는 생성 진행 기본 대기
      await new Promise(r => setTimeout(r, 20000));
      elapsed += 20;

      while (isRunning && elapsed < maxWait) {
        await new Promise(r => setTimeout(r, 5000));
        elapsed += 5;

        const status = await sendTabMessage(tab.id, { action: 'check_status' });
        
        if (status && status.downloadAvailable) {
          log(`[${cutNo}] 생성 완료 감지! (${elapsed}초 소요)`, 'success');
          completed = true;
          break;
        } else {
          log(`[${cutNo}] 생성 진행 중... (${elapsed}초 경과)`, 'info');
        }
      }

      // 3. 다운로드 트리거
      log(`[${cutNo}] 다운로드 버튼 클릭 시도...`, 'info');
      const dlRes = await sendTabMessage(tab.id, { action: 'trigger_download' });
      if (dlRes && dlRes.status === 'success') {
        log(`[${cutNo}] 다운로드 트리거 완료!`, 'success');
      } else {
        log(`[${cutNo}] 다운로드 버튼 미발견 (자동 저장 확인 필요)`, 'warn');
      }
      
    } catch (e) {
      log(`[${cutNo}] 처리 중 오류 발생: ${e.message}`, 'error');
    }
    
    // 다음 컷 전에 휴식 대기
    if (i < lines.length - 1 && isRunning) {
      log('다음 컷 준비 중 (5초 후 시작)...', 'info');
      await new Promise(r => setTimeout(r, 5000));
    }
  }
  
  log('===================================');
  log('🎉 전체 벌크 작업이 완료되었습니다!', 'success');
  isRunning = false;
  document.getElementById('current-cut').textContent = '완료';
  document.getElementById('btn-start').disabled = false;
  document.getElementById('bulk-input').disabled = false;
});

document.getElementById('btn-stop').addEventListener('click', () => {
  if (isRunning) {
    isRunning = false;
    log('긴급 정지: 사용자에 의해 작업이 중단되었습니다.', 'error');
    document.getElementById('current-cut').textContent = '중단됨';
    document.getElementById('btn-start').disabled = false;
    document.getElementById('bulk-input').disabled = false;
  }
});
