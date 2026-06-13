#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
OUT_DIR = BASE / "case_bank"
DATA_DIR = OUT_DIR / "data"
QA_DIR = OUT_DIR / "qa"
CASES_JSON = DATA_DIR / "cases.json"
INDEX_HTML = OUT_DIR / "index.html"
QA_REPORT = OUT_DIR / "qa_report.md"

TYPE_SCHEDULE = (
    ["choose_best"] * 40
    + ["choose_wrong"] * 25
    + ["choose_first_action"] * 15
    + ["choose_highest_risk"] * 10
    + ["choose_next_check"] * 10
)
TYPE_LABELS = {
    "choose_best": "最も適切な対応を選ぶ",
    "choose_wrong": "不適切な対応を見抜く",
    "choose_first_action": "最初の一手を選ぶ",
    "choose_highest_risk": "最もリスクが高い対応を選ぶ",
    "choose_next_check": "次に確認すべきことを選ぶ",
}
TYPE_QUESTIONS = {
    "choose_best": "この状況で最も適切な対応はどれですか？",
    "choose_wrong": "次のうち、最も避けるべき不適切な対応はどれですか？",
    "choose_first_action": "AIツール選定や実装に入る前に、最初に行うべきことはどれですか？",
    "choose_highest_risk": "この中で、最もリスクが高い進め方はどれですか？",
    "choose_next_check": "次に確認すべき項目として最も重要なものはどれですか？",
}
DIFFICULTIES = ["初級", "中級", "上級", "中級", "初級", "中級", "上級", "中級", "初級", "上級"]

