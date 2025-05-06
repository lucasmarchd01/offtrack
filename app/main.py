from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Song(BaseModel):
    title: str
    bpm: float
    genres: List[str]
    artists: List[str]

from collections import defaultdict, Counter

def generate_vibe_playlists(songs: List[Song]) -> dict:
    songs = [s.dict() for s in songs]

    vibes = {
        "high_energy": [],
        "chill": [],
        "pop": [],
        "house_edm": [],
        "by_artist": defaultdict(list)
    }

    for song in songs:
        bpm = song["bpm"]
        genres = [g.lower() for g in song["genres"]]
        artists = song["artists"]

        if bpm > 115:
            vibes["high_energy"].append(song)
        if bpm < 95:
            vibes["chill"].append(song)
        if any("pop" in g for g in genres):
            vibes["pop"].append(song)
        if any(g in ["edm", "house", "electro house", "progressive house", "deep house"] for g in genres):
            vibes["house_edm"].append(song)

        for artist in artists:
            vibes["by_artist"][artist].append(song)

    # Optional: return only the top N artist-based playlists
    top_artists = Counter({artist: len(songs) for artist, songs in vibes["by_artist"].items()}).most_common(3)
    artist_playlists = {f"artist_{artist}": vibes["by_artist"][artist] for artist, _ in top_artists}

    # Combine everything
    final_playlists = {
        "high_energy": sorted(vibes["high_energy"], key=lambda s: s["bpm"], reverse=True),
        "chill": sorted(vibes["chill"], key=lambda s: s["bpm"]),
        "pop": vibes["pop"],
        "house_edm": vibes["house_edm"]
    }
    final_playlists.update(artist_playlists)

    return final_playlists


def sort_by_bpm(songs: List[Song], descending=True) -> List[dict]:
    return sorted([s.dict() for s in songs], key=lambda s: s["bpm"], reverse=descending)


@app.post("/sort_playlist")
async def sort_playlist(songs: List[Song]):
    if not songs:
        raise HTTPException(status_code=400, detail="No songs provided.")
    
    sorted_songs = generate_vibe_playlists(songs)
    return {"sorted_playlist": sorted_songs}
