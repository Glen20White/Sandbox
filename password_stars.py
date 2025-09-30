minimum_length = 6
password = input(f"Please enter your password ensuring it is at least {minimum_length} characters long: ")
while len(password) < minimum_length:
    print(f"Password is not at least {minimum_length} characters long")
    password = input(f"Please enter your password ensuring it is at least {minimum_length} characters long: ")
print('*' * len(password))
