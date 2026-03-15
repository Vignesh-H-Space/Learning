-- Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to 4 decimal places.

SELECT Round(min(Lat_N),4) FROM station where Lat_N>38.7780 ;