-- COMMENT
SELECT cities.id, cities.name, states.name
FROM cities
JOIN ON cities.state_id = states.id
