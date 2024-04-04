import fastapi as FastAPI
from fastapi import status
from models import SongRequest, SongInfo
from spotify_client import search_song as search
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI.FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

in_memory_db: list[SongInfo] = []


@app.post("/song")
def create_song(new_song: SongRequest) -> SongInfo:
    # Return the song info
    pass


@app.get("/song")
def read_songs() -> list[SongInfo]:
    # Return all the songs
    pass

@app.patch("/song/{song_id}")
def update_favorite_song(song_id: str, isFav:bool) -> SongInfo:
    # Quitar de favoritos
    pass

@app.delete("/song/{song_id}")
def delete_favorite_song(song_id: str) -> FastAPI.Response:
    # Delete from the list
    pass

