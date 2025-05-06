import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import ast

# Load the input data from the text file
def load_data(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            # Parse each line as a tuple
            data.append(ast.literal_eval(line.strip()))
    return data

# Load data from input.txt
input_file = "/Users/lucasmarch/Projects/offtrack/data/input.txt"
input_data = load_data(input_file)

# Convert the data into a DataFrame
df = pd.DataFrame(input_data, columns=["Song Name", "BPM", "Genres", "Artists"])

# Flatten the genres for analysis
all_genres = [genre for genres in df["Genres"] for genre in genres]

# Count genre occurrences
genre_counts = Counter(all_genres)

# Visualization 1: Genre Distribution
plt.figure(figsize=(10, 6))
plt.bar(genre_counts.keys(), genre_counts.values(), color='skyblue')
plt.title("Genre Distribution")
plt.xlabel("Genres")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualization 2: BPM Distribution
plt.figure(figsize=(10, 6))
plt.hist(df["BPM"], bins=10, color='orange', edgecolor='black')
plt.title("BPM Distribution")
plt.xlabel("BPM")
plt.ylabel("Number of Songs")
plt.tight_layout()
plt.show()

# Visualization 3: Top Artists by Song Count
artist_counts = Counter([artist for artists in df["Artists"] for artist in artists])
top_artists = artist_counts.most_common(10)

plt.figure(figsize=(10, 6))
plt.bar([artist[0] for artist in top_artists], [artist[1] for artist in top_artists], color='green')
plt.title("Top Artists by Song Count")
plt.xlabel("Artists")
plt.ylabel("Number of Songs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 4: BPM vs Genre Count
df["Genre Count"] = df["Genres"].apply(len)
plt.figure(figsize=(10, 6))
plt.scatter(df["BPM"], df["Genre Count"], color='purple')
plt.title("BPM vs Genre Count")
plt.xlabel("BPM")
plt.ylabel("Number of Genres")
plt.tight_layout()
plt.show()