# Unit06 QAレポート

## 対象

- Unit: [[Unit06]] AIエージェントの起動タイプを判別する
- Unit dir: `units/unit06_agent_trigger_types/`
- Manifest範囲: p.35〜p.41

## ページ範囲連続性

- p.35〜p.41は連続。
- Section3「AIエージェントの起動タイプ」を、指示型・定時型・条件型とシナリオ判定の観点で再構成した。

## 最終状態

- 状態: `completed`
- 教材: `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` / prompt作成済み
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene08.png` 生成・採用済み
- 音声: `audio/scene01.mp3`〜`audio/scene08.mp3` 生成済み
- 正式動画: `video_study.mp4` 作成済み
- [[Google Drive]]: アップロード・metadata・permissions確認済み

## 画像QA

- 採用画像:
  - `assets_gptimage2/scene01.png`
  - `assets_gptimage2/scene02.png`
  - `assets_gptimage2/scene03.png`
  - `assets_gptimage2/scene04.png`
  - `assets_gptimage2/scene05.png`
  - `assets_gptimage2/scene06.png`
  - `assets_gptimage2/scene07.png`
  - `assets_gptimage2/scene08.png`
- 寸法確認:
  - `scene01`: `1024x1536`
  - `scene02`: `1086x1448`
  - `scene03`: `1086x1448`
  - `scene04`: `1086x1448`
  - `scene05`: `1024x1536`
  - `scene06`: `1086x1448`
  - `scene07`: `1086x1448`
  - `scene08`: `1086x1448`
- contact sheet: `qa/unit06_gptimage2_scene_contact_sheet_v3.png`
- Vision QA: 白ベースで統一感あり、順番・可読性に大きな問題なし。見切れ、個人情報、メールアドレス、透かし、Unit番号、ページ番号、スライド番号、不要フッター、制作都合語の混入なし。採用可。

## 音声QA

- provider: [[ElevenLabs]]
- 読み統一: AI=エーアイ / CRM=シーアールエム / FAQ=エフエーキュー / ヘルプデスクAI=ヘルプデスク・エーアイ
- ffprobe duration:
  - scene01: `24.880s`
  - scene02: `21.200s`
  - scene03: `21.760s`
  - scene04: `23.920s`
  - scene05: `29.200s`
  - scene06: `27.280s`
  - scene07: `27.520s`
  - scene08: `28.400s`
  - total: `204.160s`

## 動画QA

- MP4: `video_study.mp4`
- render dir: `remotion_video_study_20260607_072208/`
- ffprobe JSON: `qa/unit06_root_video_ffprobe_summary.json`
- ffprobe要約:
  - video: `h264`, `1080x1920`, `24fps`
  - audio: `aac`
  - duration: `227.370667s`
  - size: `16837053` bytes
  - bitrate: `592408`
- midpoint contact sheet: `remotion_video_study_20260607_072208/qa/unit06_mp4_midpoints_contact_sheet.png`
- midpoint frames summary: `remotion_video_study_20260607_072208/qa/unit06_midpoint_frames_summary.json`
- blackdetect log: `remotion_video_study_20260607_072208/qa/unit06_blackdetect.log`
- blackdetect: `black_start`なし（0.5秒以上の黒画面なし）
- Vision QA: 8シーンが順番通り表示。中央スライド枠・ヘッダー・下部解説カード・用語メモ・Step表示・進捗バーに大きなズレなし。見切れ・横はみ出し・不要フッター・透かし・メール/個人情報なし。Unit番号・ページ番号・スライド番号・制作都合語なし。採用可。

## ソース・サニタイズQA

- 原文丸写しなし: 講義ノートとして再構成済み
- 個人情報透かし・メールアドレス・購入者情報: 成果物本文・画像・動画QA上で検出なし
- `TTS` / `台本ベース` / `GPT Image 2保持` / `外部カード` / `Remotion固定テンプレート` / `@` の表示混入検索: 0件

## Drive QA

- 状態: `uploaded_verified`
- File ID: `1TfIGuDfdLU6Qdj6EEiW91tRKAmj6d6kW`
- View link: https://drive.google.com/file/d/1TfIGuDfdLU6Qdj6EEiW91tRKAmj6d6kW/view?usp=drivesdk
- 保存先: `Exports/videos/2026`
- metadata: `mimeType=video/mp4`, size `16837053`, owner `shiomaruclaw@gmail.com`
- permissions: owner only `shiomaruclaw@gmail.com`
- upload response: `drive_upload_unit06_create_20260607_0728.json`
- metadata response: `drive_upload_unit06_metadata_20260607_0728.json`

## 次の処理

1. [[Unit07]]の制作へ進む。

関連: [[AIエージェント・ストラテジスト]] / [[Unit06]] / [[GPT Image 2]] / [[Remotion]] / [[Google Drive]]
