## 環境変数（.env）の設定内容

このアプリでは以下の環境変数が必要です。  
ルートに `.env` ファイルを作成して設定してください。  
`.env.example` にサンプルを用意していますので、コピーして編集しても OK です。

```env
OPENAI_API_KEY=sk-xxx            # OpenAIのAPIキー
SLACK_BOT_TOKEN=xoxb-xxx         # Slack Botのトークン
SLACK_SIGNING_SECRET=xxx         # Slack署名検証用シークレット
MYSQL_HOST=xxx                   # MySQLホスト（Docker内サービス名）
MYSQL_USER=xxx                   # MySQLユーザー名
MYSQL_PASSWORD=xxx               # MySQLパスワード
MYSQL_DB=xxx                     # 使用するデータベース名
```
