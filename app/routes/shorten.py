from fastapi import APIRouter
from app.schemas import ShortenURLRequest, ShortenURLResponse
from app.services.short_code import generate_short_code
from app.database import SessionLocal
from app.models import URL

router = APIRouter(prefix="/api/v1")

@router.post("/shorten", response_model=ShortenURLResponse)
def shorten_url(request: ShortenURLRequest):
    db = SessionLocal()

    short_code = generate_short_code()

    url = URL(
        long_url=request.long_url,
        short_code=short_code
    )

    db.add(url)
    db.commit()
    db.close()

    short_url = f"http://localhost:8000/{short_code}"
    return ShortenURLResponse(short_url=short_url)
