// popup.js
// 사이드패널 UI와 큐 저장만 담당합니다. 실제 Flow 조작은 content.js가 합니다.

const $ = (id) => document.getElementById(id);
const MAX_INGREDIENT_IMAGES = 3;

let queue = [];
let pollTimer = null;
let ingredientImages = [];

const els = {
  ingredientDropZone: $('ingredientDropZone'),
  ingredientInput: $('ingredientInput'),
  ingredientClearButton: $('ingredientClearButton'),
  ingredientInfo: $('ingredientInfo'),
  uploadHint: $('uploadHint'),
  promptText: $('promptText'),
  clearButton: $('clearButton'),
  queueInfo: $('queueInfo'),
  delayMin: $('delayMin'),
  delayMax: $('delayMax'),
  waitAfter: $('waitAfter'),
  pauseBeforeEach: $('pauseBeforeEach'),
  pauseHint: $('pauseHint'),
  dryRun: $('dryRun'),
  promptSelector: $('promptSelector'),
  generateSelector: $('generateSelector'),
  startButton: $('startButton'),
  resumeButton: $('resumeButton'),
  stopButton: $('stopButton'),
  continueButton: $('continueButton'),
  diagnoseButton: $('diagnoseButton'),
  statusText: $('statusText'),
  countText: $('countText'),
  progressBar: $('progressBar'),
  logBox: $('logBox')
};

restoreSettings();
bindEvents();
refreshQueue();
pollProgress();

function bindEvents() {
  els.promptText.addEventListener('input', () => {
    refreshQueue();
    saveSettings();
  });

  [
    els.delayMin,
    els.delayMax,
    els.waitAfter,
    els.pauseBeforeEach,
    els.dryRun,
    els.promptSelector,
    els.generateSelector
  ].forEach((element) => element.addEventListener('change', saveSettings));
  els.pauseBeforeEach.addEventListener('change', syncPauseMode);

  els.ingredientInput.addEventListener('change', loadIngredientFiles);
  els.ingredientDropZone.addEventListener('paste', handleIngredientPaste);
  els.ingredientDropZone.addEventListener('dragover', handleIngredientDragOver);
  els.ingredientDropZone.addEventListener('dragleave', handleIngredientDragLeave);
  els.ingredientDropZone.addEventListener('drop', handleIngredientDrop);
  els.ingredientDropZone.addEventListener('click', () => els.ingredientDropZone.focus());
  els.ingredientClearButton.addEventListener('click', clearIngredientFiles);
  els.clearButton.addEventListener('click', () => {
    els.promptText.value = '';
    refreshQueue();
    saveSettings();
  });

  els.startButton.addEventListener('click', () => startBulk(false));
  els.resumeButton.addEventListener('click', () => startBulk(true));
  els.stopButton.addEventListener('click', stopBulk);
  els.continueButton.addEventListener('click', continueBulk);
  els.diagnoseButton.addEventListener('click', diagnoseFlow);

  chrome.storage.onChanged.addListener((changes, area) => {
    if (area !== 'local') return;

    if (changes.flowBulkProgress) {
      renderProgress(changes.flowBulkProgress.newValue);
    }

    if (changes.flowBulkWaiting) {
      els.continueButton.disabled = changes.flowBulkWaiting.newValue !== true;
    }
  });
}

async function loadIngredientFiles(event) {
  const files = Array.from(event.target.files || []);
  if (files.length === 0) return;

  await setIngredientFiles(files, '선택');
  event.target.value = '';
}

async function handleIngredientPaste(event) {
  const files = Array.from(event.clipboardData?.files || []).filter((file) => file.type.startsWith('image/'));
  if (files.length === 0) {
    addLocalLog('붙여넣기에서 이미지를 찾지 못했습니다. 이미지를 복사한 뒤 박스 안에서 Cmd+V 하세요.', 'warn');
    return;
  }

  event.preventDefault();
  await setIngredientFiles(files, '붙여넣기');
}

function handleIngredientDragOver(event) {
  event.preventDefault();
  els.ingredientDropZone.classList.add('active');
}

function handleIngredientDragLeave() {
  els.ingredientDropZone.classList.remove('active');
}

async function handleIngredientDrop(event) {
  event.preventDefault();
  els.ingredientDropZone.classList.remove('active');

  const files = Array.from(event.dataTransfer?.files || []).filter((file) => file.type.startsWith('image/'));
  if (files.length === 0) {
    addLocalLog('드롭된 이미지가 없습니다.', 'warn');
    return;
  }

  await setIngredientFiles(files, '드롭');
}

