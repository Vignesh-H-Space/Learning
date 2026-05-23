username = input("Enter username: ")

if username[0].isalpha() and username.replace("_", "").isalnum() :
    print("Valid Username")
else:
    print("Invalid Username")