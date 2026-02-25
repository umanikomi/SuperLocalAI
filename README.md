# RAG&FAISS&SQLite

ローカルLLMとベクトルデータベースを組み合わせた、長期記憶を持つAIアシスタントのプロトタイプだよ☆

## 概要
このプロジェクトは、LM StudioなどのローカルLLMサーバーと連携して、過去の会話内容を「記憶」として保持・活用するAIアプリだよ。
会話の内容をベクトルデータに変換して保存することで、時間が経っても関連する過去の出来事を思い出して答えてくれるんだ！マジ賢い！

## ファイル構成
```text
D:\git\superai\SuperLocalAI.No1\
├── app/
│   ├── config.py       # モデル名やDBのパスとかの設定
│   ├── llm.py          # ローカルLLM（LM Studio）との通信
│   ├── main.py         # アプリのメインループ
│   └── memory.py       # ベクトル検索(FAISS)とSQLiteによる記憶管理
├── data/               # 記憶データ（DBとインデックス）が保存される場所
├── requirements.txt    # 必要なライブラリたち
├── setup.bat           # 仮想環境構築とインストールを一括でやるやつ
└── start.bat           # アプリをサクッと起動するやつ
```

## 仕組み（ソース解説）
- **記憶の保存 (`app/memory.py`)**:
    - SQLiteで会話テキストを保存。
    - `sentence-transformers` で文章をベクトル化。
    - `FAISS` を使って高速な類似度検索ができるようにインデックスを管理してるよ！
- **記憶の活用 (`app/llm.py`)**:
    - ユーザーが質問すると、まず過去の記憶から関連するメッセージを検索！
    - 検索結果をコンテキストとしてプロンプトに埋め込んで、LLMに投げる仕組み（RAG）だよ。
- **メイン処理 (`app/main.py`)**:
    - シンプルな対話ループ。入力した内容は即座に記憶に刻まれるよ！

## セットアップ
1. `setup.bat` を実行して、必要な環境を整えるよ。
2. LM Studioを起動して、サーバーを `http://localhost:1234` で立てておいてね！
3. `start.bat` を叩けば、AIとの会話がスタートするよ☆

## 必要な技術
- Python 3.x
- sentence-transformers (ベクトル化)
- FAISS (高速ベクトル検索)
- SQLite (データ保存)
- OpenAI Python SDK (LLM通信)


