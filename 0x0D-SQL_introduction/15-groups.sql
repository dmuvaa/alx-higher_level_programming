-- mumber by score
SELECT score,
COUNT(*) as `number`
FROM second_table
GROUP BY score
ORDER BY score DESC;
