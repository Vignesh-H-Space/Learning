username = input("Enter username: ")

if username[0].isalpha() and username.replace("_", "").isalnum() and 6 <= len(username) <= 15:
    print("Valid Username")
else:
    print("Invalid Username")