import json

def load_songs(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def sort_by_bpm(songs, descending=False):
    return sorted(songs, key=lambda song: song["bpm"], reverse=descending)

def save_sorted_playlist(songs, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(songs, f, indent=2)

if __name__ == "__main__":
    songs = load_songs("songs.json")

    # Sort by energy (bpm), set descending=True for high to low energy
    sorted_songs = sort_by_bpm(songs, descending=True)

    save_sorted_playlist(sorted_songs, "sorted_by_energy.json")

    print("Playlist sorted by BPM and saved to 'sorted_by_energy.json'")
