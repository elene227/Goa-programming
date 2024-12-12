



username = input("Please enter your name: ")
choice = input("How would you like to enter your name? Upper, lower, or capitalize?: ")


name = []

if choice == "upper":
    name.append(username.upper())
elif choice == "capitalize":
    name.append(username.capitalize())
else:
    name.append(username.lower())


print(name)





