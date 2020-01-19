import lyricsgenius
genius = lyricsgenius.Genius("ZdBzOQOetc6sZnPU2F3eKnUIyAyrGvgE7aFnUICXkvnJO4CGMxZB7kirhWn59SUy")
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
song = genius.search_song("To You", artist.name)
print(song.lyrics)