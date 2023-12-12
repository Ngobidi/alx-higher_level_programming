-- display the num of record with the same score in the table second_table in my MySQL server.
-- document the count in a descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
