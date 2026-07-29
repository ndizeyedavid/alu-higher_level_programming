-- Lists score and name from second_table, excluding rows with no name, ordered by score desc
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;