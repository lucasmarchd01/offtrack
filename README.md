🎛 Logic Breakdown

    Input: A list of songs, each with:

        name

        bpm

        genres (list of strings)

        artists (list of strings)

    Vibe Categories:

        High Energy: Songs with BPM > 115, sorted descending by BPM.

        Chill: Songs with BPM < 95, sorted ascending by BPM.

        Pop: Songs where any genre contains "pop".

        House/EDM: Songs with genres like "edm", "house", or "electro house".

        By Artist: Songs grouped by the most frequent artists in the input.

    Processing:

        Iterate over all songs and assign each to one or more vibe categories based on its BPM, genre tags, or associated artists.

        Sort playlists where appropriate (e.g., energy-based playlists are sorted by BPM).

        Select the top 3 most frequent artists and generate dedicated artist-centric playlists.

    Output: A dictionary with keys like "high_energy", "chill", "pop", "house_edm", and "artist_Tate McRae", each containing a list of songs matching that vibe.