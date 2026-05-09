import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
QASE_TOKEN = os.getenv("QASE_TOKEN")