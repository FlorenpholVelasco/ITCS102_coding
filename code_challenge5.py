for x in range(5):
    for y in range(5):
        if x == y or x + y == 4:
            print("*", end= " ")
        else:
            print(" ", end= " ") 
    print("")