async function setIngredientFiles(files, sourceLabel) {
  const imageFiles = Array.from(files).filter((file) => file.type.startsWith('image/'));
  const remainingSlots = Math.max(0, MAX_INGREDIENT_IMAGES - ingredientImages.length);
  const limitedFiles = imageFiles.slice(0, remainingSlots);

  if (remainingSlots === 0) {
    addLocalLog(`이미 ${MAX_INGREDIENT_IMAGES}/${MAX_INGREDIENT_IMAGES}개가 선택되어 있습니다. 이미지 비우기 후 다시 넣으세요.`, 'warn');
    return;
  }

  if (imageFiles.length > remainingSlots) {
    addLocalLog(`남은 자리는 ${remainingSlots}개라서 새 이미지 ${limitedFiles.length}개만 추가합니다.`, 'warn');
  }

  try {
    const newImages = await Promise.all(limitedFiles.map(fileToIngredientImage));
    ingredientImages = [...ingredientImages, ...newImages].slice(0, MAX_INGREDIENT_IMAGES);
    await saveIngredientImages();
    renderIngredientInfo();
    syncPauseMode();
    syncUploadMode();
    addLocalLog(`${sourceLabel}: ${newImages.length}개 추가, 현재 ${ingredientImages.length}/${MAX_INGREDIENT_IMAGES}개`, 'success');
  } catch (err) {
    addLocalLog(`이미지 로드 실패: ${err.message}`, 'error');
  }
}

async function clearIngredientFiles() {
  ingredientImages = [];
  await saveIngredientImages();
  renderIngredientInfo();
  syncPauseMode();
  syncUploadMode();
  addLocalLog('인그리디언트 이미지 비움');
}

function fileToIngredientImage(file) {
  return new Promise((resolve, reject) => {
    if (!file.type.startsWith('image/')) {
      reject(new Error(`${file.name}은 이미지 파일이 아닙니다.`));
      return;
    }

    const reader = new FileReader();
    reader.onload = () => {
      resolve({
        name: file.name,
        type: file.type || 'image/png',
        size: file.size,
        dataUrl: String(reader.result || '')
      });
    };
    reader.onerror = () => reject(new Error(`${file.name} 읽기 실패`));
    reader.readAsDataURL(file);
  });
}

async function saveIngredientImages() {
  // 이미지 data URL은 용량이 커서 별도 키로 저장합니다. 프롬프트 수정 때마다 다시 저장하지 않기 위함입니다.
  await chrome.storage.local.set({ flowBulkIngredientImages: ingredientImages });
}

function renderIngredientInfo() {
  if (ingredientImages.length === 0) {
    els.ingredientInfo.textContent = `선택된 이미지 없음 (최대 ${MAX_INGREDIENT_IMAGES}개)`;
    return;
  }

  els.ingredientInfo.innerHTML = '';
  const summary = document.createElement('div');
  summary.className = 'fileSummary';
  summary.textContent = `${ingredientImages.length}/${MAX_INGREDIENT_IMAGES}개 선택됨`;
  els.ingredientInfo.appendChild(summary);

  const grid = document.createElement('div');
  grid.className = 'thumbGrid';
  els.ingredientInfo.appendChild(grid);

  ingredientImages.forEach((image, index) => {
    const card = document.createElement('div');
    card.className = 'thumbCard';

    const img = document.createElement('img');
    img.src = image.dataUrl;
    img.alt = `${index + 1}번 인그리디언트`;

    const name = document.createElement('div');
    name.className = 'thumbName';
    name.textContent = `${index + 1}. ${image.name || '붙여넣은 이미지'}`;

    const size = document.createElement('div');
    size.className = 'thumbSize';
    size.textContent = formatBytes(image.size);

    card.appendChild(img);
    card.appendChild(name);
    card.appendChild(size);
    grid.appendChild(card);
  });
}

function refreshQueue() {
  queue = parsePromptLines(els.promptText.value);
  els.queueInfo.textContent = `${queue.length}개 대기`;
  els.startButton.disabled = queue.length === 0;
}

function syncPauseMode() {
  const hasPanelIngredients = ingredientImages.length > 0;
  if (hasPanelIngredients) els.pauseBeforeEach.checked = false;

  els.pauseBeforeEach.disabled = hasPanelIngredients;
  els.pauseHint.textContent = hasPanelIngredients
    ? '패널 인그리디언트 사용 중: 컷마다 멈춤은 자동으로 꺼졌습니다.'
    : '컷마다 Flow에서 직접 인그리디언트를 바꿀 때만 켜세요.';
}

function syncUploadMode() {
  // 이미지 있으면 항상 자동 업로드 — 별도 설정 불필요
}

