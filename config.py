import os
from dotenv import main

main.load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
DB_URL = (f"postgresql+asyncpg://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@"
            f"{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_NAME")}")