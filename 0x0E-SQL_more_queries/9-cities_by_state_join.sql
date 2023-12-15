-- A script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities
JOIN states
ON state.id = cities.id
ORDER BY cities.id ASC;