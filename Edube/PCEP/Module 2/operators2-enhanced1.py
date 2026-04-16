hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Step 1: Convert the start time entirely into minutes and add the duration
total_minutes = (hour * 60) + mins + dura

# Step 2: Extract the final hour 
# Find total hours (total_minutes // 60), then format to a 24-hour clock (% 24)
final_hour = (total_minutes // 60) % 24

# Step 3: Extract the leftover minutes
final_min = total_minutes % 60

# Output using an f-string for cleaner formatting
print(f"{final_hour}:{final_min}")