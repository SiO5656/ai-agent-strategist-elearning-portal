# [[Unit19]] QA Report - RAGの仕組み：検索して渡す2フェーズを理解する

## 判定
- status: `passed_drive_verified_progress_visible_fix`
- completed_at: `2026-06-08T13:31:59+09:00`
- Drive link: https://drive.google.com/file/d/1Do1RREoWawTbj5LhWpoHBeo4mdLZKzsX/view?usp=drivesdk
- Drive file ID: `1Do1RREoWawTbj5LhWpoHBeo4mdLZKzsX`
- 共有範囲: owner only `shiomaruclaw@gmail.com`（public sharing false）

## 成果物
- MP4: `units/unit19_rag_mechanism/video_study.mp4`
- Remotion: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/`
- raw slide contact sheet: `units/unit19_rag_mechanism/qa/raw_slide_contact_sheet.png`
- still: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/qa/still.png`
- final midpoint contact sheet: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/qa/progress_visible_fix_20260608_133119/final_midpoint_progress_contact_sheet.png`
- progress crop contact sheet: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/qa/progress_visible_fix_20260608_133119/progress_bar_crop_contact_sheet.png`
- ffprobe: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/qa/progress_visible_fix_20260608_133119/ffprobe.json`
- blackdetect: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/qa/progress_visible_fix_20260608_133119/blackdetect.log`
- volumedetect: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/qa/progress_visible_fix_20260608_133119/volumedetect.log`
- Drive metadata: `units/unit19_rag_mechanism/remotion_video_study_20260608_000620/qa/progress_visible_fix_20260608_133119/drive_live_metadata_after_update.json`

## メディア仕様
- format: `1080x1920` vertical MP4
- video codec: `h264` / pixel format `yuv420p`
- audio codec: `aac` / sample rate `48000`
- duration: `290.453333s`
- size: `22279230` bytes
- md5: `7c39f49cab8db1ce0caff07a2634a09e`
- bitrate: `613640`
- scenes: `10`
- fps: `24`

## 実行QA
- `npm run lint`: 成功
- `npm run still`: 成功
- `npm run render`: 成功
- `ffprobe`: `1080x1920` / `h264` / `aac` / local size `22279230` bytes
- `blackdetect`: `black_start` なし
- `volumedetect`: mean `-17.3 dB`, max `-3.6 dB`

## 進捗バー修正QA
- 原因: 旧修正版は `bottom: 78px` / `height: 7px` で、Drive/Telegramスマホ再生UIに隠れる・見えにくい配置だった。
- 修正: `.progressFooter bottom: 150px`、`.progressTrack/.progressFill height: 11px` へ変更。
- 自動検出: 6チェックポイントすべてで青〜紫の進捗バーを検出（summary: `progress_visible_fix_summary.json`）。
- 目視QA: progress crop contact sheet 6コマすべてで進捗バーを確認。位置は下部カード下、プレイヤーUIに隠れにくい高さ。

## 目視QA
- raw slide contact sheet: [[GPT Image 2]]完成スライド10枚を確認。見切れなし、黒枠/ページ枠なし、スライド番号/Unit番号/透かし/メール/制作都合語なし。
- still: Step表示はタイトルカード右上 `Step 01/10` のみ。下部カード見出しは `おさえるべきポイント`。用語メモ可読。下端フッター/内部テンプレート名/制作ラベルなし。全体進捗バーあり。
- final midpoint/progress crop contact sheet: 10シーン順序OK。黒画面/空白/右端切れなし。各シーン下部に、スマホ操作UIで隠れにくい高さの全体進捗バーあり。

## Drive検証
- file ID: `1Do1RREoWawTbj5LhWpoHBeo4mdLZKzsX`
- name: `2026-06-08_unit19_rag_mechanism_video_study.mp4`
- mimeType: `video/mp4`
- Drive size: `22279230` bytes（ローカルMP4と一致）
- Drive md5: `7c39f49cab8db1ce0caff07a2634a09e`（ローカルMP4と一致）
- modifiedTime: `2026-06-08T04:31:59.282Z`
- parent: `Exports/videos/2026` / `1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only
- public sharing: `false`

関連: [[AIエージェント・ストラテジスト]] / [[Unit19]] / [[RAG]] / [[Remotion]] / [[Google Drive]] / [[進捗バー]]