function parsePromptLines(text) {
  const source = String(text || '').replace(/\r\n?/g, '\n').trim();
  if (!source) return [];

  // 새 컷번호가 나올 때만 프롬프트를 나눕니다. 설명 안의 줄바꿈과 빈 줄은 보존합니다.
  const bracketHeader = /^\s*\[((?=[^\]]*\d)[A-Za-z가-힣][A-Za-z0-9가-힣_-]{1,39})\]\s*(?:\|\s*)?(.*)$/;
  const plainHeader = /^\s*([A-Za-z]{0,4}\d+[-_]\d+[A-Za-z]?)\s*(?:\|\s+|\s+)(.*)$/;
  const lines = source.split('\n');
  const blocks = [];
  let current = null;

  for (const line of lines) {
    // [Camera], [Action] 같은 프롬프트 소제목은 숫자가 없으므로 새 컷으로 오인하지 않습니다.
    const match = line.match(bracketHeader) || line.match(plainHeader);
    if (match) {
      if (current) blocks.push(current);
      current = { cut: match[1].trim(), lines: [match[2]] };
    } else if (current) {
      current.lines.push(line);
    } else if (line.trim()) {
      // 컷번호가 전혀 없는 입력은 전체를 영상 한 개로 취급합니다.
      current = { cut: '', lines: [line] };
    }
  }
  if (current) blocks.push(current);

  return blocks.map((block, index) => {
    const joined = block.lines.join('\n').trim();
    const tripleSplit = joined.split(/\s*@@@\s*/);
    const videoSec = (tripleSplit.pop() || '').trim().match(/^(4s|6s|8s)$/)?.[1] || '8s';
    const body = videoSec && tripleSplit.length ? tripleSplit.join(' @@@ ').trim() : joined;
    const atSplit = body.split(/\s*@@\s*/);
    const prompt = atSplit[0].trim();
    const ingredients = atSplit.slice(1).join(';').split(/\s*;\s*/).map((s) => s.trim()).filter(Boolean);
    return { index, cut: block.cut, prompt, ingredients, videoSec };
  }).filter((item) => item.prompt);
}

async function startBulk(resume = false) {
  refreshQueue();
  if (queue.length === 0) return;

  const tab = await getFlowTab();
  if (!tab) return;

  const injected = await ensureContentScript(tab.id);
  if (!injected) {
    addLocalLog('content.js 주입 실패. Flow 탭 새로고침 후 다시 시도하세요.', 'error');
    return;
  }

  const settings = getSettings();
  const saved = await chrome.storage.local.get('flowBulkProgress');
  const startIndex = resume ? Math.min(saved.flowBulkProgress?.current || 0, queue.length) : 0;
  await chrome.storage.local.set({
    flowBulkQueue: queue,
    flowBulkSettings: settings,
    flowBulkProgress: { status: 'running', current: startIndex, total: queue.length, log: [] },
    flowBulkStartIndex: startIndex,
    flowBulkWaiting: false,
    flowBulkContinue: false
  });

  await chrome.tabs.sendMessage(tab.id, { type: 'START_BULK_V563' });
  els.startButton.disabled = true;
  els.stopButton.disabled = false;
  addLocalLog(resume ? `${startIndex + 1}번째부터 이어서 시작` : '처음부터 시작 신호 전송', 'success');
  pollProgress();
}

async function stopBulk() {
  const tab = await getFlowTab(false);
  await chrome.storage.local.set({ flowBulkWaiting: false, flowBulkContinue: false });
  if (tab) {
    try {
      await chrome.tabs.sendMessage(tab.id, { type: 'STOP_BULK_V563' });
    } catch {
      // Flow 탭이 닫힌 경우 저장 상태만 정리합니다.
    }
  }
  els.startButton.disabled = queue.length === 0;
  els.stopButton.disabled = true;
  els.continueButton.disabled = true;
}

async function continueBulk() {
  const tab = await getFlowTab(false);
  await chrome.storage.local.set({ flowBulkContinue: true, flowBulkWaiting: false });
  if (tab) {
    try {
      await chrome.tabs.sendMessage(tab.id, { type: 'CONTINUE_BULK_V563' });
    } catch {}
  }
  els.continueButton.disabled = true;
}

async function diagnoseFlow() {
  const tab = await getFlowTab();
  if (!tab) return;

  const injected = await ensureContentScript(tab.id);
  if (!injected) {
    addLocalLog('content.js 주입 실패', 'error');
    return;
  }

  await chrome.tabs.sendMessage(tab.id, { type: 'DIAGNOSE_FLOW_V563' });
  addLocalLog('진단 실행. 아래 로그를 확인하세요.', 'success');
  pollProgress();
}

async function getFlowTab(showAlert = true) {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab?.id || !/^https:\/\/labs\.google(\.com)?\//.test(tab.url || '')) {
    if (showAlert) addLocalLog('먼저 Google Flow 탭을 활성화하세요.', 'error');
    return null;
  }
  return tab;
}

async function ensureContentScript(tabId) {
  try {
    const response = await chrome.tabs.sendMessage(tabId, { type: 'PING_CONTENT_V563' });
    if (response?.ok && response.version === '5.6.3') return true;
  } catch {}

  try {
    await chrome.scripting.executeScript({
      target: { tabId },
      files: ['content.js']
    });
    await sleep(300);
    return true;
  } catch (err) {
    console.error('[FlowBulk] inject failed:', err);
    return false;
  }
}

