-- display all record of the table second_table having a name value in my MySQL server.
-- Doc the score in a descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
