SELECT AVG(energy) FROM songs
JOIN artists ON songs.artist_id = artists_id
WHERE artists.name = 'DRAKE';
