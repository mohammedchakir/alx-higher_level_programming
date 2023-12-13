-- This script uses the 'hbtn_0d_tvshows' database to list all genres not linked to the show 'Dexter'
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name
-- The script uses a maximum of two SELECT statements
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter')
ORDER BY name;