function getSettings() {
  return {
    delayMinSec: Number(els.delayMin.value) || 35,
    delayMaxSec: Number(els.delayMax.value) || 55,
    waitAfterClickSec: Number(els.waitAfter.value) || 90,
    uploadIngredientsOnStart: ingredientImages.length > 0,
    pauseBeforeEach: ingredientImages.length > 0 ? false : els.pauseBeforeEach.checked,
    dryRun: els.dryRun.checked,
    ingredientImages,
    promptSelector: els.promptSelector.value.trim(),
    generateSelector: els.generateSelector.value.trim()
  };
}

async function saveSettings() {
  const { ingredientImages: _images, ...panelSettings } = getSettings();
  await chrome.storage.local.set({
    flowBulkPanelSettings: {
      promptText: els.promptText.value,
      ...panelSettings
    }
  });
}

async function restoreSettings() {
  const { flowBulkPanelSettings = {}, flowBulkIngredientImages = [] } = await chrome.storage.local.get([
    'flowBulkPanelSettings',
    'flowBulkIngredientImages'
  ]);
  ingredientImages = Array.isArray(flowBulkIngredientImages)
    ? flowBulkIngredientImages.slice(0, MAX_INGREDIENT_IMAGES)
    : [];
  if (flowBulkPanelSettings.promptText) els.promptText.value = flowBulkPanelSettings.promptText;
  if (flowBulkPanelSettings.delayMinSec) els.delayMin.value = flowBulkPanelSettings.delayMinSec;
  if (flowBulkPanelSettings.delayMaxSec) els.delayMax.value = flowBulkPanelSettings.delayMaxSec;
  if (flowBulkPanelSettings.waitAfterClickSec) els.waitAfter.value = flowBulkPanelSettings.waitAfterClickSec;
  // uploadIngredientsOnStart는 이미지 유무로 자동 결정 — 저장값 복원 불필요
  // 대표님 기본 작업 방식: Flow에 같은 인그리디언트를 세팅해두고
  // 프롬프트만 여러 줄 연속으로 돌린다. 멈춤 옵션은 명시적으로 저장된 경우에만 켠다.
  els.pauseBeforeEach.checked = flowBulkPanelSettings.pauseBeforeEach === true;
  els.dryRun.checked = Boolean(flowBulkPanelSettings.dryRun);
  els.promptSelector.value = flowBulkPanelSettings.promptSelector || '';
  els.generateSelector.value = flowBulkPanelSettings.generateSelector || '';
  renderIngredientInfo();
  syncPauseMode();
  syncUploadMode();
  refreshQueue();
}

async function pollProgress() {
  if (pollTimer) clearTimeout(pollTimer);
  const { flowBulkProgress, flowBulkWaiting } = await chrome.storage.local.get([
    'flowBulkProgress',
    'flowBulkWaiting'
  ]);

  if (flowBulkProgress) renderProgress(flowBulkProgress);
  els.continueButton.disabled = flowBulkWaiting !== true;

  pollTimer = setTimeout(pollProgress, 1000);
}

function renderProgress(progress) {
  const total = progress.total || 0;
  const current = progress.current || 0;

  els.statusText.textContent = statusLabel(progress.status);
  els.countText.textContent = `${current} / ${total}`;
  els.progressBar.max = Math.max(1, total);
  els.progressBar.value = Math.min(current, total);

  els.logBox.innerHTML = '';
  for (const entry of progress.log || []) {
    const div = document.createElement('div');
    div.className = entry.level || 'info';
    div.textContent = `[${entry.at}] ${entry.message}`;
    els.logBox.appendChild(div);
  }
  els.logBox.scrollTop = els.logBox.scrollHeight;

  const active = progress.status === 'running';
  els.stopButton.disabled = !active;
  els.startButton.disabled = active || queue.length === 0;
  els.resumeButton.disabled = active || queue.length === 0 || current <= 0 || current >= total;
}

function statusLabel(status) {
  return {
    idle: '대기',
    running: '실행 중',
    done: '완료',
    stopped: '정지',
    error: '오류'
  }[status] || status || '대기';
}

function addLocalLog(message, level = 'info') {
  const div = document.createElement('div');
  div.className = level;
  div.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
  els.logBox.appendChild(div);
  els.logBox.scrollTop = els.logBox.scrollHeight;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function formatBytes(bytes) {
  const size = Number(bytes) || 0;
  if (size < 1024) return `${size}B`;
  if (size < 1024 * 1024) return `${Math.round(size / 1024)}KB`;
  return `${(size / 1024 / 1024).toFixed(1)}MB`;
}
