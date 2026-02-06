# Default Parameters & Arguments 

# def get_details_chennai (name, place = "Chennai", age):  # ERROR - Default argument at the end after other arguments
def get_details_chennai (name, age,place = "Chennai"):     
    print ("The customer name is",name)
    print("The customer resides at",place)
    print("The age of the customer is",age)

get_details_chennai("Rahul",23)  # Passing Arguments 

get_details_chennai(age = 23,place = "Bangalore",name ="Rahul")  # Overriding Default Argument