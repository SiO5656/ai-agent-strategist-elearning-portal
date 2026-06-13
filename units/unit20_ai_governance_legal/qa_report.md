# [[Unit20]] QA Report - AIガバナンスと法務：ポリシー・著作権・個人情報

## 判定
- status: `passed_drive_verified`
- completed_at: `2026-06-08T08:55:00+09:00`
- Drive link: https://drive.google.com/file/d/1cGijU6PGTJ4A6l7YBUwyvhYTWkFfETvo/view?usp=drivesdk
- Drive file ID: `1cGijU6PGTJ4A6l7YBUwyvhYTWkFfETvo`
- 共有範囲: owner only `shiomaruclaw@gmail.com`（public sharing false）

## 成果物
- MP4: `units/unit20_ai_governance_legal/video_study.mp4`
- Remotion: `units/unit20_ai_governance_legal/remotion_video_study_20260608_082801/`
- raw slide contact sheet: `units/unit20_ai_governance_legal/qa/raw_slide_contact_sheet.png`
- still: `units/unit20_ai_governance_legal/remotion_video_study_20260608_082801/qa/still.png`
- final midpoint contact sheet: `units/unit20_ai_governance_legal/remotion_video_study_20260608_082801/qa/final_midpoint_contact_sheet.png`
- ffprobe: `units/unit20_ai_governance_legal/remotion_video_study_20260608_082801/qa/ffprobe.json`
- blackdetect: `units/unit20_ai_governance_legal/remotion_video_study_20260608_082801/qa/blackdetect.log`
- volumedetect: `units/unit20_ai_governance_legal/remotion_video_study_20260608_082801/qa/volumedetect.log`

## メディア仕様
- format: `1080x1920` vertical MP4
- video codec: `h264`
- audio codec: `aac` / sample rate `48000`
- duration: `276.309333s`
- size: `21100365` bytes
- bitrate: `610920`
- scenes: `10`
- fps: `24`

## 実行QA
- `npm run lint`: 成功
- `npm run still`: 成功
- `npm run render`: 成功
- `ffprobe`: `1080x1920` / `h264` / `aac` / local size `21100365` bytes
- `blackdetect`: `black_start` なし（検出0件）
- `volumedetect`: mean `-17.4 dB`, max `-3.6 dB`
- 進捗バーコードQA: `src/StudyVideo.tsx` に `progressFooter` / `progressFill`、`src/style.css` に `.progressFooter` / `.progressFill` が存在

## 目視QA
- raw slide contact sheet: [[GPT Image 2]]完成スライド10枚を確認。白ベース図解、安全マージンあり、短い日本語ラベル中心。明らかな見切れ、メール、透かし、ページ番号、Unit番号バッジなし。
- still/final midpoint contact sheet: 10シーン順序OK。黒画面/空白なし。Step表示はタイトルカード右上のみ。下部カード内Step重複なし。下端フッター/内部テンプレート名/制作ラベルなし。
- 進捗バーQA: 各シーン下端に控えめな全体進捗バーを視認。[[Unit19]]で消えた進捗バーはUnit20では維持済み。

## Drive検証
- file ID: `1cGijU6PGTJ4A6l7YBUwyvhYTWkFfETvo`
- name: `2026-06-08_unit20_ai_governance_legal_video_study.mp4`
- mimeType: `video/mp4`
- Drive size: `21100365` bytes（ローカルMP4と一致）
- parent: `Exports/videos/2026` / `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only
- public sharing: `false`

関連: [[AIエージェント・ストラテジスト]] / [[Unit20]] / [[AIガバナンス]] / [[法務]] / [[Remotion]] / [[Google Drive]]
