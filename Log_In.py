import os
def Log_In():
    UserName_Log_In = input("Enter your username: ")
    Password_Log_In = input("Enter your password: ")

    Pass_Check = open(UserName_Log_In + ".txt", "r")

    Check_PassWord = Pass_Check.read(8)
    if Password_Log_In != Check_PassWord:
        print("No Good")
    else:
        cmd = 'TurtleRace.py'
        os.system(cmd)

    Pass_Check.close

Log_In()

   
