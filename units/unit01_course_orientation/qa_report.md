# Unit01 QAレポート

## 対象
- Unit: [[Unit01]] 講座オリエンテーション：AIを使う人から導入する人へ
- Unit dir: `units/unit01_course_orientation/`
- Manifest範囲: p.5〜p.10
- 実参照ファイル: `../extracted_text/pages/page_005.txt`〜`page_010.txt`

## 現在状態
- 状態: `scene02_accepted_continue_image_generation`
- 教材: `lesson.md` / `script.md` / `quiz.md` / `exam_cards.md` / `storyboard.json` 作成済み
- [[GPT Image 2]]完成スライド: `scene01.png` / `scene02.png` 採用済み。旧`scene02.png`はUnit番号バッジ混入のため rejected へ退避済み。`scene03.png`〜`scene08.png` は未生成
- 音声: `audio/scene01.mp3`〜`scene08.mp3` 作成済み
- 正式動画: 未生成
- [[Google Drive]]: 未アップロード

## ソース・サニタイズQA
- 原文丸写しなし: 講義ノートとして再構成済み
- 個人情報透かし・メールアドレス・購入者情報: 成果物Markdown/TXT/JSON内検索0件
- 検索対象: `units/unit01_course_orientation/`
- 検索パターン: `t.shio` / `gmail.com` / `盭目` / `剛`

## TTS音声QA
- 生成経路: [[ElevenLabs]] TTS
- audio files: `scene01.mp3`〜`scene08.mp3`
- duration:
  - scene01: `28.400s`
  - scene02: `28.560s`
  - scene03: `27.760s`
  - scene04: `32.000s`
  - scene05: `30.880s`
  - scene06: `31.520s`
  - scene07: `27.120s`
  - scene08: `32.400s`
- total: `238.640s`

## 画像生成チェック
- 生成経路: [[GPT Image 2]] via [[Codex CLI]] `$imagegen`
- 直列キュー: `proc_e309e2955fb0`
- Queue command: `START_SCENE=02 WAIT_SECONDS=600 WAIT_BEFORE_FIRST=1 ./run_rate_limited_image_queue.sh`
- Queue log: `imagegen_rate_limited_queue.log`
- 生成済み:
  - `assets_gptimage2/scene01.png`: `1024x1536`
- Vision QA scene01:
  - 3:4縦長、白ベース、青・シアン系で統一。
  - 見切れなし。
  - 透かし、メールアドレス、個人情報なし。
  - スライド番号、不要フッターなし。
  - 「使う人から導入する人へ」「個人利用→組織導入」のテーマが伝わる。

## Remotion / MP4検証
- 未実施。全scene画像が揃った後、[[Unit12]]ロック版テンプレートをコピーして実施する。

## Google Drive検証
- 未実施。MP4完成後に `Exports/videos/2026/` へアップロードし、file ID / webViewLink / name / size / mimeType / permissionsを確認する。

## QA判定
- [[Unit01]]は教材テキスト・TTS・scene01画像まで進行中。
- `scene02.png` は生成成功したが、上部に `Unit01` 番号バッジが混入したため不採用。
- `TooManyRequests` は未発生。品質理由で直列キューを停止。
- 次は `scene02` の単発再生成とVision QA。番号バッジなしを確認してから `scene03` 以降へ進む。

## 2026-06-06 11:09 JST 画像品質停止
- [[GPT Image 2]] / [[Codex CLI]] `$imagegen` で `scene02.png` は生成成功し、寸法は `1024x1536`。
- Vision QAで上部に `Unit01` の青い番号バッジ混入を確認。
- `TooManyRequests` は未発生。品質理由で `proc_e309e2955fb0` を停止。
- `scene02.png` は `assets_gptimage2/rejected/scene02_unit01_badge_20260606_1109.png` に退避し、採用パスから削除済み。
- `prompts_gptimage2/scene01.txt`〜`scene08.txt` は、Unit番号・ページ番号・スライド番号・番号バッジ禁止文を追加済み。
- 再開は `scene02` の単発再生成から。再生成後にVision QAで番号バッジなしを確認してから `scene03` 以降へ進む。

## 2026-06-06 11:42 JST scene02再生成QA
- 1時間クールダウンは不要と判断し、`proc_5d5f2d81d5ab` を停止して即時単発再生成を実行。
- `assets_gptimage2/scene02.png`: `1024x1536`。
- Vision QA: 合格。Unit番号・ページ番号・スライド番号・番号バッジなし。見切れなし。透かし/不要フッター/メールアドレス/個人情報らしき文字列なし。
- 次は `scene03` を単発生成し、同じ品質ゲートを通す。

## 2026-06-06 11:45 JST scene03品質停止
- `assets_gptimage2/scene03.png`: `1024x1536` で生成成功。
- Vision QA: 不合格。中央ラベルが「ストラテジスト」ではなく「ストラデジスト」に崩れていた。
- Unit番号・ページ番号・スライド番号・番号バッジ、見切れ、透かし、不要フッター、個人情報らしき文字列はなし。
- 不採用画像は `assets_gptimage2/rejected/scene03_strategist_typo_20260606_1145.png` に退避済み。
- `scene03.txt` は中央ラベルを「導入設計」に変更し、「ストラテジスト」を画像内に入れない指定へ修正済み。

関連: [[AIエージェント・ストラテジスト]] / [[Unit01]] / [[GPT Image 2]] / [[Google Drive]]

## 2026-06-06 13:06 JST scene03 cron再開停止
- `scene03` を修正済みpromptで単発再生成したが、`TooManyRequests` で失敗。
- 新規 `assets_gptimage2/scene03.png` は生成されていない。
- Log: `imagegen_scene03_regen_20260606_cron_resume.log`
- 次回再開地点: `scene03`。

