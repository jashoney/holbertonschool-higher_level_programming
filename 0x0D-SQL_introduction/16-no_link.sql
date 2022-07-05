-- list scores from second_table scores and the number of times they occur grouped by score in desc socre order
SELECT score, name FROM second_table WHERE name != "" AND name IS NOT NULL ORDER BY score DESC;
