from fastapi import FastAPI
from app.routes.shorten import router as shorten_router
from app.database import Base, engine
from app.models import URL

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(shorten_router)

@app.get("/")
def home():
    return {"message": "URL Shortener is running"}
