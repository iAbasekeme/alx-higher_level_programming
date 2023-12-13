-- A script that lists all records of the table
SELECT score, name
FROM second_table
GROUP BY score
ORDER BY name DESC;