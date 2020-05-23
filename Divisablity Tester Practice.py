def DivTest(num = 0): 
    while num < 1000:
        if num%3 == 0 + num%5 == 0:
            print("FizzBuzz")
        else:
            if num%3 == 0:
                print("Fizz")
            if num%5 == 0:
                print("Buzz")
        num=num + 1


DivTest()
