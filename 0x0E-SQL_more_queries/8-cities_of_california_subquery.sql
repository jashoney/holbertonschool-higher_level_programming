-- lists of all the Californian cites in our db
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
