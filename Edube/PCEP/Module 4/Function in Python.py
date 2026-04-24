# Function with Parameter
def get_name (fname, lname):
    print("The name of the person is",fname,lname)

get_name("Vijay","Mallayya")

# Function with ordered Parameter
def get_name2(fname = "Roshan",lname = "Kumar"):
    print("The second person name is",fname,lname)
    
get_name2()
get_name2("Harshal","Patel")