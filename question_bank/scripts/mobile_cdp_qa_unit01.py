#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import subprocess
import time
import urllib.request
from pathlib import Path

import websocket

BASE = Path('/Users/clawuser/SiO-Brain/projects/ai-agent-strategist-course/elearning_v2')
HTML = BASE / 'question_bank/unit01_course_orientation/index.html'
PNG = BASE / 'question_bank/unit01_course_orientation/mobile_cdp_390x844.png'
PORT = 9229
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
URL = HTML.resolve().as_uri()

proc = subprocess.Popen([
    CHROME,
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    f'--remote-debugging-port={PORT}',
    '--remote-allow-origins=*',
    URL,
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


try:
    endpoint = None
    for _ in range(60):
        try:
            data = json.loads(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json', timeout=1).read())
            page = next((item for item in data if item.get('type') == 'page' and item.get('webSocketDebuggerUrl')), data[0])
            endpoint = page['webSocketDebuggerUrl']
            break
        except Exception:
            time.sleep(0.1)
    if not endpoint:
        raise RuntimeError('CDP endpoint not ready')

    ws = websocket.create_connection(endpoint, timeout=5)
    counter = 0

    def call(method: str, params: dict | None = None):
        nonlocal_counter[0] += 1
        msg_id = nonlocal_counter[0]
        ws.send(json.dumps({'id': msg_id, 'method': method, 'params': params or {}}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get('id') == msg_id:
                if 'error' in msg:
                    raise RuntimeError(f'{method}: {msg["error"]}')
                return msg.get('result')

    nonlocal_counter = [0]
    call('Page.enable')
    call('Runtime.enable')
    call('Emulation.setDeviceMetricsOverride', {
        'width': 390,
        'height': 844,
        'deviceScaleFactor': 2,
        'mobile': True,
        'screenWidth': 390,
        'screenHeight': 844,
    })
    call('Emulation.setTouchEmulationEnabled', {'enabled': True})
    call('Page.reload', {'ignoreCache': True})
    for _ in range(120):
        res = call('Runtime.evaluate', {
            'expression': "document.readyState === 'complete' && !!document.querySelector('h1') && !!document.getElementById('questionText')",
            'returnByValue': True,
        })
        if res['result'].get('value') is True:
            break
        time.sleep(0.1)
    else:
        raise RuntimeError('page did not finish rendering quiz UI')
    time.sleep(0.4)
    eval_result = call('Runtime.evaluate', {
        'expression': '''(() => ({
          clientWidth: document.documentElement.clientWidth,
          scrollWidth: document.documentElement.scrollWidth,
          bodyScrollWidth: document.body.scrollWidth,
          miniCount: document.querySelectorAll('.mini').length,
          firstQuestion: document.getElementById('questionText') ? document.getElementById('questionText').textContent : null,
          buttons: Array.from(document.querySelectorAll('button')).slice(0,5).map(b => ({text:b.textContent.trim(), h: Math.round(b.getBoundingClientRect().height), w: Math.round(b.getBoundingClientRect().width)})),
          titleRect: (() => { const r = document.querySelector('h1').getBoundingClientRect(); return {x:Math.round(r.x), width:Math.round(r.width), right:Math.round(r.right)} })()
        }))()''',
        'returnByValue': True,
    })
    if 'exceptionDetails' in eval_result or 'value' not in eval_result.get('result', {}):
        raise RuntimeError(f'Runtime.evaluate failed or returned no value: {json.dumps(eval_result, ensure_ascii=False)}')
    metrics = eval_result['result']['value']
    shot = call('Page.captureScreenshot', {'format': 'png', 'captureBeyondViewport': False})
    PNG.write_bytes(base64.b64decode(shot['data']))
    print(json.dumps({'metrics': metrics, 'screenshot': str(PNG), 'screenshot_size': PNG.stat().st_size}, ensure_ascii=False, indent=2))
finally:
    proc.terminate()
    try:
        proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        proc.kill()
