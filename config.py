from dotenv import load_dotenv
import os

# .env 파일을 읽어서 환경변수로 등록
load_dotenv()

# 예시: 환경변수 꺼내기
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")