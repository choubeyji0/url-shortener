import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/url_shortener"
)
