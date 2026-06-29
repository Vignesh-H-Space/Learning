class Counter:
    count = 0  # Class Variable

c1 = Counter()
c2 = Counter()

# Modifying through the instance
c1.count += 1

# Modifying through the Master Blueprint
Counter.count += 5

