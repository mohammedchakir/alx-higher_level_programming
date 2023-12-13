-- This script lists all genres from 'hbtn_0d_tvshows' and displays the number of shows linked to each
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- Genres without any shows linked are not displayed
-- Results are sorted in descending order by the number of shows linked
-- The script uses only one SELECT statement
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;

