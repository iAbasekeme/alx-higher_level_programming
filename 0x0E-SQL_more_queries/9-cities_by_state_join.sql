-- A script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, cities.states.id
FROM cities
ORDER BY cities.id ASC;