my_favorite_number = ("0")
user_number = str(input("please enter your favorite number here: "))

if user_number == my_favorite_number:
    print("perfect!")
elif user_number > my_favorite_number:
    print("more")
else:
    print("less")