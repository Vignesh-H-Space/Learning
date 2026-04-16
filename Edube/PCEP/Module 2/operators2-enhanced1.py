hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Step 1: Convert the start time entirely into minutes and add the duration
total_minutes = (hour * 60) + mins + dura

