def liters_100km_to_miles_gallon(liters):
    # 1. How many miles are in 100 kilometers?
    # (100 km / 1.609344 km per mile)
    miles = 100 / 1.609344
    
    # 2. How many gallons is the given amount of liters?
    gallons = liters / 3.785411784
    
    # 3. Miles per gallon is just miles divided by gallons!
    return miles / gallons


def miles_gallon_to_liters_100km(miles):
    # 1. How many kilometers are in the given amount of miles?
    km = miles * 1.609344
    
    # 2. We know this distance was traveled using exactly 1 gallon (3.785411784 liters)
    liters = 3.785411784
    
    # 3. If it takes 'x' liters to travel 'y' km, we divide them to find liters per 1 km.
    # Then we multiply by 100 to find liters per 100 km.
    return (liters / km) * 100


# --- The PCEP Test Suite ---
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))