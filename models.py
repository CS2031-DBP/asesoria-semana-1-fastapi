from pydantic import BaseModel

class SongRequest(BaseModel):
    name: str
    artist: str
    isFav: bool = False

class SongInfo(BaseModel):
    preview_url: str | None
    external_url: str
    img_url: str
    id: str
    name: str
    artist: str
    isFav: bool = False

