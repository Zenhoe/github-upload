weekday = input("Waht day is it: ")

if weekday == "Monday" or "Tusday" or "Wensday" or "Thursday" or "Friday":
    weekday = True
    vacation = False

def sleepin ():
    if weekday == True: 
        print("Don't sleep in")
    else:
        print("Do sleep in")

sleepin()