// content.js
// Google Flow 페이지에서 실행되는 자동화 본체입니다.
// 목표: 필요할 때만 인그리디언트 이미지 업로드 -> 프롬프트 입력 -> 생성 버튼 1회 클릭 -> 대기 -> 다음 컷.

(() => {
  if (window.__flowBulkRecoveryV563) return;
  window.__flowBulkRecoveryV563 = true;

  const INPUT_SELECTOR = [
    'textarea:not([disabled])',
    'input[type="text"]:not([disabled])',
    'input:not([type]):not([disabled])',
    '[contenteditable="true"]',
    '[contenteditable="plaintext-only"]',
    '[role="textbox"]'
  ].join(',');

  let stopped = false;
  let running = false;
  let cachedInput = null;
  let cachedButton = null;
  let progress = makeProgress('idle');

  chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'PING_CONTENT_V563') {
      sendResponse({ ok: true, version: '5.6.3' });
      return false;
    }

    if (message.type === 'START_BULK_V563') {
      runBulk().catch((err) => {
        log(`치명 오류: ${err.message}`, 'error');
        progress.status = 'error';
        saveProgress();
      });
      sendResponse({ ok: true });
      return false;
    }

    if (message.type === 'STOP_BULK_V563') {
      stopped = true;
      log('정지 요청 받음', 'warn');
      sendResponse({ ok: true });
      return false;
    }

    if (message.type === 'CONTINUE_BULK_V563') {
      chrome.storage.local.set({ flowBulkContinue: true });
      sendResponse({ ok: true });
      return false;
    }

    if (message.type === 'DIAGNOSE_FLOW_V563') {
      diagnose().then(sendResponse);
      return true;
    }
  });

  async function runBulk() {
    if (running) {
      await log('이미 실행 중입니다.', 'warn');
      return;
    }

    running = true;
    stopped = false;
    cachedInput = null;
    cachedButton = null;

    const { flowBulkQueue = [], flowBulkSettings = {}, flowBulkStartIndex = 0 } = await chrome.storage.local.get([
      'flowBulkQueue',
      'flowBulkSettings',
      'flowBulkStartIndex'
    ]);

    progress = makeProgress('running', flowBulkQueue.length);
    await saveProgress();

    if (flowBulkQueue.length === 0) {
      await log('큐가 비어 있습니다.', 'error');
      running = false;
      progress.status = 'error';
      await saveProgress();
      return;
    }

    await log(`총 ${flowBulkQueue.length}개 시작${flowBulkSettings.dryRun ? ' (드라이런)' : ''}`);

    // v5.3.4: 인그리디언트는 컷마다 processItem 안에서 첨부 상태를 보장한다.
    // (Flow가 생성 후 첨부를 초기화하는 경우 대비 — 최초 1회 업로드 설계 폐기)

    const firstIndex = Math.max(0, Math.min(Number(flowBulkStartIndex) || 0, flowBulkQueue.length));
    progress.current = firstIndex;
    await saveProgress();

    for (let index = firstIndex; index < flowBulkQueue.length; index++) {
      if (stopped) break;

      const item = flowBulkQueue[index];
      progress.current = index;
      await saveProgress();

      const ok = await processItem(item, index, flowBulkQueue.length, flowBulkSettings);
      if (!ok) {
        progress.status = 'error';
        await saveProgress();
        running = false;
        return;
      }

      progress.current = index + 1;
      await saveProgress();

      if (index < flowBulkQueue.length - 1 && !stopped) {
        const delay = randomInt(flowBulkSettings.delayMinSec || 30, flowBulkSettings.delayMaxSec || 45);
        await log(`다음 컷까지 ${delay}초 대기`);
        await sleepSeconds(delay);
      }
    }

    progress.status = stopped ? 'stopped' : 'done';
    await log(stopped ? '정지됨' : '전체 완료', stopped ? 'warn' : 'success');
    await saveProgress();
    running = false;
  }

  async function processItem(item, index, total, settings) {
    const label = item.cut ? `[${item.cut}]` : `#${index + 1}`;
    const prompt = String(item.prompt || '').trim();

    if (!prompt) {
      await log(`${label} 프롬프트가 비어 있어 건너뜀`, 'warn');
      return true;
    }

    await log(`${index + 1}/${total} ${label} 입력 시작`);

    if (settings.pauseBeforeEach) {
      await log(`${label} 인그리디언트 확인 대기: Flow에서 직접 세팅 후 "계속" 클릭`, 'warn');
      const continued = await waitForContinue();
      if (!continued) return false;
    }

    const input = await findPromptInput(settings.promptSelector);
    if (!input) {
      await log('프롬프트 입력창을 찾지 못했습니다. 진단 버튼으로 후보를 확인하세요.', 'error');
      return false;
    }
    cachedInput = input;
    await log(`입력창 확인: ${describePromptTarget(input)}`);

    await ensureGenerationSettings(item);

    const ingredientsReady = await ensureIngredientsAttached(settings, input, item);
    if (!ingredientsReady) {
      await log(`${label} 인그리디언트 첨부 실패`, 'error');
      return false;
    }

    if (!settings.dryRun) {
      const inputOk = await setInputValue(input, prompt);
      if (!inputOk) {
        await log(`${label} 입력 실패`, 'error');
        return false;
      }
      // React 상태 업데이트 대기
      await sleep(400);
    }

    await log(`${label} 프롬프트 입력 완료`, 'success');

    const button = await findGenerateButton(settings.generateSelector, input);
    if (!button) {
      await log('생성 버튼을 찾지 못했습니다. Flow 화면에서 입력창/버튼 위치를 확인하세요.', 'error');
      return false;
    }
    cachedButton = button;

    const buttonText = compactText(button);
    await log(`클릭 대상: "${buttonText || button.tagName.toLowerCase()}"`);

    if (!settings.dryRun) {
      // v5.4.1: 더블 생성 방지 — 클릭 후 입력창이 비었는지로 성공을 검증하고, 안 비었을 때만 재클릭
      const clicked = await clickGenerateVerified(button, input, prompt);
      if (!clicked) {
        await log('생성 버튼 클릭 실패', 'error');
        return false;
      }
      await log(`${label} 생성 클릭 완료`, 'success');

      // Flow가 제출 후에도 이전 프롬프트를 남겨두므로 실제 키보드 입력으로 비우고
      // 팝업을 닫습니다. 다음 컷은 반드시 새 입력창/버튼을 다시 탐색합니다.
      await resetComposerAfterSubmit(input);

      const waitSec = settings.waitAfterClickSec || 80;
      await log(`${waitSec}초 생성 대기`);
      await sleepSeconds(waitSec);
    }

    return true;
  }

  // v5.3.4: 미사용 (ensureIngredientsAttached 로 대체). 롤백 대비 보존.
  async function uploadIngredientsOnce(settings) {
    const images = Array.isArray(settings.ingredientImages) ? settings.ingredientImages : [];
    if (images.length === 0) {
      await log('업로드 이미지 없음: Flow에 이미 세팅된 인그리디언트를 그대로 사용');
      return true;
    }

    if (settings.dryRun) {
      await log(`드라이런: 인그리디언트 이미지 ${images.length}개 업로드 생략`);
      return true;
    }

    await log(`인그리디언트 이미지 ${images.length}개 — Flow 자동 업로드 시작`);

    // Flow 화면에 이미 file input이 있으면 버튼 클릭 없이 바로 주입합니다.
    let uploaded = await uploadIntoBestFileInput(images);
    if (uploaded) {
      await log('인그리디언트 파일 주입 완료', 'success');
      await sleep(2500);
      return true;
    }

    const ingredientButton = findIngredientEntryButton();
    if (!ingredientButton) {
      await log('인그리디언트 추가 버튼을 찾지 못했습니다. Flow 화면에서 업로드 영역이 보이는지 확인하세요.', 'error');
      await logUploadCandidates();
      return false;
    }

    await log(`인그리디언트 버튼 클릭: "${compactText(ingredientButton) || ingredientButton.tagName.toLowerCase()}"`);
    if (!(await clickOnce(ingredientButton))) {
      await log('인그리디언트 버튼 클릭 실패', 'error');
      return false;
    }
    await sleep(1200);

    const uploadButton = findUploadButton();
    if (uploadButton) {
      await log(`업로드 버튼 클릭: "${compactText(uploadButton) || uploadButton.tagName.toLowerCase()}"`);
      await clickOnce(uploadButton);
      await sleep(900);
    }

    uploaded = await uploadIntoBestFileInput(images);
    if (!uploaded) {
      await log('파일 선택 input을 찾지 못했습니다. 진단 버튼으로 업로드 후보를 확인하세요.', 'error');
      await logUploadCandidates();
      return false;
    }

    await log('인그리디언트 파일 주입 완료', 'success');
    await sleep(3000);
    return true;
  }

  async function uploadIntoBestFileInput(images, scope) {
    const inputs = deepQueryAll('input[type="file"]')
      .filter((input) => !input.disabled)
      .map((input) => ({
        input,
        score: scoreFileInput(input) + (scope && scope !== document.body && scope.contains(input) ? 200 : 0)
      }))
      .sort((a, b) => b.score - a.score);

    if (!inputs[0]) return false;
    return setFileInputFiles(inputs[0].input, images);
  }

  // v5.4.0: Flow 첨부 정식 경로 = 애셋 피커 (+ → 애셋 검색 → 행 선택 → "프롬프트에 추가")
  // 2026-07-11 라이브 DOM 채취로 확정. 파일 업로드 주입은 라이브러리로만 들어가서 폐기.

  // v5.5.0: 생성 설정 패널 자동화 — 2026-07-12 라이브 채취
  // 칩(닫힘): "🍌 Nano Banana Pro crop_16_9 1x" / 동영상 모드: "Veo 3.1 - Lite" + 4s/6s/8s
  // 패널 항목: 'image이미지' 'play_circle동영상' | 비율 | '1x' 'x2' 'x3' 'x4' | 모델 드롭다운 | "생성 시 N크레딧"
  // 주의: 일반 .click()으로는 패널이 안 열림 — 포인터 이벤트 시퀀스 필수.
  function pressLikeUser(el) {
    const rect = el.getBoundingClientRect();
    const x = rect.left + rect.width / 2;
    const y = rect.top + rect.height / 2;
    for (const type of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click']) {
      el.dispatchEvent(new PointerEvent(type, { bubbles: true, cancelable: true, clientX: x, clientY: y, pointerId: 1, isPrimary: true, button: 0 }));
    }
  }

  async function ensureGenerationSettings(item) {
    const wantSec = item?.videoSec || null; // '4s' | '6s' | '8s' | null(이미지)

    const chip = deepQueryAll('button, [role="button"]').filter(isVisible)
      .find((b) => /Nano Banana|Veo/i.test(compactText(b)));
    if (!chip) {
      await log('생성 설정 칩을 못 찾음 — 모드/초수/출력수 확인 생략', 'warn');
      return true;
    }
    pressLikeUser(chip);

    const panel = await waitFor(() => deepQueryAll('div').find((e) => isVisible(e) && /생성 시 .*크레딧/.test(compactText(e))), 4000);
    if (!panel) {
      await log('설정 패널이 안 열림 — 현재 설정 그대로 진행', 'warn');
      return true;
    }

    const pressOption = async (labels) => {
      for (const label of labels) {
        const el = deepQueryAll('button, [role="button"], [role="tab"], [role="radio"], div').filter(isVisible)
          .find((e) => compactText(e) === label);
        if (el) { pressLikeUser(el); await sleep(700); return true; }
      }
      return false;
    };

    if (wantSec) {
      if (!(await pressOption(['play_circle동영상', '동영상']))) await log('동영상 모드 토글 실패', 'warn');
      if (!(await pressOption([wantSec]))) await log(`초수 ${wantSec} 버튼 못 찾음`, 'warn');
      else await log(`동영상 모드 · ${wantSec} 설정`, 'success');
    } else {
      await pressOption(['image이미지', '이미지']);
    }

    // 대표님 기본 출력 비율: 가로형 16:9
    if (!(await pressOption(['crop_16_9', '16:9', '가로 16:9']))) {
      await log('16:9 버튼을 못 찾음 — 현재 비율을 꼭 확인하세요', 'warn');
    }

    // 출력 수 1x 강제 — 2장 생성(크레딧 2배) 원천 차단
    if (!(await pressOption(['1x']))) await log('출력 1x 버튼 못 찾음 — 프롬프트당 2장 이상 생성될 수 있음', 'warn');

    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
    await sleep(400);
    return true;
  }

  async function ensureIngredientsAttached(settings, input, item) {
    const names = Array.isArray(item?.ingredients) ? item.ingredients.filter(Boolean) : [];
    const legacyImages = Array.isArray(settings.ingredientImages) ? settings.ingredientImages : [];

    if (names.length === 0 && legacyImages.length === 0) return true;

    if (settings.dryRun) {
      await log(`드라이런: 인그리디언트 첨부 생략 (${names.join(', ') || '이미지 ' + legacyImages.length + '개'})`);
      return true;
    }

    if (names.length === 0) {
      await log('경고: 이미지 업로드 방식은 폐기됨 — 큐 줄 끝에 "@@ 애셋이름1; 애셋이름2" 형식으로 라이브러리 애셋 이름을 지정하세요. 이 컷은 첨부 없이 진행.', 'warn');
      return true;
    }

    const composer = findComposerBox(input);
    if (!composer) {
      await log('컴포저 박스를 못 찾았습니다', 'error');
      return false;
    }

    await clearComposerChips(composer);

    for (let i = 0; i < names.length; i++) {
      const ok = await attachAssetByName(names[i], composer);
      if (!ok) {
        await log(`인그리디언트 "${names[i]}" 첨부 실패 — 애셋 이름이 라이브러리와 정확히 같은지 확인`, 'error');
        return false;
      }
      await sleep(800);
    }

    const chips = countComposerChips(composer);
    if (chips < names.length) {
      await log(`경고: 첨부 칩 ${chips}/${names.length}개만 확인됨`, 'warn');
    } else {
      await log(`인그리디언트 ${chips}개 첨부 완료: ${names.join(' → ')}`, 'success');
    }
    return true;
  }

  function composerChipCancelButtons(composer) {
    if (!composer) return [];
    return Array.from(composer.querySelectorAll('button, [role="button"]'))
      .filter((button) => isVisible(button) && /^cancel$/i.test(compactText(button)));
  }

  function countComposerChips(composer) {
    return composerChipCancelButtons(composer).length;
  }

  async function clearComposerChips(composer) {
    for (let guard = 0; guard < 6; guard++) {
      const cancels = composerChipCancelButtons(composer);
      if (cancels.length === 0) return;
      await clickOnce(cancels[0]);
      await sleep(500);
    }
  }

  async function attachAssetByName(name, composer) {
    const plus = findComposerPlusButton(composer);
    if (!plus) {
      await log('컴포저 + 버튼(add_2)을 못 찾았습니다', 'error');
      return false;
    }
    await clickOnce(plus);

    const search = await waitFor(() => deepQueryAll('input').find((el) =>
      /애셋 검색/.test(`${el.placeholder || ''} ${el.getAttribute('aria-label') || ''}`) && isVisible(el)), 6000);
    if (!search) {
      await log('애셋 검색창이 안 떴습니다 (+ 클릭 후 피커 미표시)', 'error');
      return false;
    }

    if (!(await setSearchValue(search, name))) {
      await log('검색어 입력 실패', 'error');
      return false;
    }
    await sleep(900);

    const row = await waitFor(() => findAssetRow(name, search), 5000);
    if (!row) {
      await log(`애셋 "${name}"이 검색 결과에 없습니다`, 'error');
      return false;
    }
    await clickOnce(row);
    await sleep(700);

    const addButton = await waitFor(() => deepQueryAll('button, [role="button"]').find((button) =>
      /프롬프트에 추가/.test(compactText(button)) && isVisible(button)), 5000);
    if (!addButton) {
      await log('"프롬프트에 추가" 버튼이 안 떴습니다', 'error');
      return false;
    }
    await clickOnce(addButton);
    await sleep(900);
    return true;
  }

  function findAssetRow(name, searchInput) {
    const needle = String(name).toLowerCase().replace(/\s+/g, ' ').trim();
    const searchRect = searchInput.getBoundingClientRect();
    const rows = deepQueryAll('div, li, [role="option"]').filter((el) => {
      const rect = el.getBoundingClientRect();
      if (!(rect.top > searchRect.bottom - 4 && rect.height > 36 && rect.height < 80 && rect.width > 150 && rect.width < 340)) return false;
      const text = compactText(el).toLowerCase();
      return text.startsWith(needle) || text.includes(needle);
    });
    return rows[0] || null;
  }

  async function setSearchValue(input, value) {
    input.focus();
    await sleep(120);
    const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value')?.set;
    if (!setter) return false;
    setter.call(input, '');
    input.dispatchEvent(new Event('input', { bubbles: true }));
    setter.call(input, value);
    input.dispatchEvent(new InputEvent('input', { bubbles: true, data: value, inputType: 'insertText' }));
    await sleep(150);
    return String(input.value || '').toLowerCase().includes(String(value).slice(0, 4).toLowerCase());
  }

  async function waitFor(conditionFn, timeoutMs) {
    const startedAt = Date.now();
    while (Date.now() - startedAt < timeoutMs) {
      try {
        const value = conditionFn();
        if (value) return value;
      } catch {}
      await sleep(250);
    }
    return null;
  }

  function findComposerPlusButton(composer) {
    if (!composer || composer === document.body) return null;
    const buttons = Array.from(composer.querySelectorAll('button, [role="button"]'))
      .filter(isUsableButton)
      .map((button) => ({ button, score: scoreComposerPlusButton(button) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score);
    return buttons[0]?.button || null;
  }

  function scoreComposerPlusButton(button) {
    const label = buttonLabel(button);
    const text = compactText(button);
    const rect = button.getBoundingClientRect();
    let score = 0;

    if (/add_2/.test(text) || /add_2/.test(label)) score += 150;   // Flow 컴포저 + 버튼 = "add_2만들기"
    if (/^\+$|^add\b/.test(text)) score += 80;
    if (/attach|첨부|업로드|upload/.test(label)) score += 40;
    if (/arrow_forward|send|에이전트|agent|nano|cancel|close/.test(label)) score -= 400;
    if (rect.width <= 60 && rect.height <= 60) score += 30;

    return score;
  }

  async function logUploadCandidates() {
    const inputs = deepQueryAll('input[type="file"]').slice(0, 10);
    const buttons = deepQueryAll('button, [role="button"], [aria-label], [title]')
      .filter(isVisible)
      .map((button) => compactText(button) || button.getAttribute?.('aria-label') || button.getAttribute?.('title') || button.tagName.toLowerCase())
      .slice(0, 25);

    await log(`업로드 진단: file input ${inputs.length}개`);
    inputs.forEach((input, index) => {
      log(`파일${index + 1}: accept="${input.accept || ''}" multiple=${Boolean(input.multiple)}`);
    });
    buttons.forEach((text, index) => {
      log(`버튼후보${index + 1}: "${String(text).slice(0, 60)}"`);
    });
  }

  async function findPromptInput(customSelector) {
    if (isUsableInput(cachedInput) && !isBadPromptInput(cachedInput)) return cachedInput;

    const custom = queryVisible(customSelector);
    if (custom && isInputLike(custom) && !isBadPromptInput(custom)) return editorRoot(custom);

    const composer = findComposerPromptInput();
    if (composer) return composer;

    const nearButton = findInputNearGenerateButton();
    if (nearButton) return nearButton;

    const all = deepQueryAll(INPUT_SELECTOR)
      .filter(isUsableInput)
      .filter((input) => !isBadPromptInput(input))
      .map((input) => ({ input, score: scorePromptInput(input) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score);

    return all[0] ? editorRoot(all[0].input) : null;
  }

  function findComposerPromptInput() {
    const inputs = deepQueryAll(INPUT_SELECTOR)
      .filter(isUsableInput)
      .filter((input) => !isBadPromptInput(input))
      .map((input) => ({ input, score: scorePromptInput(input) }))
      .filter((entry) => entry.score >= 120)
      .sort((a, b) => b.score - a.score);

    return inputs[0] ? editorRoot(inputs[0].input) : null;
  }

  function scorePromptInput(input) {
    const root = editorRoot(input);
    const rect = root.getBoundingClientRect();
    const label = inputLabel(root);
    const context = nearbyText(root).toLowerCase();
    let score = 0;

    if (/무엇을 만들고 싶으신가요|what.*make|prompt|프롬프트/.test(label + ' ' + context)) score += 180;
    if (/에이전트|nano banana|생성 시|ingredient|인그리디언트/.test(context)) score += 120;
    if (rect.top > window.innerHeight * 0.45) score += 90;
    if (rect.width >= 350 && rect.height >= 36) score += 40;
    if (rect.bottom > window.innerHeight - 260) score += 50;

    return score;
  }

  function describePromptTarget(input) {
    const root = editorRoot(input);
    const rect = root.getBoundingClientRect();
    const label = inputLabel(root) || nearbyText(root).slice(0, 90) || root.tagName.toLowerCase();
    return `${root.tagName.toLowerCase()} ${Math.round(rect.left)},${Math.round(rect.top)} ${Math.round(rect.width)}x${Math.round(rect.height)} "${label.slice(0, 90)}"`;
  }

  function isBadPromptInput(input) {
    const root = editorRoot(input);
    const rect = root.getBoundingClientRect();
    const label = inputLabel(root);
    const context = nearbyText(root).toLowerCase();

    if (/search|검색|필터|filter/.test(label + ' ' + context)) return true;
    if (rect.top < window.innerHeight * 0.22 && rect.width > 260) return true;
    return false;
  }

  function inputLabel(input) {
    return [
      input.getAttribute?.('aria-label'),
      input.getAttribute?.('placeholder'),
      input.getAttribute?.('title'),
      input.textContent,
      input.innerText
    ].filter(Boolean).join(' ').replace(/\s+/g, ' ').trim().toLowerCase();
  }

  function nearbyText(element) {
    let box = element;
    for (let depth = 0; depth < 4; depth++) {
      if (!box || box === document.body) break;
      const text = compactText(box);
      if (text.length > 0) return text.slice(0, 500);
      box = box.parentElement;
    }
    return '';
  }

  function findInputNearGenerateButton() {
    const buttons = deepQueryAll('button, [role="button"]')
      .filter(isVisible)
      .filter((button) => /만들기|생성|create|generate|arrow_forward|send/i.test(compactText(button)));

    for (const button of buttons) {
      let box = button.parentElement;
      for (let depth = 0; depth < 10; depth++) {
        if (!box || box === document.body) break;
        const inputs = Array.from(box.querySelectorAll(INPUT_SELECTOR))
          .filter(isUsableInput)
          .filter((input) => !isBadPromptInput(input));
        if (inputs.length > 0) return editorRoot(inputs.sort((a, b) => area(b) - area(a))[0]);
        box = box.parentElement;
      }
    }

    return null;
  }

  async function findGenerateButton(customSelector, input) {
    if (isUsableButton(cachedButton)) return cachedButton;

    const custom = queryVisible(customSelector);
    if (custom && isUsableButton(custom)) return custom;

    const arrow = findPromptSendButton(input);
    if (arrow) return arrow;

    const scoped = findButtonNearInput(input);
    if (scoped) return scoped;

    const buttons = deepQueryAll('button, [role="button"]').filter(isUsableButton);
    const scored = buttons
      .map((button) => ({ button, score: scoreGenerateButton(button, input) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score);

    return scored[0]?.button || null;
  }

  function findButtonNearInput(input) {
    if (!input) return null;

    let box = input.parentElement;
    for (let depth = 0; depth < 12; depth++) {
      if (!box || box === document.body) break;

      const buttons = Array.from(box.querySelectorAll('button, [role="button"]'))
        .filter(isUsableButton)
        .map((button) => ({ button, score: scoreGenerateButton(button, input) + Math.max(0, 12 - depth) }))
        .filter((entry) => entry.score > 0)
        .sort((a, b) => b.score - a.score);

      if (buttons[0]) return buttons[0].button;
      box = box.parentElement;
    }

    return null;
  }

  function findPromptSendButton(input) {
    if (!input) return null;

    const inputRect = input.getBoundingClientRect();
    const composerBox = findComposerBox(input);
    const scopedButtons = composerBox
      ? deepQueryAll('button, [role="button"]', composerBox)
      : [];

    const scoped = scopedButtons
      .filter(isUsableButton)
      .filter((button) => !isBadGenerateButton(button))
      .map((button) => ({ button, score: scorePromptSendButton(button, inputRect, composerBox) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score);

    if (scoped[0]) return scoped[0].button;

    const buttons = deepQueryAll('button, [role="button"]')
      .filter(isUsableButton)
      .filter((button) => !isBadGenerateButton(button))
      .map((button) => ({ button, score: scorePromptSendButton(button, inputRect, null) }))
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score);

    return buttons[0]?.button || null;
  }

  function findComposerBox(input) {
    let box = input;
    for (let depth = 0; depth < 8; depth++) {
      if (!box || box === document.body) break;

      const rect = box.getBoundingClientRect();
      const context = compactText(box).toLowerCase();
      const hasButton = box.querySelector?.('button, [role="button"]');
      const looksLikeComposer = /무엇을 만들고 싶으신가요|에이전트|nano banana|생성 시|prompt/.test(context);
      const isBottomPanel = rect.top > window.innerHeight * 0.45 && rect.width >= 320 && rect.height >= 70;

      if (hasButton && (looksLikeComposer || isBottomPanel)) return box;
      box = box.parentElement;
    }

    return null;
  }

  function scorePromptSendButton(button, inputRect, composerBox) {
    const label = buttonLabel(button);
    const rect = button.getBoundingClientRect();
    let score = 0;

    const composerRect = composerBox?.getBoundingClientRect?.();
    if (composerRect) {
      const insideComposer =
        rect.left >= composerRect.left - 8 &&
        rect.right <= composerRect.right + 8 &&
        rect.top >= composerRect.top - 8 &&
        rect.bottom <= composerRect.bottom + 8;
      if (insideComposer) score += 180;
      else score -= 400;

      const nearComposerRight = rect.left >= composerRect.left + composerRect.width * 0.68;
      const nearComposerBottom = rect.top >= composerRect.top + composerRect.height * 0.45;
      if (nearComposerRight && nearComposerBottom) score += 140;
    }

    // Flow의 실제 생성 버튼은 프롬프트 박스 오른쪽 아래의 작은 화살표 버튼이다.
    const nearRight = rect.left >= inputRect.left + inputRect.width * 0.55 && rect.left <= inputRect.right + 130;
    const nearBottom = rect.top >= inputRect.top + inputRect.height * 0.35 && rect.top <= inputRect.bottom + 120;
    if (nearRight && nearBottom) score += 120;

    if (/arrow_forward|send|submit|north_east|chevron_right|→|➜/.test(label)) score += 100;
    if (/생성|만들기|generate|create/.test(label)) score += 80;
    if (rect.width >= 34 && rect.width <= 90 && rect.height >= 34 && rect.height <= 90) score += 35;
    if (rect.width < 24 || rect.height < 24) score -= 80;
    // 텍스트 없는 아이콘 버튼이 실제 생성 버튼 — 텍스트 있으면 페널티
    const buttonText = compactText(button);
    if (buttonText.length === 0) score += 60;
    else if (buttonText.length > 10) score -= 80;

    return score;
  }

  function scoreGenerateButton(button, input) {
    if (isBadGenerateButton(button)) return -999;

    const text = buttonLabel(button);
    let score = 0;

    if (/arrow_forward|send|submit|→|➜/.test(text)) score += 100;
    if (/만들기|생성|create|generate/.test(text)) score += 80;
    if (/add|plus|upload|이미지|미디어|ingredient|인그리디언트/.test(text)) score -= 120;

    const rect = button.getBoundingClientRect();
    if (rect.width < 24 || rect.height < 20) score -= 30;

    if (input) {
      const inputRect = input.getBoundingClientRect();
      const distance = Math.abs(rect.left - inputRect.right) + Math.abs(rect.top - inputRect.top);
      if (distance < 500) score += 20;
    }

    return score;
  }

  function isBadGenerateButton(button) {
    const label = buttonLabel(button);
    if (/search|검색|닫기|close|arrow_back|back|menu|more_vert|more_horiz|더 생성하기|옵션|option|overflow|설정|settings|help|도움말|필터|filter|grid|library|라이브러리/.test(label)) return true;
    // suggestion 칩, 이미지 카드 등 긴 텍스트 버튼은 생성 버튼 아님
    const text = compactText(button);
    if (text.length > 25) return true;
    return false;
  }

  function buttonLabel(button) {
    return `${compactText(button)} ${button.getAttribute?.('aria-label') || ''} ${button.getAttribute?.('title') || ''}`.toLowerCase();
  }

  async function setInputValue(input, value) {
    const target = editorRoot(input);
    target.focus();
    await sleep(150);

    if (target.tagName === 'TEXTAREA' || target.tagName === 'INPUT') {
      const proto = target.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
      const setter = Object.getOwnPropertyDescriptor(proto, 'value')?.set;
      if (!setter) return false;

      setter.call(target, '');
      target.dispatchEvent(new Event('input', { bubbles: true }));
      setter.call(target, value);
      target.dispatchEvent(new InputEvent('input', { bubbles: true, data: value, inputType: 'insertText' }));
      target.dispatchEvent(new Event('change', { bubbles: true }));
      return String(target.value || '').includes(value.slice(0, 12));
    }

    if (target.isContentEditable || target.getAttribute('role') === 'textbox') {
      // 기존 내용 전체 선택 후 CDP InsertText로 교체 — React가 실제 키보드 입력처럼 인식
      selectAll(target);
      await sleep(60);

      const response = await chrome.runtime.sendMessage({ type: 'CDP_INSERT_TEXT', text: value });
      await sleep(150);

      if (!response?.ok) {
        // CDP 실패 시 execCommand 폴백
        document.execCommand('delete', false, null);
        await sleep(60);
        document.execCommand('insertText', false, value);
        target.dispatchEvent(new InputEvent('input', { bubbles: true, data: value, inputType: 'insertText' }));
        await sleep(120);
      }

      const actual = String(target.textContent || target.innerText || '');
      return actual.includes(value.slice(0, 12));
    }

    return false;
  }


  // v5.6.3: 절대 단일 클릭. Flow는 생성 후에도 입력창을 유지하므로
  // 입력창 초기화를 성공 기준으로 사용하지 않습니다. CDP 전송 성공만 확인합니다.
  async function clickGenerateVerified(button, input, prompt) {
    const fingerprint = String(prompt || '').trim().slice(0, 200);

    // 같은 프롬프트가 짧은 시간 안에 다시 제출되는 것을 저장소 수준에서 차단합니다.
    const { flowBulkSubmitLock } = await chrome.storage.local.get('flowBulkSubmitLock');
    if (flowBulkSubmitLock?.fingerprint === fingerprint && Date.now() - flowBulkSubmitLock.at < 30000) {
      await log('중복 제출 차단: 같은 프롬프트가 30초 안에 다시 클릭되려 했습니다.', 'error');
      return false;
    }
    await chrome.storage.local.set({ flowBulkSubmitLock: { fingerprint, at: Date.now() } });

    button.scrollIntoView({ behavior: 'instant', block: 'center', inline: 'center' });
    await sleep(250);
    const rect = button.getBoundingClientRect();
    const x = Math.round(rect.left + rect.width / 2);
    const y = Math.round(rect.top + rect.height / 2);

    const response = await chrome.runtime.sendMessage({ type: 'CDP_CLICK', x, y });
    if (!response?.ok) {
      await log(`단일 클릭 전송 실패: ${response?.error || '알 수 없는 오류'} — 안전을 위해 재클릭하지 않음`, 'error');
      return false;
    }

    await log('생성 클릭 1회 전송 확인 — 입력창 유지 여부와 관계없이 생성 대기로 이동', 'success');
    return true;
  }

  async function resetComposerAfterSubmit(input) {
    await sleep(1800); // Flow가 제출 내용을 먼저 확정할 시간을 줍니다.

    const target = editorRoot(input);
    if (target && target.isConnected && isVisible(target)) {
      try {
        target.focus();
        selectAll(target);
        await sleep(80);
        const response = await chrome.runtime.sendMessage({ type: 'CDP_KEY', key: 'Backspace', keyCode: 8 });
        if (!response?.ok) throw new Error(response?.error || 'Backspace 전송 실패');
        await sleep(250);

        const remaining = String(target.value ?? target.textContent ?? '').trim();
        await log(remaining ? '이전 프롬프트가 일부 남음 — 다음 입력 때 전체 교체' : '이전 프롬프트 비우기 완료', remaining ? 'warn' : 'success');
      } catch (err) {
        await log(`입력창 비우기 보조 실패: ${err.message} — 다음 입력 때 전체 교체`, 'warn');
      }
    }

    // DOM 캐시 초기화 (다음 컷에서 신선한 DOM 탐색)
    cachedInput = null;
    cachedButton = null;
    await sleep(350);
  }

  async function clickOnce(button) {
    button.scrollIntoView({ behavior: 'instant', block: 'center', inline: 'center' });
    await sleep(250);

    const rect = button.getBoundingClientRect();
    const x = Math.round(rect.left + rect.width / 2);
    const y = Math.round(rect.top + rect.height / 2);

    try {
      const response = await chrome.runtime.sendMessage({ type: 'CDP_CLICK', x, y });
      if (response?.ok) return true;
      console.warn('[FlowBulk] CDP 클릭 실패, DOM 클릭 폴백:', response?.error);
    } catch (err) {
      console.warn('[FlowBulk] CDP 메시지 실패, DOM 클릭 폴백:', err);
    }

    try {
      button.focus?.();
      button.click();
      return true;
    } catch {
      return false;
    }
  }

  async function waitForContinue() {
    await chrome.storage.local.set({ flowBulkWaiting: true, flowBulkContinue: false });

    while (!stopped) {
      const { flowBulkContinue } = await chrome.storage.local.get('flowBulkContinue');
      if (flowBulkContinue) {
        await chrome.storage.local.set({ flowBulkWaiting: false, flowBulkContinue: false });
        return true;
      }
      await sleep(500);
    }

    await chrome.storage.local.set({ flowBulkWaiting: false });
    return false;
  }

  async function diagnose() {
    const inputs = deepQueryAll(INPUT_SELECTOR).filter(isUsableInput).slice(0, 12);
    const buttons = deepQueryAll('button, [role="button"]').filter(isVisible).slice(0, 20);
    const fileInputs = deepQueryAll('input[type="file"]').slice(0, 8);

    await log(`진단: 입력 후보 ${inputs.length}개, 버튼 후보 ${buttons.length}개, 파일 후보 ${fileInputs.length}개`);
    inputs.forEach((input, index) => {
      const score = scorePromptInput(input);
      const blocked = isBadPromptInput(input) ? '차단' : '허용';
      log(`입력${index + 1}: ${blocked} score=${score} ${describePromptTarget(input)}`);
    });
    buttons.forEach((button, index) => {
      log(`버튼${index + 1}: "${compactText(button).slice(0, 50)}"`);
    });
    fileInputs.forEach((input, index) => {
      log(`파일${index + 1}: accept="${input.accept || ''}" multiple=${Boolean(input.multiple)}`);
    });

    return { ok: true, inputs: inputs.length, buttons: buttons.length, fileInputs: fileInputs.length };
  }

  function deepQueryAll(selector, root = document) {
    const results = [];

    function walk(node) {
      try {
        results.push(...Array.from(node.querySelectorAll(selector)));
        Array.from(node.querySelectorAll('*')).forEach((child) => {
          if (child.shadowRoot) walk(child.shadowRoot);
        });
      } catch {
        // 접근 불가 shadow root는 건너뜁니다.
      }
    }

    walk(root);
    return [...new Set(results)];
  }

  function queryVisible(selector) {
    if (!selector) return null;
    try {
      const found = document.querySelector(selector);
      return found && isVisible(found) ? found : null;
    } catch {
      return null;
    }
  }

  function isInputLike(element) {
    if (!element || element.nodeType !== 1) return false;
    return element.matches?.(INPUT_SELECTOR) || element.isContentEditable || element.getAttribute('role') === 'textbox';
  }

  function isUsableInput(element) {
    return isInputLike(element) && isVisible(element) && !element.disabled;
  }

  function isUsableButton(element) {
    if (!element || !isVisible(element)) return false;
    if (element.disabled || element.getAttribute('aria-disabled') === 'true') return false;
    return element.matches?.('button, [role="button"]');
  }

  function isVisible(element) {
    if (!element || !element.getBoundingClientRect) return false;
    const rect = element.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) return false;
    const style = getComputedStyle(element);
    return style.display !== 'none' && style.visibility !== 'hidden' && Number(style.opacity) !== 0;
  }

  function editorRoot(element) {
    if (!element) return element;
    if (element.tagName === 'TEXTAREA' || element.tagName === 'INPUT') return element;

    let root = element;
    while (root.parentElement && root.parentElement.isContentEditable) {
      root = root.parentElement;
    }
    return root;
  }

  function selectAll(element) {
    const range = document.createRange();
    range.selectNodeContents(element);
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
  }

  function compactText(element) {
    return String(element?.textContent || element?.getAttribute?.('aria-label') || element?.getAttribute?.('title') || '')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function area(element) {
    const rect = element.getBoundingClientRect();
    return rect.width * rect.height;
  }

  function randomInt(min, max) {
    const safeMin = Math.max(1, Number(min) || 1);
    const safeMax = Math.max(safeMin, Number(max) || safeMin);
    return Math.floor(Math.random() * (safeMax - safeMin + 1)) + safeMin;
  }

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  async function sleepSeconds(seconds) {
    for (let left = seconds; left > 0; left--) {
      if (stopped) return;
      await sleep(1000);
    }
  }

  function makeProgress(status, total = 0) {
    return { status, current: 0, total, log: [] };
  }

  async function log(message, level = 'info') {
    progress.log.push({
      at: new Date().toLocaleTimeString(),
      level,
      message
    });
    progress.log = progress.log.slice(-120);
    await saveProgress();
    console.log(`[FlowBulk:${level}] ${message}`);
  }

  async function saveProgress() {
    await chrome.storage.local.set({ flowBulkProgress: progress });
  }
})();
