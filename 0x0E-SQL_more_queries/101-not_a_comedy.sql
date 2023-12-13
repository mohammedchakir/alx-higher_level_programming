-- This script lists all shows without the genre 'Comedy' in the database 'hbtn_0d_tvshows'
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
-- The script uses a maximum of two SELECT statements
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy')
ORDER BY title;
