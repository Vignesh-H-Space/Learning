# Variable Length Argument

# def get_details_chennai (name, place = "Chennai", age):  # ERROR - Default argument at the end after other arguments
def get_details_chennai (name,place = "Chennai",*age):     
    print ("The customer name is",name)
    print("The customer resides at",place)
    print("The age of the customer is",age)

get_details_chennai("Rahul",23,15.5,9)  # Passing Arguments but Chennai as default is not accepted 

get_details_chennai("Kohli","Delhi",32,53,67.4)

# get_details_chennai(place = "Bangalore",name ="Rahul",age = 56,652,21)  # ERROR - Because positional argument follows keyword argument