CATEGORIES = [
    {
        "name": "業務課題発見",
        "unit": ["Unit 12", "Unit 13", "Unit 15", "Unit 39"],
        "tags": ["課題発見", "業務整理", "As-Is/To-Be"],
        "topics": [
            ("営業日報の入力負荷", "営業部", "日報入力をAIで楽にしたい", "入力項目が多く、マネージャーが読める粒度もばらついている", "日報テンプレートと活用目的", "営業責任者", "入力時間と案件更新率"),
            ("問い合わせ分類の混乱", "カスタマーサポート", "問い合わせを自動で振り分けたい", "カテゴリ名が担当者ごとに違い、過去履歴にも表記ゆれがある", "問い合わせ履歴と分類ルール", "サポートリーダー", "一次分類の正確率"),
            ("請求確認の手戻り", "経理部", "請求書チェックをAIに任せたい", "例外処理が口頭で共有され、チェック観点が明文化されていない", "請求チェックリスト", "経理担当者", "差し戻し件数"),
            ("採用候補者対応", "人事部", "候補者への案内を自動化したい", "職種ごとに案内内容が違い、最新情報の所在が分かれています", "採用FAQと職種別案内", "採用担当者", "返信待ち時間"),
            ("現場報告の属人化", "店舗運営部", "店舗からの報告をAIで要約したい", "報告文の長さや表現が店舗ごとに大きく異なる", "報告フォーマット", "エリアマネージャー", "要約確認時間"),
            ("契約確認の遅延", "法務部", "契約書レビューの一次確認をAI化したい", "契約類型とリスク基準が整理されていない", "契約類型別チェック観点", "法務責任者", "一次確認の所要時間"),
            ("在庫問い合わせの集中", "物流部", "在庫確認をAIチャットで受けたい", "基幹システムと現場メモの情報が一致しないことがある", "在庫データの更新ルール", "物流管理者", "回答一致率"),
            ("稟議作成のばらつき", "管理部", "稟議書の下書きをAIに作らせたい", "承認者が重視する観点が部署ごとに違う", "稟議テンプレートと承認基準", "承認者", "差し戻し率"),
            ("マニュアル探索の時間", "情報システム部", "社内マニュアルをAIで探せるようにしたい", "ファイル名と内容が一致せず、古い版も残っている", "マニュアル版管理", "情シス担当者", "検索成功率"),
            ("研修質問対応", "教育担当", "受講者質問への回答をAIで支援したい", "質問の背景知識に差があり、同じ回答では伝わりにくい", "研修FAQと受講者レベル", "講師", "再質問率"),
        ],
    },
    {
        "name": "AIエージェント適用判断",
        "unit": ["Unit 04", "Unit 05", "Unit 07", "Unit 09"],
        "tags": ["適用判断", "エージェント", "自律性"],
        "topics": [
            ("月次レポート作成", "経営企画", "月次レポートを自動で作りたい", "データ取得、加工、コメント作成、配布まで複数手順がある", "月次レポート工程", "経営企画責任者", "作成時間と修正回数"),
            ("メール返信補助", "営業部", "定型メールをAIに返信させたい", "相手先や契約状況によって文面判断が必要です", "メール種別と承認条件", "営業担当", "返信品質評価"),
            ("経費精算確認", "管理部", "経費精算をAIで確認したい", "領収書、規程、例外承認の照合が必要です", "経費規程と例外ルール", "管理部長", "確認工数"),
            ("商談準備", "営業企画", "商談前の企業調査をAIに任せたい", "公開情報と社内履歴を組み合わせる必要があります", "調査観点と出典ルール", "営業マネージャー", "準備時間"),
            ("シフト調整", "店舗運営", "シフト調整をAIで自動化したい", "希望、スキル、労務制約、急な欠勤を考慮します", "シフト制約条件", "店長", "調整回数"),
            ("FAQ応答", "サポート", "FAQ応答をAIエージェントに任せたい", "回答だけでなく必要に応じてチケット起票も必要です", "FAQと起票条件", "サポート責任者", "一次解決率"),
            ("議事録からタスク化", "プロジェクト管理", "会議内容からタスクを自動抽出したい", "決定事項と検討事項が会話の中に混在しています", "議事録ルール", "PM", "タスク抽出精度"),
            ("採用スクリーニング", "人事", "応募書類の確認をAIで効率化したい", "評価基準の公平性と説明可能性が求められます", "評価基準表", "人事責任者", "レビュー時間"),
            ("障害一次対応", "情報システム", "社内IT問い合わせをAIで一次対応したい", "権限付与や端末操作を伴うケースがあります", "対応範囲とエスカレーション基準", "情シス責任者", "自己解決率"),
            ("見積作成", "営業管理", "見積書作成をAIで補助したい", "価格表、個別値引き、承認条件の参照が必要です", "価格表と承認条件", "営業管理者", "見積ミス率"),
        ],
    },
    {
        "name": "RAG・ナレッジ活用",
        "unit": ["Unit 16", "Unit 17", "Unit 18", "Unit 19"],
        "tags": ["RAG", "ナレッジ", "検索"],
        "topics": [
            ("古いFAQの混在", "サポート", "FAQをRAGで参照させたい", "旧版FAQと新版FAQが同じフォルダに残っています", "FAQの版管理", "ナレッジ管理者", "誤回答率"),
            ("議事録検索", "開発部", "過去議事録から決定理由を探したい", "議事録のタイトルだけでは内容が判断できません", "議事録メタデータ", "開発リーダー", "検索ヒット精度"),
            ("規程回答", "人事労務", "就業規則への質問にAIで答えたい", "例外規程や改定履歴の扱いが曖昧です", "規程本文と改定履歴", "労務担当", "回答根拠提示率"),
            ("製品仕様検索", "営業支援", "製品仕様をAIに答えさせたい", "仕様書、価格表、販促資料の内容に差があります", "製品資料の正本", "商品企画", "回答一致率"),
            ("社内手順書", "バックオフィス", "手順書をチャットで検索したい", "部署ごとのローカル手順が残っています", "手順書の正本管理", "業務管理者", "手順遵守率"),
            ("顧客別ルール", "営業事務", "顧客別対応ルールをAIに確認させたい", "顧客情報には権限差と機密度があります", "顧客別ルールと権限", "営業事務責任者", "確認時間"),
            ("技術問い合わせ", "技術サポート", "過去対応から回答候補を出したい", "過去回答には暫定対応と恒久対応が混在しています", "対応履歴の分類", "技術責任者", "再オープン率"),
            ("研修教材検索", "教育担当", "教材から必要箇所を探したい", "スライド、動画台本、補足資料が別管理です", "教材メタデータ", "講座設計者", "該当箇所到達時間"),
            ("法務ナレッジ", "法務", "契約レビュー観点を検索したい", "案件種別ごとの判断理由が文章中に埋もれています", "レビュー観点タグ", "法務担当", "観点漏れ件数"),
            ("障害ナレッジ", "情シス", "障害対応手順をAIで案内したい", "古い回避策が検索上位に出ることがあります", "障害手順の有効期限", "運用担当", "一次復旧時間"),
        ],
    },
    {
        "name": "プロンプト・指示設計",
        "unit": ["Unit 03", "Unit 05", "Unit 30", "Unit 31"],
        "tags": ["プロンプト", "指示設計", "コンテキスト"],
        "topics": [
            ("要約の粒度", "経営企画", "長い資料をAIに要約させたい", "役員向けと実務担当向けで必要な粒度が違います", "要約目的と読者", "資料作成者", "修正回数"),
            ("メール文面", "営業", "顧客メールの下書きをAIに作らせたい", "丁寧さ、禁止表現、次アクションが案件ごとに違います", "文面ルール", "営業担当", "承認修正率"),
            ("FAQ回答トーン", "サポート", "回答文のトーンを統一したい", "謝罪、案内、確認依頼の使い分けが難しい", "応対トーン基準", "品質管理担当", "品質評価"),
            ("分析観点", "マーケティング", "アンケート自由回答を分析したい", "分類観点を指定しないと一般的な要約になります", "分析軸", "マーケ責任者", "示唆採用数"),
            ("議事録タスク", "PMO", "議事録からTODOを抽出したい", "担当者名、期限、未決事項を区別する必要があります", "抽出ルール", "PM", "タスク漏れ率"),
            ("レビュー観点", "法務", "契約書の気になる点を出したい", "リスクの重要度と根拠条文を分けたいです", "レビュー観点テンプレート", "法務担当", "観点の再現性"),
            ("チャットボット制約", "情シス", "社内ボットに禁止事項を守らせたい", "権限外回答や断定表現を避けたいです", "回答ポリシー", "情シス管理者", "逸脱件数"),
            ("企画書作成", "新規事業", "企画書のたたきをAIに作らせたい", "市場、顧客、収益性の観点が抜けやすい", "企画書構成", "事業責任者", "レビュー指摘数"),
            ("コード説明", "開発", "コード変更点を説明させたい", "読み手が非エンジニアの場合もあります", "説明対象と粒度", "開発リーダー", "理解度評価"),
            ("研修フィードバック", "教育", "受講者回答にコメントしたい", "否定しすぎず、次の学習行動につなげたい", "フィードバック方針", "講師", "再提出改善率"),
        ],
    },
    {
        "name": "ワークフロー自動化",
        "unit": ["Unit 26", "Unit 27", "Unit 28", "Unit 29"],
        "tags": ["自動化", "ワークフロー", "HITL"],
        "topics": [
            ("承認前チェック", "管理部", "稟議前チェックを自動化したい", "金額や案件種別で承認ルートが変わります", "承認条件", "管理責任者", "差し戻し率"),
            ("問い合わせ起票", "サポート", "メールからチケットを自動起票したい", "緊急度と担当チームを判定する必要があります", "起票ルール", "サポート責任者", "初動時間"),
            ("定例資料更新", "経営企画", "毎週の数字更新を自動化したい", "データ取得失敗時の扱いが決まっていません", "更新手順と例外処理", "企画担当", "更新ミス件数"),
            ("採用連絡", "人事", "面接日程案内を自動化したい", "候補者都合と面接官予定を調整します", "日程調整条件", "採用担当", "調整往復数"),
            ("在庫アラート", "物流", "在庫不足を自動通知したい", "商品別に閾値と通知先が違います", "在庫閾値ルール", "物流担当", "欠品予兆検知"),
            ("経費アラート", "経理", "規程違反っぽい申請を検出したい", "判断が曖昧な申請は人の確認が必要です", "規程違反条件", "経理責任者", "確認時間"),
            ("商談後フォロー", "営業", "商談後メールとCRM更新を自動化したい", "商談内容により送る資料が変わります", "フォロー分岐条件", "営業マネージャー", "フォロー漏れ"),
            ("障害通知", "情シス", "障害検知後の連絡を自動化したい", "影響範囲が未確定な段階で連絡が必要です", "通知テンプレート", "運用責任者", "初報時間"),
            ("レビュー依頼", "開発", "PR内容からレビュー担当を提案したい", "専門領域と負荷の両方を考慮します", "担当割当ルール", "開発リーダー", "レビュー待ち時間"),
            ("研修リマインド", "教育", "未受講者へ自動リマインドしたい", "役職や締切により文面を変えたいです", "リマインド条件", "教育担当", "受講完了率"),
        ],
    },
    {
        "name": "ツール連携",
        "unit": ["Unit 08", "Unit 27", "Unit 28", "Unit 30"],
        "tags": ["ツール連携", "MCP", "API"],
        "topics": [
            ("CRM連携", "営業", "CRMから情報を取得して回答したい", "顧客ごとに閲覧権限が異なります", "CRM権限設計", "営業管理者", "参照ミス率"),
            ("カレンダー連携", "人事", "面接日程を自動調整したい", "外部候補者と社内面接官の予定を扱います", "カレンダー連携範囲", "採用担当", "調整完了時間"),
            ("チケット連携", "情シス", "問い合わせからチケット更新まで行いたい", "誤ってクローズすると業務影響があります", "チケット操作権限", "情シス責任者", "誤更新件数"),
            ("ストレージ検索", "管理部", "社内ファイルを横断検索したい", "部署限定資料と全社資料が混在しています", "フォルダ権限", "情報管理者", "権限逸脱ゼロ"),
            ("チャット通知", "PMO", "進捗遅延をチャットに通知したい", "通知が多すぎると現場が見なくなります", "通知条件", "PM", "有効通知率"),
            ("BI連携", "経営企画", "BIの数値をAIが説明するようにしたい", "指標定義を知らないと誤った説明になります", "指標定義書", "データ担当", "説明正確率"),
            ("メール送信", "営業支援", "AIがメール送信まで行うようにしたい", "宛先や添付間違いの影響が大きいです", "送信前確認ルール", "営業責任者", "誤送信ゼロ"),
            ("SFA更新", "営業", "商談メモからSFAを更新したい", "確定情報と推測情報が混ざっています", "更新項目定義", "営業企画", "更新差し戻し率"),
            ("勤怠連携", "労務", "勤怠異常をAIで確認したい", "個人情報と労務判断が関わります", "勤怠データ権限", "労務責任者", "確認漏れ件数"),
            ("ナレッジ投稿", "サポート", "解決済みチケットからFAQを作りたい", "未確認情報を公開すると混乱します", "FAQ公開承認", "ナレッジ担当", "公開後修正率"),
        ],
    },
    {
        "name": "セキュリティ・権限",
        "unit": ["Unit 10", "Unit 18", "Unit 20", "Unit 38"],
        "tags": ["セキュリティ", "権限", "ガバナンス"],
        "topics": [
            ("個人情報を含む問い合わせ", "サポート", "顧客情報を含む問い合わせをAIで要約したい", "個人情報や契約情報が本文に含まれることがあります", "個人情報取扱ルール", "情報管理責任者", "漏えいゼロ"),
            ("管理者権限の操作", "情シス", "AIにアカウント権限付与を任せたい", "権限付与は業務影響が大きく監査も必要です", "権限申請フロー", "情シス責任者", "不正付与ゼロ"),
            ("社外AI利用", "企画部", "外部AIに社内資料を貼って分析したい", "資料には未公開情報が含まれます", "外部AI利用基準", "情報セキュリティ担当", "利用ルール遵守率"),
            ("ログ保存", "法務", "AIの判断ログを保存したい", "保存期間と閲覧権限が未定です", "監査ログ設計", "法務担当", "追跡可能率"),
            ("部署別ナレッジ", "全社", "部署ごとの資料をAI検索したい", "検索結果に他部署の機密が出る懸念があります", "アクセス制御", "情報管理者", "権限逸脱ゼロ"),
            ("自動送信", "営業", "AIが顧客にメールを送る運用にしたい", "誤送信や不適切表現が信用問題になります", "送信承認条件", "営業責任者", "誤送信ゼロ"),
            ("モデル学習利用", "開発", "入力データを学習に使う設定を確認したい", "契約上のデータ利用条件が未確認です", "AIサービス契約条件", "法務・情シス", "設定確認率"),
            ("委託先連携", "管理部", "委託先にもAIボットを使わせたい", "社外ユーザーの権限とログ管理が必要です", "外部ユーザー権限", "委託管理者", "アクセス棚卸し率"),
            ("機密分類", "研究開発", "研究メモをAIで整理したい", "機密度が高い情報と公開可能情報が混在しています", "情報分類基準", "研究責任者", "分類精度"),
            ("退職者アカウント", "人事・情シス", "退職時のアクセス停止をAIで支援したい", "停止漏れは重大リスクになります", "退職時チェックリスト", "情シス担当", "停止漏れゼロ"),
        ],
    },
    {
        "name": "評価・品質保証",
        "unit": ["Unit 23", "Unit 24", "Unit 25", "Unit 42"],
        "tags": ["評価", "品質保証", "PoC"],
        "topics": [
            ("回答品質評価", "サポート", "AI回答の品質を測りたい", "正解だけでなく言い回しや根拠提示も重要です", "評価観点表", "品質管理担当", "合格率"),
            ("PoC成功判定", "経営企画", "AI導入PoCの成否を判断したい", "現場の満足度と工数削減がずれる可能性があります", "成功指標", "プロジェクト責任者", "KPI達成率"),
            ("誤回答テスト", "法務", "契約レビューAIの誤りを検出したい", "見落としの影響が大きく、例外パターンもあります", "テストケース集", "法務責任者", "重大見落としゼロ"),
            ("運用モニタリング", "情シス", "AIボットの稼働後品質を見たい", "利用数だけでは品質劣化に気づけません", "監視指標", "運用担当", "エスカレーション率"),
            ("人手レビュー", "営業支援", "AI作成文を人が確認する基準を作りたい", "すべて確認すると効率化効果が小さくなります", "レビュー条件", "営業責任者", "確認工数"),
            ("評価データ作成", "教育", "研修AIの採点精度を確認したい", "模範解答が1つに限られない問題があります", "採点ルーブリック", "講座設計者", "採点一致率"),
            ("A/B比較", "マーケ", "AI文案の効果を比較したい", "開封率だけでは商談化への影響が分かりません", "比較設計", "マーケ責任者", "商談化率"),
            ("ガードレール検証", "全社", "AIが禁止回答をしないか試したい", "通常質問だけでは逸脱を見つけにくいです", "禁止回答テスト", "ガバナンス担当", "逸脱ゼロ"),
            ("改善サイクル", "サポート", "AI回答を継続改善したい", "現場の修正内容がナレッジ更新に戻っていません", "フィードバックループ", "ナレッジ担当", "改善反映率"),
            ("ベンダー比較", "購買", "複数AIツールを評価したい", "デモの印象だけで選ぶと運用で差が出ます", "比較評価表", "購買責任者", "要件適合率"),
        ],
    },
    {
        "name": "導入計画・ROI",
        "unit": ["Unit 23", "Unit 24", "Unit 25", "Unit 43"],
        "tags": ["導入計画", "ROI", "展開"],
        "topics": [
            ("コスト試算", "経営企画", "AI導入の費用対効果を示したい", "ライセンス費だけでなく教育・運用費もかかります", "コスト項目", "経営層", "投資回収期間"),
            ("段階導入", "全社DX", "全社に一気にAIを展開したい", "部署ごとに業務成熟度とデータ整備状況が違います", "展開ロードマップ", "DX責任者", "定着率"),
            ("対象業務選定", "業務改革", "最初のAI導入テーマを選びたい", "候補が多く、効果とリスクの比較が必要です", "テーマ選定基準", "改革責任者", "優先順位合意"),
            ("教育費用", "人事", "AI研修の投資対効果を説明したい", "受講完了だけでは業務活用につながったか分かりません", "教育KPI", "人事責任者", "活用件数"),
            ("ベンダー契約", "購買", "AIサービス契約を進めたい", "従量課金とデータ利用条件の確認が必要です", "契約評価表", "購買担当", "想定外費用ゼロ"),
            ("人員配置", "サポート", "AI導入後の人員計画を見直したい", "削減だけを目的にすると現場協力が得にくいです", "役割再設計", "サポート責任者", "高付加価値業務比率"),
            ("経営報告", "DX推進", "AI導入状況を経営会議に報告したい", "利用数、品質、効果を分けて見せる必要があります", "報告ダッシュボード", "DX担当", "意思決定スピード"),
            ("リスク予算", "情シス", "セキュリティ対策費を含めたい", "便利さだけを強調すると必要な対策費が削られます", "リスク対策項目", "CIO", "対策実施率"),
            ("スモールスタート", "中小企業", "小さくAI活用を始めたい", "予算と担当者が限られています", "最小実行範囲", "経営者", "初回成果までの日数"),
            ("効果測定", "営業", "AI支援の売上効果を測りたい", "売上は外部要因にも左右されます", "測定設計", "営業責任者", "活動効率改善率"),
        ],
    },
    {
        "name": "社内定着・失敗対応",
        "unit": ["Unit 32", "Unit 33", "Unit 36", "Unit 37"],
        "tags": ["定着", "変革", "失敗対応"],
        "topics": [
            ("利用が広がらない", "全社", "AIツールを入れたが使われない", "現場は何に使えばよいか分からない状態です", "ユースケース集", "DX推進者", "週次利用率"),
            ("現場の不安", "営業部", "AIで仕事が奪われると不安が出ている", "目的が効率化だけに見えています", "役割説明", "部門長", "参加率"),
            ("品質クレーム", "サポート", "AI回答で顧客から指摘が出た", "誰が確認し、どう改善するか決まっていません", "インシデント対応手順", "品質責任者", "再発件数"),
            ("ルール未整備", "全社", "部署ごとにAI利用ルールがばらばら", "禁止事項と推奨例が共有されていません", "利用ガイドライン", "ガバナンス担当", "違反件数"),
            ("チャンピオン不足", "DX推進", "推進担当だけが頑張っている", "各部署に相談役がいません", "推進体制", "DX責任者", "相談対応件数"),
            ("成功事例共有", "人事", "AI活用事例を社内に広めたい", "事例が個人の工夫に留まり再現されていません", "事例テンプレート", "教育担当", "横展開数"),
            ("過度な期待", "経営層", "AIなら何でもできるという期待がある", "できることとできないことの線引きが必要です", "期待値調整資料", "DX推進者", "手戻り件数"),
            ("現場改善の停滞", "店舗", "初期導入後に改善が止まった", "フィードバックの集約先が決まっていません", "改善バックログ", "店舗責任者", "改善実施数"),
            ("責任分界", "全社", "AIの判断ミス時の責任が曖昧", "利用者、承認者、運用者の役割が混ざっています", "責任分界表", "管理部", "判断迷い件数"),
            ("教育の継続", "教育", "初回研修後に活用が続かない", "学習後に実務へ戻す仕組みがありません", "実務ミッション", "講師", "実務適用件数"),
        ],
    },
]

