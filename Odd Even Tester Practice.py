def OddevenTester(limit = 0):
    while limit < 3000:
        if limit%2 == 0:
            print(str(limit) + " Even")
        else:
            print(str(limit) + " Odd")
        limit = limit + 1

OddevenTester()
