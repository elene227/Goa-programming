
original_username = "original_username"
original_password = "original_password"
original_email = "original_email@example.com"


input_username = input("შეიყვანეთ აქაუნთის სახელი: ")
input_password = input("შეიყვანეთ პაროლი: ")
input_email = input("შეიყვანეთ ემაილი: ")


if (input_username == original_username and
        input_password == original_password and
        input_email == original_email):
    print("მონაცემები სწორია!")
else:
    print("მონაცემები არასწორია.")
