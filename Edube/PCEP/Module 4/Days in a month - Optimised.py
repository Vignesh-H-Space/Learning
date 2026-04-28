def is_year_leap(year):
    if year % 4 !=0 or year % 100 == 0 and year % 400 != 0:
        return False
    else :
        return True

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
        
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    

    if month == 2 and is_year_leap(year):
        return 29
        
    return month_days[month]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
 