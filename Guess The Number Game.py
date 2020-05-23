import random

print("This is a guessing game")
print("The computor while get a random number and you have to guess it")
Input_Num = int(input("Enter a number: "))
Num_Guess = int(input("Guess the number 1 out of " + str(Input_Num) + " : "))
num = random.randint(1, Input_Num)

if Num_Guess < num:
    NumX = num - Num_Guess
    print("Wrong, you were " + str(NumX) + " off")
    print("The real number is " + str(num))
else:
    if Num_Guess > num:
        NumX = Num_Guess - num
        print("Wrong, you were " + str(NumX) + " off")
        print("The real number is " + str(num))
if Num_Guess == num:
    print("YOU WIN THAT IS RIGHT")
    print("Good job you win")