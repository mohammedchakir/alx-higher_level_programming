-- This script lists all Comedy shows in the database 'hbtn_0d_tvshows'
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
-- The script uses only one SELECT statement
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
