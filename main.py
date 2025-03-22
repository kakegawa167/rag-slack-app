import os
import openai
import chromadb
import mysql.connector
from slack_sdk import WebClient
from dotenv import load_dotenv
import time

print("⏳ DB起動を待っています...")
time.sleep(5)  # 5秒待つ(DBの接続待ち。必要に応じて長くする)

load_dotenv()

# OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Slack
slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

# MySQL
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB")
)

# ChromaDB
chroma_client = chromadb.Client()

print("✅ 全ての接続が成功しました！")
