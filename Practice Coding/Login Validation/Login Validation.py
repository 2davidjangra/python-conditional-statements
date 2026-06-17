stored_username = "admin"
stored_password = "1234"

for i in range(3):
    username = input("Username: ")
    password = input("Password: ")

    if username == stored_username and password == stored_password:
        print("Login Successful")
        break
    else:
        print("Invalid Username or Password")
else:
    print("Account Locked")
