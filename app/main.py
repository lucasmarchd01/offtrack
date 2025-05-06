from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Song(BaseModel):
    name: str
    bpm: float
    genres: List[str]
    artists: List[str]

def sort_by_bpm(songs: List[Song], descending=True) -> List[dict]:
    return sorted([s.dict() for s in songs], key=lambda s: s["bpm"], reverse=descending)


@app.post("/sort_playlist")
async def sort_playlist(songs: List[Song]):
    if not songs:
        raise HTTPException(status_code=400, detail="No songs provided.")
    
    sorted_songs = sort_by_bpm(songs)
    return {"sorted_playlist": sorted_songs}
