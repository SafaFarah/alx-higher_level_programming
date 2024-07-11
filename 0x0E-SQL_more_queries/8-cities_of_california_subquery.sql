-- list all cities of California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
