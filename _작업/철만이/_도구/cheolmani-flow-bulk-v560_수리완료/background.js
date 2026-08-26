// background.js
// Chrome 확장 서비스 워커입니다. Flow 페이지에 "진짜 클릭"을 보내기 위해
// chrome.debugger CDP 입력 이벤트만 담당합니다.

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => event.waitUntil(clients.claim()));

async function setupSidePanel() {
  if (!chrome.sidePanel) return;
  await chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true });
}

setupSidePanel().catch((err) => console.error('[FlowBulk] sidePanel setup failed:', err));
chrome.runtime.onInstalled.addListener(() => {
  setupSidePanel().catch((err) => console.error('[FlowBulk] sidePanel install setup failed:', err));
});

chrome.action.onClicked.addListener(async (tab) => {
  if (!chrome.sidePanel || !tab.windowId) return;
  try {
    await chrome.sidePanel.open({ windowId: tab.windowId });
  } catch (err) {
    console.error('[FlowBulk] sidePanel open failed:', err);
  }
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'CDP_CLICK') {
    const tabId = sender.tab?.id || message.tabId;
    if (!tabId) {
      sendResponse({ ok: false, error: 'tabId 없음' });
      return false;
    }

    cdpClick(tabId, message.x, message.y)
      .then(() => sendResponse({ ok: true }))
      .catch((err) => sendResponse({ ok: false, error: err.message }));
    return true;
  }

  if (message.type === 'CDP_KEY') {
    const tabId = sender.tab?.id || message.tabId;
    if (!tabId) {
      sendResponse({ ok: false, error: 'tabId 없음' });
      return false;
    }

    cdpKey(tabId, message.key, message.keyCode)
      .then(() => sendResponse({ ok: true }))
      .catch((err) => sendResponse({ ok: false, error: err.message }));
    return true;
  }

  if (message.type === 'CDP_INSERT_TEXT') {
    const tabId = sender.tab?.id || message.tabId;
    if (!tabId) {
      sendResponse({ ok: false, error: 'tabId 없음' });
      return false;
    }

    cdpInsertText(tabId, message.text)
      .then(() => sendResponse({ ok: true }))
      .catch((err) => sendResponse({ ok: false, error: err.message }));
    return true;
  }

  if (message.type === 'PING_BACKGROUND') {
    sendResponse({ ok: true });
    return false;
  }
});

const attachedTabs = new Set();

chrome.debugger.onDetach.addListener((source) => {
  if (source.tabId) attachedTabs.delete(source.tabId);
});

async function ensureDebuggerAttached(tabId) {
  const target = { tabId };
  if (!attachedTabs.has(tabId)) {
    try {
      await chrome.debugger.attach(target, '1.3');
      attachedTabs.add(tabId);
    } catch (err) {
      if (String(err.message || '').includes('already attached')) {
        attachedTabs.add(tabId);
      } else {
        throw new Error(`debugger attach 실패: ${err.message}`);
      }
    }
  }
  return target;
}

async function withDebugger(tabId, task) {
  const target = await ensureDebuggerAttached(tabId);
  try {
    return await task(target);
  } catch (err) {
    if (String(err.message || '').includes('detached') || String(err.message || '').includes('not attached')) {
      attachedTabs.delete(tabId);
      const reTarget = await ensureDebuggerAttached(tabId);
      return await task(reTarget);
    }
    throw err;
  }
}

async function cdpClick(tabId, x, y) {
  if (!Number.isFinite(x) || !Number.isFinite(y)) {
    throw new Error('클릭 좌표가 올바르지 않음');
  }

  await withDebugger(tabId, async (target) => {
    await chrome.debugger.sendCommand(target, 'Input.dispatchMouseEvent', {
      type: 'mouseMoved',
      x,
      y,
      button: 'none',
      buttons: 0
    });
    // Flow는 터치와 마우스를 각각 클릭으로 처리할 수 있습니다.
    // 반드시 마우스 이벤트 한 종류만 한 번 보냅니다.
    await chrome.debugger.sendCommand(target, 'Input.dispatchMouseEvent', {
      type: 'mousePressed',
      x,
      y,
      button: 'left',
      buttons: 1,
      clickCount: 1,
      pointerType: 'mouse'
    });
    await sleep(40);
    await chrome.debugger.sendCommand(target, 'Input.dispatchMouseEvent', {
      type: 'mouseReleased',
      x,
      y,
      button: 'left',
      buttons: 0,
      clickCount: 1,
      pointerType: 'mouse'
    });
  });
}

async function cdpInsertText(tabId, text) {
  await withDebugger(tabId, async (target) => {
    await chrome.debugger.sendCommand(target, 'Input.insertText', { text });
  });
}

async function cdpKey(tabId, key, keyCode) {
  await withDebugger(tabId, async (target) => {
    await chrome.debugger.sendCommand(target, 'Input.dispatchKeyEvent', {
      type: 'keyDown',
      key,
      windowsVirtualKeyCode: keyCode,
      nativeVirtualKeyCode: keyCode
    });
    await sleep(40);
    await chrome.debugger.sendCommand(target, 'Input.dispatchKeyEvent', {
      type: 'keyUp',
      key,
      windowsVirtualKeyCode: keyCode,
      nativeVirtualKeyCode: keyCode
    });
  });
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
