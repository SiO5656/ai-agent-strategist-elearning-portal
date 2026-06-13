# [[Unit24]] QA report

- status: `completed_drive_verified`
- title: AIプロジェクトの効果検証と進行管理
- source pages: p.211〜216（p.217 は [[Unit25]] 開始のため除外）
- MP4: `video_study.mp4`
- Drive: https://drive.google.com/file/d/1izFT1MInvvm-rK5z-5LPF0pTn38g27Lq/view?usp=drivesdk
- file ID: `1izFT1MInvvm-rK5z-5LPF0pTn38g27Lq`

## 制作物

- lesson: `lesson.md`
- script: `script.md`
- quiz: `quiz.md`
- exam cards: `exam_cards.md`
- storyboard: `storyboard.json`
- GPT Image 2 prompts: `prompts_gptimage2/scene01.txt`〜`scene08.txt`
- accepted slides: `assets_gptimage2/scene01.png`〜`scene08.png`
- audio: `audio/scene01.mp3`〜`scene08.mp3`
- Remotion: `remotion_video_study_20260609_112650/`

## 画像QA

- provider: [[GPT Image 2]] via [[Codex CLI]] `$imagegen`
- accepted slide count: 8
- dimensions: 全8枚 `1086x1448` / ratio `0.75`（3:4 portrait）
- 初回2:3混入: scene01〜04/08で検知し、3:4へ再生成済み
- raw manifest: `qa/raw_slide_manifest.json`
- raw contact sheet: `qa/raw_slide_contact_sheet.jpg`
- vision QA: 白ベース、図解中心、安全マージンあり。不要なページ番号/Unit番号/透かし/メール表記なし。

## Remotion / MP4 QA

- `npm install`: pass
- `npm run lint`: pass
- `npm run still`: pass
- `npm run render`: pass
- ffprobe: `remotion_video_study_20260609_112650/qa/final_spacing_balance_ffprobe.json`
- blackdetect: `remotion_video_study_20260609_112650/qa/final_spacing_balance_blackdetect.log`
- volumedetect: `remotion_video_study_20260609_112650/qa/final_spacing_balance_volumedetect.log`
- media summary: `remotion_video_study_20260609_112650/qa/final_spacing_balance_qa_media_summary.json`

### ffprobe summary

- resolution: `1080x1920`
- video codec: `h264`
- audio codec: `aac`
- duration: `230.570667s`
- size: `18237498` bytes
- bit rate: `632777`
- audio mean/max: `-17.0 dB` / `-3.5 dB`

### Visual QA

- final midpoint contact sheet: `remotion_video_study_20260609_112650/qa/final_spacing_balance_midpoint_contact_sheet.jpg`
- lower-card crop contact sheet: `remotion_video_study_20260609_112650/qa/final_spacing_balance_lower_card_crop_sheet.jpg`
- midpoint visual result: 全8シーンが順に存在。黒/空白フレーム、古いUnit混入、見切れ、下端フッター、内部テンプレート名、制作ラベルは見当たらない。
- lower-card visual result: 全8シーンで「おさえるべきポイント」と用語メモがカード内に収まり、右端/下端のテキスト切れなし。下部カード高さを `350px` → `370px` に拡張し、「おさえるべきポイント」文字上余白 `33px`、用語メモカード下〜外枠下余白 `31〜32px` に調整済み。
- progress-bar visual result: 全8シーンで控えめな全体進捗バーを確認。`bottom:72px` / `height:11px` で、下部カードとの重なりなし、画面下端の見切れなし。

## 進捗バーQA

- `src/StudyVideo.tsx` に `progressFooter`: `True`
- `src/StudyVideo.tsx` に `progressFill`: `True`
- `src/style.css` に `.progressFooter`: `True`
- `src/style.css` に `.progressFill`: `True`
- CSS: `bottom:72px` / `height:11px` 確認済み

## Privacy scan

- unapproved actual email count: `0`
- notes: ポリシー文としての「透かし/メール/購入者」言及は許容。実値混入は検知なし。

## Drive verification

- update response: `drive_update_response_spacing_balance.json`
- metadata: `drive_metadata_verified_spacing_balance.json`
- permissions: `drive_permissions_verified_spacing_balance.json`
- verification summary: `drive_verification_summary_spacing_balance.json`
- mimeType: `video/mp4`
- local size: `18237498`
- Drive size: `18237498`
- size match: `True`
- owner: `shiomaruclaw@gmail.com`
- public sharing: `False`
- parent: `Exports/videos/2026` (`1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`)

関連: [[Unit24]] / [[Remotion]] / [[GPT Image 2]] / [[Google Drive]] / [[QA]]
