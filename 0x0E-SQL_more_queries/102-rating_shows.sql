-- This script lists all shows from 'hbtn_0d_tvshows_rate' by their rating
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating
-- The script uses only one SELECT statement
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
