def Create_Account():
    UserName = input("What is your username: ")
    print("Your password has to be 8 long")
    Password = input("What is your password: ")
    Create = open(UserName + ".txt", "w")
    Create.write(Password + "\n")
    Create.write(UserName + "\n")
    Create.close()


Create_Account()