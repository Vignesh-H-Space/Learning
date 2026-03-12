-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION.
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('a','i','e','o','u');