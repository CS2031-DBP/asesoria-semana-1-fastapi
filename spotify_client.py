import requests
import base64

from models import SongRequest, SongInfo

_CLIENT_ID = "d1a859ed941147b0854d70aa0333091e"
_CLIENT_SECRET = "aa312f507b684497853c6a7f6454e9be"

auth_str = f"{_CLIENT_ID}:{_CLIENT_SECRET}"
auth_b64 = base64.b64encode(auth_str.encode()).decode()

auth_options = {
    "url": "https://accounts.spotify.com/api/token",
    "data": {"grant_type": "client_credentials"},
    "headers": {"Authorization": f"Basic {auth_b64}"},
}


_ACCES_TOKEN = ""


def get_access_token() -> str:
    global _ACCES_TOKEN
    if _ACCES_TOKEN:
        return _ACCES_TOKEN

    response = requests.post(**auth_options)
    response.raise_for_status()
    _ACCES_TOKEN = response.json()["access_token"]
    return _ACCES_TOKEN


def search_song(song: SongRequest) -> SongInfo:
    access_token = get_access_token()
    search_options = {
        "url": "https://api.spotify.com/v1/search",
        "params": {
            "q": f"track:{song.name} artist:{song.artist}",
            "type": "track",
            "limit": 1,
        },
        "headers": {"Authorization": f"Bearer {access_token}"},
    }
    response = requests.get(**search_options)
    response.raise_for_status()

    response = response.json()["tracks"]["items"][0]

    song_info: SongInfo = {
        "preview_url": response["preview_url"],
        "external_url": response["external_urls"]["spotify"],
        "img_url": response["album"]["images"][0]["url"],
        "id": response["id"],
        "name": response["name"],
        "artist": response["artists"][0]["name"],
    }

    return song_info
