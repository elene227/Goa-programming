
original_password = "mypassword"
user_input = input("შეიყვანეთ პაროლი: ")


while user_input != original_password:
    print("პაროლი არასწორია, სცადეთ ხელახლა.")
    user_input = input("შეიყვანეთ პაროლი: ")

print("პაროლი სწორია!")
