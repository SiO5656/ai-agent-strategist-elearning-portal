# qa_report - [[Unit17]] 知識をAI活用資産へ変える考え方

## 完了状態
- status: `completed_drive_verified`
- 完了日時: `2026-06-07T21:44:47+09:00`
- 担当profile: `default` main session recovery（[[studio]] worker停止後の継続回収）

## 成果物
- MP4: `units/unit17_knowledge_to_ai_asset/video_study.mp4`
- [[Remotion]] render dir: `units/unit17_knowledge_to_ai_asset/remotion_video_study_20260607_213602/`
- Drive file ID: `1BFZE3KYvRCdlfbhWXQjPhzlAtMzefeDj`
- Drive link: https://drive.google.com/file/d/1BFZE3KYvRCdlfbhWXQjPhzlAtMzefeDj/view?usp=drivesdk
- Drive parent: `Exports/videos/2026` (`1c_i3B3Wwe48xTeIB_7gSAQ-vVnBrncfI`)

## 入力素材
- [[GPT Image 2]]完成スライド: `assets_gptimage2/scene01.png`〜`scene10.png`
- 画像寸法: `scene01=1024x1536; scene02=1024x1536; scene03=1086x1448; scene04=1024x1536; scene05=1086x1448; scene06=1086x1448; scene07=1086x1448; scene08=1024x1536; scene09=1024x1536; scene10=1086x1448`
- rejected: `assets_gptimage2/scene07_rejected_extra_ai_text.png`（余計なAI文字混入のため退避）
- TTS: `audio/scene01.mp3`〜`scene10.mp3`
- 合計音声長: `247.840s`

## 実行コマンド結果
- `npm install`: success（185 packages, 0 vulnerabilities）
- `npm run lint`: success
- `npm run still`: success -> `remotion_video_study_20260607_213602/qa/still.png`
- `npm run render`: success -> `remotion_video_study_20260607_213602/out/video_study.mp4`
- `ffprobe`: `h264/aac`, `1080x1920`, duration `257.642667s`, size `20586752` bytes, bitrate `639234`
- `blackdetect`: `black_start`なし
- `volumedetect`: mean `-17.0 dB`, max `-3.7 dB`

## 目視QA
- raw slide contact sheet: `units/unit17_knowledge_to_ai_asset/qa/unit17_image_contact_sheet.png`
- still: `units/unit17_knowledge_to_ai_asset/remotion_video_study_20260607_213602/qa/still.png`
- final midpoint contact sheet: `units/unit17_knowledge_to_ai_asset/remotion_video_study_20260607_213602/qa/final_midpoint_contact_sheet.png`
- 判定: 合格。10シーン順序OK、黒/空白フレームなし、固定テンプレート維持、見切れ/文字かぶりなし。
- 契約確認: Stepはタイトルカード右上のみ、下部カード見出しは `おさえるべきポイント`、下部カード内Stepなし、下端フッター/進捗バー/内部テンプレートラベルなし。

## Drive検証
- `mimeType`: `video/mp4`
- `size`: `20586752`（ローカルMP4サイズ一致）
- owner: `shiomaruclaw@gmail.com`
- permissions: owner only `shiomaruclaw@gmail.com`
- public sharing: `false`
- metadata log: `units/unit17_knowledge_to_ai_asset/drive_upload_unit17_metadata_20260607_2143.json`

関連: [[AIエージェント・ストラテジスト]] / [[Unit17]] / [[Remotion]] / [[GPT Image 2]] / [[Google Drive]]
