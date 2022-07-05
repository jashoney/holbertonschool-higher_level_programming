-- list scores from second_table scores and the number of times they occur grouped by score in desc socre order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
