import random

def Rock_Paper_Scissors():
    print("This is a game of rock, paper, scissors")
    print("Just enter one of the three and the computer will play with you")



    Det_Number = random.randint(1, 3)



    if Det_Number == 1:
        computerChoice = "Rock"
    if Det_Number == 2:
        computerChoice = "Paper"
    if Det_Number == 3:
        computerChoice = "Scissors"



    UserInput = input("Please enter your choice: ")



    if UserInput == "Rock":
        if computerChoice == "Scissors":
            print(UserInput)
            print(computerChoice)
            print("You win")

    if UserInput == "Scissors": 
        if computerChoice == "Rock":
            print(UserInput)
            print(computerChoice)
            print("You lose")
    
    if UserInput == "Paper": 
        if computerChoice == "Scissors":
            print(UserInput)
            print(computerChoice)
            print("You lose")
                
    if UserInput == "Scissors": 
        if computerChoice == "Paper":
            print(UserInput)
            print(computerChoice)
            print("You win")
    
    if UserInput == "Paper": 
        if computerChoice == "Rock":
            print(UserInput)
            print(computerChoice)
            print("You win")
    
    if UserInput == "Rock": 
        if computerChoice == "Paper":
            print(UserInput)
            print(computerChoice)
            print("You lose")

    

Rock_Paper_Scissors()


        

    
