# [[Unit26]] QA report - 自動化レベルの進化論

## 結論
- Status: `completed_drive_verified`
- 動画: `video_study.mp4`
- Drive: https://drive.google.com/file/d/1aR3mF3SLo8N2BJ1_GfficRNM7wpw16gG/view?usp=drivesdk
- File ID: `1aR3mF3SLo8N2BJ1_GfficRNM7wpw16gG`

## 実行証跡
- TTS: [[Hermes]] `text_to_speech` / provider `elevenlabs` で `audio/scene01.mp3`〜`audio/scene10.mp3` を生成。
- Remotion: `npm run lint` / `npm run still` / `npm run render` 成功。
- local MP4: `units/unit26_automation_levels/video_study.mp4`
- render MP4: `units/unit26_automation_levels/remotion_video_study_20260611_000000/out/video_study.mp4`

## メディア検証
- ffprobe: `1080x1920`, `h264/aac`, duration `121.322667s`, size `13530507` bytes, bit_rate `892199`
- blackdetect: exit `0`, black_startなし
- volumedetect: mean `-17.1 dB`, max `-3.5 dB`
- raw slide manifest: `qa/raw_slide_manifest.json` / all_ratio_3_4 `true`

## 目視QA
- raw slide contact sheet: `qa/raw_slide_contact_sheet.jpg`
  - 10枚すべて表示。3:4 portrait、白ベース、図解中心。
  - 明らかな文字化け、ページ番号、フッター、個人情報なし。
- final midpoint contact sheet: `remotion_video_study_20260611_000000/qa/midpoint_contact_sheet.jpg`
  - 10シーン順序表示、タイトル右上Step、GPT Image 2スライド、下部カード、進捗バーを確認。
  - 見切れ・重なりの重大問題なし。
- lower card crop: `remotion_video_study_20260611_000000/qa/lower_card_crop_contact_sheet.jpg`
  - `おさえるべきポイント`表示、本文・用語メモの見切れなし。
- progress crop: `remotion_video_study_20260611_000000/qa/progress_bar_crop_contact_sheet.jpg`
  - 進捗バー視認、下端フッター/制作ラベルなし。
- code check: `src/StudyVideo.tsx` と `src/style.css` に `progressFooter` / `progressFill` 残存を確認。

## Drive検証
- Drive metadata readback: `mimeType=video/mp4`, size `13530507`
- Owner: `shiomaruclaw@gmail.com`
- Permissions: owner only / public共有なし

関連: [[Unit26]] / [[Google Drive]] / [[Remotion]] / [[GPT Image 2]]
