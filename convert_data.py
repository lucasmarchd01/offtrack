import ast
import json
import csv

def parse_songs(file_path):
    songs = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                title, bpm, genres, artists = ast.literal_eval(line)
                song = {
                    "title": title,
                    "bpm": float(bpm),
                    "genres": genres,
                    "artists": artists
                }
                songs.append(song)
            except Exception as e:
                print(f"Error parsing line: {line}\n{e}")
    return songs

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["title", "bpm", "genres", "artists"])
        writer.writeheader()
        for song in data:
            writer.writerow({
                "title": song["title"],
                "bpm": song["bpm"],
                "genres": ', '.join(song["genres"]),
                "artists": ', '.join(song["artists"])
            })

# Run the whole process
if __name__ == "__main__":
    songs = parse_songs("data/test_input.txt")
    save_to_json(songs, "songs.json")
    save_to_csv(songs, "songs.csv")
    print("Files saved: songs.json and songs.csv")
