-- This SQL script displays the maximum temperature of each state, ordered by state name.
SELECT state, MAX(temperature) AS max_temp
FROM temperature_data -- Replace 'temperature_data' with the actual table name
GROUP BY state
ORDER BY state;
