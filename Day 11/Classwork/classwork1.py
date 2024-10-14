
my_name = "ელენე"  


user_name = input("შეიყვანეთ თქვენი სახელი: ")
user_height = int(input("შეიყვანეთ თქვენი სიმაღლე (სანტიმეტრებში): "))


if user_name == my_name or user_height > 170:
    print("პირობა შესრულებულია.")
else:
    print("პირობა ვერ შესრულდა.")