GENERAL_DISTRACTORS = [
    "AIの出力を数日使ってから、問題が出た時点でルールを整備する",
    "現場への説明を後回しにして、まず全員に同じ使い方を指示する",
    "精度が高そうなツールを選び、業務側の整理は導入後に進める",
    "例外対応をAIに任せ、人の確認は利用者から苦情が出た時だけ行う",
]


def rotate_with_answer(options: list[str], answer_text: str, desired_index: int) -> tuple[list[str], int]:
    pool = []
    for item in options:
        if item not in pool:
            pool.append(item)
    pool = [x for x in pool if x != answer_text]
    while len(pool) < 3:
        pool.append(GENERAL_DISTRACTORS[len(pool) % len(GENERAL_DISTRACTORS)])
    choices = pool[:3]
    idx = desired_index % 4
    choices.insert(idx, answer_text)
    return choices, idx


def build_actions(category: str, topic: tuple[str, str, str, str, str, str, str], idx: int) -> dict[str, str]:
    title, dept, request, condition, asset, stakeholder, metric = topic
    best = f"{asset}と現行フローを棚卸しし、{metric}を指標に小さく検証してから展開範囲を決める"
    first = f"{stakeholder}に確認し、目的・制約・{asset}の正本を1枚に整理する"
    wrong = f"最新AIツールを先に契約し、{asset}や運用ルールは利用状況を見ながら後で整える"
    risk = f"{asset}を権限確認なしでAIに接続し、関係者全員が自由に使える状態にする"
    next_check = f"{asset}の更新責任者、利用権限、成功指標としての{metric}を確認する"
    plausible_a = f"{dept}の一部メンバーで試行し、失敗例と例外条件を集めて改善する"
    plausible_b = f"対象範囲を限定し、人が確認する条件を決めたうえでAI支援を始める"
    return {
        "best": best,
        "first": first,
        "wrong": wrong,
        "risk": risk,
        "next_check": next_check,
        "plausible_a": plausible_a,
        "plausible_b": plausible_b,
    }


