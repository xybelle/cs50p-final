SELECT AVG(energy) as ave_energy FROM songs
WHERE artist_id = (
    SELECT id FROM artists
    WHERE name = 'DRAKE'
);
