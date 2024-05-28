main_pwd = input("Enter your main password: ")

while True:
    q1 = input("Would you like to view passwords or add passwords? Or q to quit").lower()
    if q1 == "q":
        quit()
    if q1 == "add":
        add_user = input("What is the username for this password? ")
        add_pwd = input("Enter the password ")
        with open("password.txt", "a") as file:
            file.write("Username: " + add_user + "| Password: " + add_pwd )
    if q1 == "view":
        with open("password.txt", "r") as file:
            for lines in file:
                print(lines.rstrip())
