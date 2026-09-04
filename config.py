import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://qae-assignment-tau.vercel.app"
USER_ID = os.getenv("USER_ID")

if not USER_ID:
    raise RuntimeError("USER_ID environment variable is not set")