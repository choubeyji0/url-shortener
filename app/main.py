from fastapi import FastAPI
from app.routes.shorten import router as shorten_router
from app.routes.redirect import router as redirect_router
from app.database import Base, engine

app = FastAPI(title="URL Shortener")

# Create all tables if they do not exist
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(shorten_router)
app.include_router(redirect_router)

@app.get("/")
def home():
    return {"message": "URL Shortener is running"}
