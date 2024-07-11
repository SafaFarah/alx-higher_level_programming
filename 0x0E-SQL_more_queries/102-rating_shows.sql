-- list shows by their rating sum
SELECT tv_shows.title, SUM(ratings.rating) AS rating
FROM tv_shows
LEFT JOIN ratings ON tv_shows.id = ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