def build_case(case_no: int, category: dict, topic: tuple[str, str, str, str, str, str, str], topic_idx: int) -> dict:
    case_type = TYPE_SCHEDULE[case_no - 1]
    title, dept, request, condition, asset, stakeholder, metric = topic
    actions = build_actions(category["name"], topic, topic_idx)
    scenario = f"あなたは{dept}を支援するAI導入担当です。{dept}から「{request}」と相談されました。現状は、{condition}。"
    question = TYPE_QUESTIONS[case_type]
    if case_type == "choose_best":
        answer_text = actions["best"]
        options = [actions["plausible_a"], actions["wrong"], actions["plausible_b"], actions["risk"]]
        explanation = f"この場面では、いきなり導入するより、{asset}と業務の流れをそろえてから{metric}で検証することが重要です。小さく試すことで、効果とリスクを同時に確認できます。"
    elif case_type == "choose_wrong":
        answer_text = actions["wrong"]
        options = [actions["best"], actions["first"], actions["plausible_a"], actions["plausible_b"]]
        explanation = f"不適切なのは、ツール選定を先行させて{asset}や運用ルールの整理を後回しにする進め方です。AI導入では、参照情報・責任・評価軸を先にそろえる必要があります。"
    elif case_type == "choose_first_action":
        answer_text = actions["first"]
        options = [actions["best"], actions["wrong"], actions["plausible_b"], actions["risk"]]
        explanation = f"最初の一手は、目的と制約、そして{asset}の正本を確認することです。ここが曖昧なまま実装すると、後から評価や権限設計で手戻りが起きます。"
    elif case_type == "choose_highest_risk":
        answer_text = actions["risk"]
        options = [actions["best"], actions["first"], actions["plausible_a"], actions["wrong"]]
        explanation = f"最もリスクが高いのは、権限確認なしで{asset}をAIに接続することです。情報漏えいや誤操作につながるため、アクセス制御とログ設計が先に必要です。"
    else:
        answer_text = actions["next_check"]
        options = [actions["best"], actions["first"], actions["wrong"], actions["plausible_a"]]
        explanation = f"次に確認すべきなのは、{asset}の更新責任、利用権限、{metric}です。これにより、AIが参照する情報の信頼性と導入効果を判断できます。"
    choices, answer_index = rotate_with_answer(options, answer_text, (case_no + topic_idx) % 4)
    why_others = []
    for choice in choices:
        if choice == answer_text:
            why_others.append("この選択肢が、このケースで最も問われている判断に合っています。")
        elif choice == actions["wrong"]:
            why_others.append("ツール導入を先行させ、業務・データ・運用ルールの整理を後回しにしている点が危険です。")
        elif choice == actions["risk"]:
            why_others.append("権限や監査を確認せずにAIへ接続しており、情報漏えい・誤操作のリスクが高くなります。")
        elif choice == actions["first"]:
            why_others.append("初期確認としては有効ですが、この設問で求める最終判断としてはまだ一歩手前です。")
        else:
            why_others.append("一部は有効ですが、目的・情報・権限・評価をそろえる観点が不足しています。")
    difficulty = DIFFICULTIES[topic_idx]
    related_units = category["unit"][:]
    if case_no % 3 == 0 and "Unit 45" not in related_units:
        related_units.append("Unit 45")
    return {
        "id": f"C{case_no:03d}",
        "title": title,
        "category": category["name"],
        "type": case_type,
        "typeLabel": TYPE_LABELS[case_type],
        "difficulty": difficulty,
        "relatedUnits": related_units[:4],
        "scenario": scenario,
        "question": question,
        "choices": choices,
        "answerIndex": answer_index,
        "explanation": explanation,
        "whyOthers": why_others,
        "reflectionPrompts": [
            f"あなたの職場で、{asset}に相当する情報はどこにありますか？",
            f"{stakeholder}以外に、最初に巻き込むべき人は誰ですか？",
            f"{metric}を測るために、今日から取れる小さな記録は何ですか？",
        ],
        "tags": sorted(set(category["tags"] + [dept, asset.split("と")[0]]))[:5],
    }


