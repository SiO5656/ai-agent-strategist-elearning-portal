# [[Unit28]] QA report - 実行・連携パターンと理解度チェック

## 結論
- Status: `completed_drive_verified`
- 動画: `video_study.mp4`
- Drive: https://drive.google.com/file/d/12Zc7CfkttHY2RY9bRvWUfBHReY3dfGEv/view?usp=drivesdk
- File ID: `12Zc7CfkttHY2RY9bRvWUfBHReY3dfGEv`

## 実行証跡
- GPT Image 2 slides: `assets_gptimage2/scene01.png`〜`assets_gptimage2/scene10.png`
- raw slide QA: `qa/raw_slide_contact_sheet.jpg`
- TTS: `audio/scene01.mp3`〜`audio/scene10.mp3`
- Remotion: `npm install` / `npm run lint` / `npm run still` / `npm run render` 成功
- local MP4: `units/unit28_workflow_execution_patterns/video_study.mp4`
- render MP4: `units/unit28_workflow_execution_patterns/remotion_video_study_20260611_000000/out/video_study.mp4`

## メディア検証
- ffprobe: `1080x1920`, `h264/aac`, duration `114.560000s`, size `11901421` bytes, bit_rate `831104`
- blackdetect: `black_start` なし
- volumedetect: mean `-17.1 dB`, max `-3.6 dB`

## 目視QA
- raw slide contact sheet: `qa/raw_slide_contact_sheet.jpg`
  - 10枚すべて表示。Unit28内容として整合。重大な文字崩れ・見切れ・余白過多・個人情報/透かし/フッター/ページ番号なし。
- final midpoint contact sheet: `remotion_video_study_20260611_000000/qa/midpoint_contact_sheet.jpg`
  - 10シーン順序表示、タイトル右上Step、GPT Image 2スライド、下部カード、進捗バーを確認。
  - 重大な見切れ・重なり・黒画面・下端フッター残存なし。
- lower card crop: `remotion_video_study_20260611_000000/qa/lower_card_crop_contact_sheet.jpg`
  - `おさえるべきポイント`表示、字幕/箇条書き/用語メモの重大な見切れ・重なりなし。
- progress crop: `remotion_video_study_20260611_000000/qa/progress_bar_crop_contact_sheet.jpg`
  - 控えめな進捗バーあり。制作フッターや不要な文字なし。

## Drive検証
- Drive metadata readback: `mimeType=video/mp4`, size `11901421`
- Local size: `11901421`
- Size match: `true`
- Owner: `shiomaruclaw@gmail.com`
- Permissions: owner only / public共有なし

関連: [[Unit28]] / [[Google Drive]] / [[Remotion]] / [[GPT Image 2]]
