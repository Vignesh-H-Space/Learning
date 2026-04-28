def is_year_leap(year):
    if year % 4 !=0 or year % 100 == 0 and year % 400 != 0:
        return False
    else :
        return True
        
def days_in_month(year, month):
    # Optional but good practice: catch invalid months
    if month < 1 or month > 12:
        return None
        
    # We put a 0 at the start so the indexes match the month numbers perfectly!
    # Index:       0   1   2   3   4   5   6   7   8   9  10  11  12
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if it's the one single exception (February in a leap year)
    if month == 2 and is_year_leap(year):
        return 29
        
    # For every other month, just look up the answer in the list!
    return month_days[month]

def day_of_year(year, month, day):

    year_cal = year % 100
    year_cal += int(year_cal / 4 )
    
    month_list  = [0,1,4,4,0,2,5,0,3,6,1,4,6]
    
    month_val = month_list[month]
    
    cent = int(year / 100 )
    cent %= 4
    
    cent_list = [6,4,2,0]
    cent_val = cent_list[cent]
    
    total = year_cal + month_val + cent_val + day
    
    total %= 7
    
    week_list = ["None","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    if is_year_leap(year) and month < 3:
        total -=1
    
    return week_list[total]

print(day_of_year(2024, 1, 1))