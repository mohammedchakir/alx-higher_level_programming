-- This script lists all shows in the database 'hbtn_0d_tvshows'
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Shows without a genre will display NULL for genre_id
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- The script uses only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
