-- COMMENT
SELECT name, id
FROM states
WHERE states.id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
