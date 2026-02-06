# Positional Arguments in Function

def get_details (name, place, age):  # Parameters 
    print ("The customer name is",name)
    print("The customer resides at",place)
    print("The age of the customer is",age)

get_details("Rahul","Chennai",23)  # Passing Arguments 

# get_details(23,"Chennai","Rahul") - ERROR - Due to wrong order 

get_details(age = 23,place = "Chennai",name ="Rahul")  # Positional Arguments