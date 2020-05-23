def Speed_Test(speed = 130):
    points = 0
    if speed <= 70:
        print("Ok")
    else:
        if speed >= 71:
            print("Bad")
            if speed >= 75:
                while speed >= 75:
                    points += 1
                    speed -= 5
                print("Points are equal to: " + str(points))
                if points >= 12:
                    print("Suspended License")



                

Speed_Test()
    