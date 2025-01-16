# GC-System


このガイドでは、Docker を使用してプロジェクトをセットアップおよび実行する手順を説明します。MySQL の設定、バックエンドサーバーの起動、初期データでのデータベースシード、WebSocket サーバーの起動方法についても解説します。

## 前提条件

プロジェクトを始める前に、以下のソフトウェアがマシンにインストールされていることを確認してください：

- **Docker** と **Docker Compose**：Docker Desktop（Docker Compose を含む）をインストールしてください。公式ウェブサイトからダウンロードできます: https://www.docker.com/get-started

- **Python 3.12**：このプロジェクトでは Python バージョン 3.12 を使用します。事前にインストールされていることを確認してください。


## 実行方法

### 1. プロジェクトを cloneする
```sh
# HTTPS
git clone https://oceanic-constellations@dev.azure.com/oceanic-constellations/GC-Frontend-Dev/_git/GC-Backend-Dev

# SSH
git clone git@ssh.dev.azure.com:v3/oceanic-constellations/GC-Frontend-Dev/GC-Backend-Dev

```


* プロジェクトディレクトリは以下のような構造である必要があります：


<pre>

GC-Backend-Dev

├─ Dockerfile
├─ README.md
├─ app
│  ├─ api
│  │  ├─ deps.py
│  │  └─ v1
│  │     ├─ auth.py
│  │     └─ users.py
│  ├─ config.py
│  ├─ core
│  │  ├─ config.py
│  │  └─ security.py
│  ├─ database.py
│  ├─ main.py
│  ├─ models.py
│  ├─ run_seeds.py
│  ├─ schemas
│  │  ├─ auth.py
│  │  ├─ ship.py
│  │  └─ user.py
│  └─ websocket_server.py
├─ docker-compose.yml
├─ requirements.txt
├─ .env.templ
├─ scripts
│  ├─ update_communication_data.py
│  ├─ update_mission_data.py
│  ├─ update_propulsion_data.py
│  ├─ update_system_data.py
│  └─ update_telemetry_data.py
└─ seed
   ├─ seed_communication.py
   ├─ seed_mission.py
   ├─ seed_propulsion.py
   ├─ seed_registry.py
   ├─ seed_ships.py
   ├─ seed_system.py
   ├─ seed_telemetry.py
   └─ seed_users.py

</pre>

### 2. 環境変数ファイルの生成

```sh

mv .env.templ .env

```

### 3. docker-compose を使って実行

```sh

docker compose up --build

```

サービスを停止するには

```sh

docker compose down

```

### 4. 仮想環境を作成する（任意だが推奨）
プロジェクト専用の環境を作成することで、依存関係を管理しやすくなります:

```sh
   
   python -m venv .venv
   source env/bin/activate    # Linux/Macの場合
   env\Scripts\activate       # Windowsの場合

```

### 5. シードファイルから初期仮想データを入力する

* すべてのテーブルのデータを同時に入力するには...
```sh

   python -m app.run_seeds

```
* 必要に応じて個別に入力することもできます。
```sh
   # cmdの入力例
   python -m seed.seed_communication

   # 
   python -m seed.seed_mission
 
 ....

```

### 6. データベースの値を更新するためのスクリプトの実行

```sh

   python -m scripts.update_communication_data
   python -m scripts.update_mission_data
   python -m scripts.update_propulsion
   python -m scripts.update_system_data
   python -m scripts.update_telemetry_data

```

* 必要に応じて1つまたは複数個を同時に実行させることができます。


## FastAPI アプリにアクセス
* ブラウザで以下にアクセスしてください：
   http://localhost:8000

   自動生成された API ドキュメントを見るには：
   Swagger UI: http://localhost:8000/docs
   ReDoc: http://localhost:8000/redoc

* WebSocketサーバーのテスト方法
   ローカルでWebSocketサーバーをテストするには:

   サーバーが実行中であることを確認します（docker compose up または uvicorn コマンドを使用）。
   WebSocketクライアントを使用して ws://localhost:9000 に接続します。