true = True
while true == True:
    #Add infomation 
    def Add_Info():
        Human = input("Who would you like to add info about: ")
        Comand = input("What would you like to do: ")
        if Comand == "Add":
            Info = input("Add in informaiton: ")
            Add = open(Human + ".txt", "a")
            Add.write(Info + "\n")
            Add.close()
            loop = input()
            while loop == "new":
                Info = input("Add in informaiton: ")
                loop = input()
                Add = open(Human + ".txt", "a")
                Add.write(Info + "\n")
                Add.close()
        if Comand == "Read":
            Add = open(Human + ".txt", "r")
            Read_Info = Add.read()
            print(Read_Info)
            Add.close()


        

    #Add the person 
    def Add_Person():
        NameOfPerson = input("What is the name of the person: ")
        if NameOfPerson == "skip":
            Add_Info()
        else:
            Location = input("Where is the person from: ")
            Add = open(NameOfPerson + ".txt", "w")
            Add.write(NameOfPerson + "\n")
            Add.write(Location + "\n")
            Add.close()
            Add_Info()



    #Add Person
    Add_Person()
