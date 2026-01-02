from pydantic import BaseModel, HttpUrl

class ShortenURLRequest(BaseModel):
    long_url: HttpUrl

class ShortenURLResponse(BaseModel):
    short_url: str
  
