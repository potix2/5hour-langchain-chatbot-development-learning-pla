# LangChain Tutorial Project

シンプルなLangChainチャットボットのプロジェクトです。

## セットアップ

### 1. 仮想環境の作成とアクティベート

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境のアクティベート
# Windows の場合:
venv\Scripts\activate
# macOS/Linux の場合:
source venv/bin/activate
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