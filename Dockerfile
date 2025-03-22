#ベースイメージ
FROM python:3.10

#作業ディレクトリを作成
WORKDIR /app

# 必要なライブラリをコピー
COPY requirements.txt .

# ライブラリインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコードをコピー
COPY . .

CMD ["python", "main.py"]