def build_cases() -> list[dict]:
    cases = []
    case_no = 1
    for category in CATEGORIES:
        for topic_idx, topic in enumerate(category["topics"]):
            cases.append(build_case(case_no, category, topic, topic_idx))
            case_no += 1
    return cases


def render_html(cases: list[dict]) -> str:
    cases_json = json.dumps(cases, ensure_ascii=False, indent=2)
    generated_at = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M JST")
    categories = sorted({c["category"] for c in cases})
    categories_json = json.dumps(categories, ensure_ascii=False)
    type_counts = Counter(c["type"] for c in cases)
    type_counts_json = json.dumps(type_counts, ensure_ascii=False)
    return f'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>実践ケース問題100選 | AIエージェント・ストラテジスト</title>
  <style>
    :root {{ --bg:#f7f8fb; --panel:#fff; --ink:#172033; --muted:#66708a; --line:#e5e8f0; --brand:#3858ff; --brand2:#00a6a6; --soft:#eef2ff; --ok:#168456; --bad:#b42318; --warn:#b96b00; --shadow:0 18px 40px rgba(24,34,61,.10); --radius:24px; }}
    * {{ box-sizing:border-box; }}
    html {{ scroll-behavior:smooth; }}
    body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans JP",sans-serif; color:var(--ink); background: radial-gradient(circle at top left, rgba(56,88,255,.16), transparent 34rem), radial-gradient(circle at top right, rgba(0,166,166,.14), transparent 30rem), var(--bg); line-height:1.75; }}
    a {{ color:inherit; }}
    .wrap {{ width:min(1180px, calc(100% - 32px)); margin:0 auto; }}
    header {{ padding:22px 0; position:sticky; top:0; z-index:10; backdrop-filter:blur(16px); background:rgba(247,248,251,.84); border-bottom:1px solid rgba(229,232,240,.9); }}
    .nav {{ display:flex; gap:12px; align-items:center; justify-content:space-between; }}
    .brand {{ display:flex; gap:12px; align-items:center; font-weight:900; }}
    .mark {{ width:42px; height:42px; border-radius:14px; display:grid; place-items:center; color:white; background:linear-gradient(135deg,var(--brand),var(--brand2)); box-shadow:var(--shadow); }}
    .navlinks {{ display:flex; flex-wrap:wrap; gap:10px; justify-content:flex-end; }}
    .pill {{ text-decoration:none; border:1px solid var(--line); background:rgba(255,255,255,.78); padding:9px 13px; border-radius:999px; color:var(--muted); font-size:13px; }}
    .hero {{ padding:48px 0 24px; }}
    .heroGrid {{ display:grid; grid-template-columns:1.15fr .85fr; gap:22px; align-items:stretch; }}
    .panel,.heroCard,.caseCard {{ background:rgba(255,255,255,.9); border:1px solid var(--line); border-radius:var(--radius); box-shadow:var(--shadow); }}
    .heroCard {{ padding:32px; overflow:hidden; position:relative; }}
    .eyebrow {{ color:var(--brand); font-weight:900; font-size:14px; }}
    h1 {{ margin:8px 0 0; font-size:clamp(30px,5vw,56px); line-height:1.12; letter-spacing:-.04em; }}
    h2 {{ margin:0; font-size:clamp(24px,3vw,34px); letter-spacing:-.03em; }}
    h3 {{ margin:10px 0 8px; font-size:20px; line-height:1.45; }}
    .lead,.muted {{ color:var(--muted); }}
    .lead {{ margin:18px 0 0; font-size:clamp(15px,2.2vw,18px); max-width:760px; }}
    .ctaRow {{ display:flex; flex-wrap:wrap; gap:12px; margin-top:22px; }}
    .btn {{ appearance:none; border:0; display:inline-flex; align-items:center; justify-content:center; gap:8px; min-height:46px; padding:12px 16px; border-radius:14px; font:inherit; font-weight:850; text-decoration:none; cursor:pointer; transition:.15s ease; }}
    .btn:hover {{ transform:translateY(-1px); }}
    .btnPrimary {{ background:linear-gradient(135deg,var(--brand),#243bd1); color:white; box-shadow:0 14px 28px rgba(56,88,255,.22); }}
    .btnGhost {{ background:white; color:var(--ink); border:1px solid var(--line); }}
    .btnSoft {{ background:var(--soft); color:#243bd1; }}
    .stats {{ padding:20px; display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; }}
    .stat {{ background:#fff; border:1px solid var(--line); border-radius:18px; padding:16px; min-width:0; }}
    .stat b {{ display:block; font-size:30px; line-height:1.05; }}
    section {{ padding:24px 0; }}
    .sectionTitle {{ display:flex; justify-content:space-between; align-items:flex-end; gap:14px; margin-bottom:14px; }}
    .pathGrid {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; }}
    .pathStep {{ padding:18px; border-radius:20px; background:white; border:1px solid var(--line); min-width:0; }}
    .pathStep strong {{ display:block; font-size:16px; }}
    .toolbar {{ padding:18px; display:grid; grid-template-columns:1fr auto auto auto; gap:12px; align-items:center; }}
    input,select,textarea {{ width:100%; min-height:46px; border:1px solid var(--line); border-radius:14px; background:white; padding:0 14px; font:inherit; color:var(--ink); }}
    textarea {{ min-height:90px; padding:12px 14px; resize:vertical; }}
    .categoryChips {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:12px; }}
    .chip {{ border:1px solid var(--line); background:white; border-radius:999px; padding:9px 12px; cursor:pointer; font:inherit; color:var(--muted); }}
    .chip.active {{ background:var(--soft); color:#243bd1; border-color:rgba(56,88,255,.28); font-weight:850; }}
    .grid {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:16px; }}
    .caseCard {{ padding:20px; min-width:0; display:flex; flex-direction:column; gap:12px; }}
    .meta {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; }}
    .badge {{ display:inline-flex; align-items:center; border:1px solid var(--line); background:#fff; color:var(--muted); border-radius:999px; padding:5px 9px; font-size:12px; font-weight:750; }}
    .typeBadge {{ background:var(--soft); color:#243bd1; border-color:rgba(56,88,255,.22); }}
    .scenario {{ padding:14px; background:#fbfcff; border:1px solid var(--line); border-radius:16px; }}
    .choices {{ display:grid; gap:10px; }}
    .choice {{ text-align:left; border:1px solid var(--line); background:white; border-radius:15px; padding:12px; font:inherit; cursor:pointer; min-height:48px; }}
    .choice.correct {{ border-color:rgba(22,132,86,.45); background:rgba(22,132,86,.08); color:#0c6843; font-weight:850; }}
    .choice.wrong {{ border-color:rgba(180,35,24,.35); background:rgba(180,35,24,.06); color:#8a1c14; }}
    .answerBox {{ display:none; border:1px solid var(--line); background:#fff; border-radius:16px; padding:14px; }}
    .answerBox.open {{ display:block; }}
    .whyList {{ margin:8px 0 0; padding-left:20px; color:var(--muted); }}
    .reflection {{ border-top:1px dashed var(--line); padding-top:12px; }}
    .reflection ul {{ margin:8px 0; padding-left:20px; }}
    .caseFooter {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:auto; }}
    .empty {{ grid-column:1/-1; padding:40px; text-align:center; color:var(--muted); }}
    footer {{ padding:36px 0 50px; color:var(--muted); font-size:13px; }}
    @media (max-width: 980px) {{ .heroGrid,.grid {{ grid-template-columns:1fr; }} .pathGrid {{ grid-template-columns:repeat(2,minmax(0,1fr)); }} .toolbar {{ grid-template-columns:1fr; }} }}
    @media (max-width: 620px) {{ .wrap {{ width:min(100% - 22px,1180px); }} header {{ position:static; padding-top:16px; }} .nav {{ align-items:flex-start; }} .navlinks {{ display:none; }} .hero {{ padding-top:24px; }} .heroCard {{ padding:22px; border-radius:22px; }} .stats {{ grid-template-columns:1fr; padding:14px; }} .stat b {{ font-size:24px; }} .pathGrid {{ grid-template-columns:1fr; }} .sectionTitle {{ align-items:flex-start; flex-direction:column; }} .caseCard {{ padding:16px; }} }}
  </style>
</head>
<body>
  <header>
    <div class="wrap nav">
      <div class="brand"><div class="mark">AI</div><div>実践ケース問題100選<br><span class="muted">AIエージェント・ストラテジスト</span></div></div>
      <nav class="navlinks" aria-label="ナビゲーション">
        <a class="pill" href="../elearning_page/index.html">ポータルへ戻る</a>
        <a class="pill" href="#cases">ケース一覧</a>
        <a class="pill" href="#howto">使い方</a>
      </nav>
    </div>
  </header>
  <main>
    <div class="wrap hero">
      <div class="heroGrid">
        <div class="heroCard">
          <div class="eyebrow">四択の次は、現場判断を鍛える</div>
          <h1>実践ケース100問で<br>“使える理解”へ。</h1>
          <p class="lead">正しい対応、不適切な対応、最初の一手、リスク、次に確認すべきことを混ぜたケーススタディです。解説と「自分の職場なら？」メモで、学習を実務へつなげます。</p>
          <div class="ctaRow">
            <a class="btn btnPrimary" href="#cases">ケースを解く</a>
            <button class="btn btnGhost" id="randomTen">ランダム10問</button>
            <button class="btn btnGhost" id="reviewWrong">間違い復習</button>
          </div>
        </div>
        <aside class="panel stats" aria-label="ケース統計">
          <div class="stat"><b>100</b><span>実践ケース</span></div>
          <div class="stat"><b>10</b><span>カテゴリ</span></div>
          <div class="stat"><b id="solvedCount">0</b><span>解答済み</span></div>
          <div class="stat"><b id="correctRate">0%</b><span>正答率</span></div>
          <div class="stat" style="grid-column:1/-1;"><b id="memoCount">0</b><span>自分用メモ</span></div>
        </aside>
      </div>
    </div>

    <section id="howto">
      <div class="wrap">
        <div class="sectionTitle"><h2>深く学ぶ流れ</h2><p class="muted">動画・四択の後に、現場判断へ進む</p></div>
        <div class="pathGrid">
          <div class="pathStep"><strong>1. 状況を読む</strong><span class="muted">部署・制約・情報状態を確認</span></div>
          <div class="pathStep"><strong>2. 問題タイプを見る</strong><span class="muted">適切/不適切/最初の一手/リスク/次の確認</span></div>
          <div class="pathStep"><strong>3. 解説で判断軸を確認</strong><span class="muted">なぜ他の選択肢が微妙かまで読む</span></div>
          <div class="pathStep"><strong>4. 自分の職場に置き換える</strong><span class="muted">メモ欄に実務適用を書き残す</span></div>
        </div>
      </div>
    </section>

    <section id="cases">
      <div class="wrap">
        <div class="sectionTitle"><h2>ケース一覧</h2><p class="muted" id="resultCount">100件</p></div>
        <div class="panel toolbar">
          <input id="search" type="search" placeholder="部署・課題・タグで検索">
          <select id="categoryFilter" aria-label="カテゴリ"><option value="all">すべてのカテゴリ</option></select>
          <select id="typeFilter" aria-label="問題タイプ"><option value="all">すべての問題タイプ</option></select>
          <select id="statusFilter" aria-label="状態"><option value="all">すべて</option><option value="unsolved">未解答</option><option value="correct">正解済み</option><option value="wrong">間違い</option><option value="memo">メモあり</option></select>
        </div>
        <div class="categoryChips" id="categoryChips"></div>
        <div class="grid" id="caseGrid" style="margin-top:16px;"></div>
      </div>
    </section>
  </main>
  <footer><div class="wrap">Generated: {generated_at} / Source: case_bank/data/cases.json / Type counts: {type_counts_json}</div></footer>
  <script>
    const CASES = {cases_json};
    const CATEGORIES = {categories_json};
    const TYPE_LABELS = {json.dumps(TYPE_LABELS, ensure_ascii=False)};
    const STORAGE_KEY = 'sio-ai-agent-strategist-case-bank-v1';
    const $ = (id) => document.getElementById(id);
    let state = loadState();
    let forcedIds = null;
    function loadState() {{ try {{ return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {{ answers: {{}}, memos: {{}} }}; }} catch (_) {{ return {{ answers: {{}}, memos: {{}} }}; }} }}
    function saveState() {{ localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); updateStats(); }}
    function escapeHtml(value) {{ return String(value).replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c])); }}
    function statusOf(c) {{ const a = state.answers[c.id]; if (!a) return 'unsolved'; return a.correct ? 'correct' : 'wrong'; }}
    function updateStats() {{ const answers = Object.values(state.answers); const solved = answers.length; const correct = answers.filter(a => a.correct).length; const memos = Object.values(state.memos).filter(v => String(v || '').trim()).length; $('solvedCount').textContent = solved; $('correctRate').textContent = solved ? `${{Math.round(correct / solved * 100)}}%` : '0%'; $('memoCount').textContent = memos; }}
    function initFilters() {{ CATEGORIES.forEach(cat => {{ const opt = document.createElement('option'); opt.value = cat; opt.textContent = cat; $('categoryFilter').appendChild(opt); }}); Object.entries(TYPE_LABELS).forEach(([value,label]) => {{ const opt = document.createElement('option'); opt.value = value; opt.textContent = label; $('typeFilter').appendChild(opt); }}); $('categoryChips').innerHTML = ['all', ...CATEGORIES].map(cat => `<button class="chip ${{cat === 'all' ? 'active' : ''}}" data-category="${{escapeHtml(cat)}}">${{cat === 'all' ? 'すべて' : escapeHtml(cat)}}</button>`).join(''); document.querySelectorAll('.chip').forEach(btn => btn.addEventListener('click', () => {{ forcedIds = null; $('categoryFilter').value = btn.dataset.category; document.querySelectorAll('.chip').forEach(b => b.classList.toggle('active', b === btn)); renderCases(); }})); }}
    function filteredCases() {{ const query = $('search').value.trim().toLowerCase(); const cat = $('categoryFilter').value; const type = $('typeFilter').value; const status = $('statusFilter').value; let list = CASES.filter(c => {{ const hay = `${{c.id}} ${{c.title}} ${{c.category}} ${{c.typeLabel}} ${{c.difficulty}} ${{c.scenario}} ${{c.question}} ${{c.tags.join(' ')}} ${{c.relatedUnits.join(' ')}}`.toLowerCase(); const st = statusOf(c); const memo = String(state.memos[c.id] || '').trim(); return (!forcedIds || forcedIds.has(c.id)) && (!query || hay.includes(query)) && (cat === 'all' || c.category === cat) && (type === 'all' || c.type === type) && (status === 'all' || status === st || (status === 'memo' && memo)); }}); return list; }}
    function renderCases() {{ const list = filteredCases(); $('resultCount').textContent = `${{list.length}}件 / 100件`; if (!list.length) {{ $('caseGrid').innerHTML = '<div class="panel empty">条件に合うケースがありません。</div>'; updateStats(); return; }} $('caseGrid').innerHTML = list.map(c => renderCase(c)).join(''); bindCaseEvents(); updateStats(); }}
    function renderCase(c) {{ const selected = state.answers[c.id]?.selectedIndex; const answered = Number.isInteger(selected); const correct = answered && selected === c.answerIndex; const memo = state.memos[c.id] || ''; return `<article class="caseCard" data-id="${{c.id}}"><div class="meta"><span class="badge">${{c.id}}</span><span class="badge">${{escapeHtml(c.category)}}</span><span class="badge typeBadge">${{escapeHtml(c.typeLabel)}}</span><span class="badge">${{escapeHtml(c.difficulty)}}</span><span class="badge">${{answered ? (correct ? '正解済み' : '間違い') : '未解答'}}</span></div><h3>${{escapeHtml(c.title)}}</h3><div class="scenario">${{escapeHtml(c.scenario)}}</div><strong>${{escapeHtml(c.question)}}</strong><div class="choices">${{c.choices.map((choice, i) => `<button class="choice ${{answered && i === c.answerIndex ? 'correct' : ''}} ${{answered && i === selected && i !== c.answerIndex ? 'wrong' : ''}}" data-id="${{c.id}}" data-index="${{i}}"><b>${{String.fromCharCode(65+i)}}.</b> ${{escapeHtml(choice)}}</button>`).join('')}}</div><div class="answerBox ${{answered ? 'open' : ''}}"><strong>${{answered ? (correct ? '正解' : '不正解') : ''}}：${{String.fromCharCode(65 + c.answerIndex)}} が正解</strong><p>${{escapeHtml(c.explanation)}}</p><details><summary>なぜ他の選択肢は微妙か</summary><ol class="whyList">${{c.whyOthers.map((w,i) => `<li><b>${{String.fromCharCode(65+i)}}.</b> ${{escapeHtml(w)}}</li>`).join('')}}</ol></details></div><div class="reflection"><strong>自分の職場なら？</strong><ul>${{c.reflectionPrompts.map(p => `<li>${{escapeHtml(p)}}</li>`).join('')}}</ul><textarea data-memo="${{c.id}}" placeholder="ここに自分用メモを残す">${{escapeHtml(memo)}}</textarea></div><div class="caseFooter"><button class="btn btnGhost resetOne" data-id="${{c.id}}">この問題をリセット</button><span class="badge">関連: ${{c.relatedUnits.map(escapeHtml).join(' / ')}}</span></div></article>`; }}
    function bindCaseEvents() {{ document.querySelectorAll('.choice').forEach(btn => btn.addEventListener('click', () => {{ const c = CASES.find(x => x.id === btn.dataset.id); const selected = Number(btn.dataset.index); state.answers[c.id] = {{ selectedIndex: selected, correct: selected === c.answerIndex, answeredAt: new Date().toISOString() }}; saveState(); renderCases(); }})); document.querySelectorAll('[data-memo]').forEach(area => area.addEventListener('input', () => {{ state.memos[area.dataset.memo] = area.value; saveState(); }})); document.querySelectorAll('.resetOne').forEach(btn => btn.addEventListener('click', () => {{ delete state.answers[btn.dataset.id]; saveState(); renderCases(); }})); }}
    $('search').addEventListener('input', () => {{ forcedIds = null; renderCases(); }}); $('categoryFilter').addEventListener('change', () => {{ forcedIds = null; document.querySelectorAll('.chip').forEach(b => b.classList.toggle('active', b.dataset.category === $('categoryFilter').value)); renderCases(); }}); $('typeFilter').addEventListener('change', () => {{ forcedIds = null; renderCases(); }}); $('statusFilter').addEventListener('change', () => {{ forcedIds = null; renderCases(); }});
    $('randomTen').addEventListener('click', () => {{ const shuffled = [...CASES].sort((a,b) => a.id.localeCompare(b.id)).sort(() => Math.random() - 0.5).slice(0,10); forcedIds = new Set(shuffled.map(c => c.id)); $('search').value=''; $('categoryFilter').value='all'; $('typeFilter').value='all'; $('statusFilter').value='all'; renderCases(); document.getElementById('cases').scrollIntoView({{ behavior:'smooth' }}); }});
    $('reviewWrong').addEventListener('click', () => {{ forcedIds = null; $('statusFilter').value='wrong'; renderCases(); document.getElementById('cases').scrollIntoView({{ behavior:'smooth' }}); }});
    initFilters(); renderCases();
  </script>
</body>
</html>
'''


def validate_cases(cases: list[dict]) -> list[str]:
    errors = []
    if len(cases) != 100:
        errors.append(f"expected 100 cases, got {len(cases)}")
    ids = [c.get("id") for c in cases]
    if len(ids) != len(set(ids)):
        errors.append("duplicate ids")
    cat_counts = Counter(c["category"] for c in cases)
    if sorted(cat_counts.values()) != [10] * 10:
        errors.append(f"category counts invalid: {dict(cat_counts)}")
    type_counts = Counter(c["type"] for c in cases)
    expected = {"choose_best": 40, "choose_wrong": 25, "choose_first_action": 15, "choose_highest_risk": 10, "choose_next_check": 10}
    if dict(type_counts) != expected:
        errors.append(f"type counts invalid: {dict(type_counts)}")
    secret_re = re.compile(r"(sk-[A-Za-z0-9]{12,}|AIza[0-9A-Za-z_-]{20,}|ghp_[0-9A-Za-z]{20,}|xox[baprs]-[0-9A-Za-z-]{10,})")
    for c in cases:
        if len(c.get("choices", [])) != 4:
            errors.append(f"{c.get('id')} choices != 4")
        if len(c.get("whyOthers", [])) != 4:
            errors.append(f"{c.get('id')} whyOthers != 4")
        if not isinstance(c.get("answerIndex"), int) or not 0 <= c["answerIndex"] <= 3:
            errors.append(f"{c.get('id')} invalid answerIndex")
        if len(c.get("reflectionPrompts", [])) != 3:
            errors.append(f"{c.get('id')} reflectionPrompts != 3")
        blob = json.dumps(c, ensure_ascii=False)
        if secret_re.search(blob):
            errors.append(f"{c.get('id')} secret-like token")
    return errors


def write_report(cases: list[dict], errors: list[str]) -> None:
    cat_counts = Counter(c["category"] for c in cases)
    type_counts = Counter(c["type"] for c in cases)
    now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M JST")
    report = [
        "# [[実践ケース問題100選]] QA Report",
        "",
        f"- 生成日時: {now}",
        "- 対象: `case_bank/index.html` / `case_bank/data/cases.json`",
        f"- ケース数: {len(cases)}",
        f"- カテゴリ数: {len(cat_counts)}",
        f"- 検証エラー: {len(errors)}",
        "",
        "## カテゴリ件数",
    ]
    for k, v in cat_counts.items():
        report.append(f"- [[{k}]]: {v}")
    report += ["", "## 問題タイプ件数"]
    for k, v in type_counts.items():
        report.append(f"- `{k}` / {TYPE_LABELS[k]}: {v}")
    report += ["", "## 検証結果", "```text"]
    report += [f"CASE_COUNT {len(cases)}", f"CATEGORY_COUNT {len(cat_counts)}", f"ERROR_COUNT {len(errors)}"]
    if errors:
        report += ["ERRORS"] + errors
    report += ["```", "", "## 証跡", "- 生成スクリプト: `case_bank/scripts/build_case_bank.py`", "- データ: `case_bank/data/cases.json`", "- HTML: `case_bank/index.html`", "", "関連: [[AIエージェント・ストラテジスト]] / [[eラーニング教材]] / [[ケース問題100選]]"]
    QA_REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    cases = build_cases()
    errors = validate_cases(cases)
    CASES_JSON.write_text(json.dumps(cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    INDEX_HTML.write_text(render_html(cases), encoding="utf-8")
    write_report(cases, errors)
    print(f"CASE_COUNT {len(cases)}")
    print(f"CATEGORY_COUNT {len(Counter(c['category'] for c in cases))}")
    print(f"TYPE_COUNTS {dict(Counter(c['type'] for c in cases))}")
    print(f"ERROR_COUNT {len(errors)}")
    if errors:
        raise SystemExit("; ".join(errors[:5]))

if __name__ == "__main__":
    main()