関連: [[AIエージェント・ストラテジスト]] / [[Unit01]] / [[GPT Image 2]] / [[TooManyRequests]]

## 2026-06-06 15:41 JST scene03再生成QA
- しおの[[Codex]]アプリ側ステータス確認を受け、`scene03` を単発再生成。
- `assets_gptimage2/scene03.png`: `1086x1448`。
- Vision QA: 合格。中央「導入設計」、周囲「対象業務」「現場」「法務」「情シス」「費用対効果」、下部「合意形成」「導入を前へ」は読める範囲。
- Unit番号・ページ番号・スライド番号・番号バッジなし。見切れなし。透かし/不要フッター/個人情報らしき文字列なし。
- 次は `scene04` を単発生成し、同じ品質ゲートを通す。

関連: [[AIエージェント・ストラテジスト]] / [[Unit01]] / [[GPT Image 2]] / [[Codex]]

## 2026-06-06 16:18 JST scene04〜08生成・動画レンダーQA
- [[GPT Image 2]] / [[Codex CLI]] `$imagegen` を待機なしの単発直列で実行し、`scene04.png`〜`scene08.png` を生成。
- 画像寸法:
  - `scene04.png`: `1086x1448`
  - `scene05.png`: `1003x1568`
  - `scene06.png`: `1024x1536`
  - `scene07.png`: `1024x1536`
  - `scene08.png`: `1024x1536`
- Vision QA: `scene04`〜`scene08` は合格。Unit番号・ページ番号・スライド番号・番号バッジ混入なし。見切れ、透かし、不要フッター、個人情報らしき文字列なし。
- [[Remotion]] レンダー:
  - Render dir: `remotion_video_study_20260606_160547/`
  - MP4: `video_study.mp4`
  - `npm run lint`: 成功
  - `npm run still`: 成功
  - `npm run render`: 成功
  - `ffprobe`: `1080x1920`, `24fps`, `249.791667s`, audio `aac`, `48000Hz`, stereo
  - file size: 約 `57MB`
- 中間フレームQA:
  - Contact sheet: `remotion_video_study_20260606_160547/qa/unit01_midframe_contact_sheet.png`
  - 抽出時刻: scene01 `14.833s`, scene02 `44.583s`, scene03 `74.021s`, scene04 `105.167s`, scene05 `137.875s`, scene06 `170.354s`, scene07 `200.938s`, scene08 `232.458s`
  - Vision QA: 合格。全sceneで黒画面/空白なし。ヘッダー、下部カード、Step表示、進捗バーに大きなズレなし。制作都合語や不要フッターなし。
- [[Google Drive]]:
  - アップロード未実施。`gws` のOAuth refresh tokenが `invalid_grant: Token has been expired or revoked` で停止。
  - `gws auth login -s drive` は認証URLを出して待機したが、ブラウザ側認証が完了せずタイムアウト。

関連: [[AIエージェント・ストラテジスト]] / [[Unit01]] / [[Remotion]] / [[Google Drive]]

## 2026-06-06 16:26 JST MP4サイズ最適化
- しおの指摘「いつもよりサイズ重くない？」を受け、既存Unit12と比較。
- 比較:
  - [[Unit01]] 初回MP4: `56.96 MiB`, `249.81s`, total bitrate `1,912,596bps`, video bitrate `1,589,975bps`
  - [[Unit12]] 既存MP4: `22.14 MiB`, `318.19s`, total bitrate `583,682bps`, video bitrate `260,734bps`
- 原因: [[Remotion]] 初回レンダーのH.264ビットレートが既存Unitより高めだった。
- 対応: `ffmpeg` で `libx264 -crf 30 -preset medium -pix_fmt yuv420p -c:a aac -b:a 96k` に再エンコード。
- 圧縮後:
  - Canonical MP4: `video_study.mp4`
  - Original backup: `video_study_original_57mb.mp4`
  - Size: `14 MiB`
  - Duration: `249.813s`
  - Video: `h264`, `1080x1920`, `24fps`, bitrate `373,514bps`
  - Audio: `aac`, `48000Hz`, stereo, bitrate `90,828bps`
- 圧縮後中間フレームQA:
  - Contact sheet: `remotion_video_study_20260606_160547/qa/unit01_crf30_midframe_contact_sheet.png`
  - Vision QA: 合格。文字潰れ、目立つブロックノイズ、黒画面、レイアウト崩れなし。

関連: [[AIエージェント・ストラテジスト]] / [[Unit01]] / [[Remotion]] / [[ffmpeg]]

## 2026-06-13 Drive納品・正式完了検証
- 状態: `completed_drive_verified`
- Drive: https://drive.google.com/file/d/1QECygfkb3YOHjn4N4dFHITY9LXGqwB27/view?usp=drivesdk
- file ID: `1QECygfkb3YOHjn4N4dFHITY9LXGqwB27`
- MP4: `units/unit01_course_orientation/video_study.mp4`
- ffprobe: `1080x1920`, `h264/aac`, local size `14671930` bytes
- Drive readback: `mimeType=video/mp4`, size `14671930` bytes、local/Drive size一致
- permissions: owner only `shiomaruclaw@gmail.com`、public/domain共有なし
- final contact sheet: `qa/final_u01_u04_20260613/unit01_04_final_contact_sheet.jpg`
- blackdetect: `qa/final_u01_u04_20260613/blackdetect_summary.txt`（black_startなし）
関連: [[Unit01]] / [[Google Drive]] / [[動画QA]]
