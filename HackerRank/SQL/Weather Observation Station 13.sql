-- Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345 . Truncate your answer to  decimal places.

SELECT ROUND(SUM(Lat_N), 4)
FROM STATION
WHERE Lat_N > 38.7880 AND Lat_N < 137.2345;