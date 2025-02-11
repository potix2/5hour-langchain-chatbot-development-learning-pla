# 会話の文脈管理 – LangGraphによる実装

このプロジェクトは、LangGraphを使用して会話の文脈を管理するチャットボットを実装したものです。

## 技術的な特徴

### StateGraphによる会話管理
- グラフベースの会話フロー制御
- 状態管理による文脈の保持
- チェックポイントによる会話履歴の保存

### 実装の特徴
1. 状態管理
   - `State`クラスによるメッセージ履歴の管理
   - SystemMessage、HumanMessage、AIMessageの構造化

2. グラフ構造
   - `chatbot_node`による応答生成
   - START→chatbot→ENDの単純な会話フロー
   - `MemorySaver`によるチェックポイント管理

3. インタラクション
   - タイピングエフェクトによる自然な応答表示
   - カラフルなコンソール出力
   - 日本語での対話

## セットアップ

### 1. 仮想環境の作成とアクティベート
```bash
# 仮想環境の作成
python -m venv venv
source venv/bin/activate  # Unix系
```

### 2. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

### 3. 環境変数の設定
1. `.env.template`を`.env`にコピー
2. `.env`ファイルにOpenAI APIキーを設定

## 実行方法
```bash
python main.py
```

## 使用例

```
You: こんにちは
Assistant: こんにちは！何かお手伝いできることはありますか？

You: 今日の天気について教えてください
Assistant: 申し訳ありませんが、私はリアルタイムの天気情報にアクセスすることができません。
天気予報を知りたい場合は、天気予報サイトやアプリをご確認いただくことをお勧めします。
代わりに、他にお手伝いできることはありますか？
```

## 技術スタック

- LangChain
- LangGraph
- OpenAI GPT-4
- Python 3.12
- Colorama（コンソール出力の装飾）

## 注意事項

- OpenAI APIキーが必要です
- インターネット接続が必要です
- APIの使用には料金が発生する可能性があります 