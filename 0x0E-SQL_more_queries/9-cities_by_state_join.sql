-- A script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.id
FROM hbtn_0d_usa
ORDER BY cities.id ASC;