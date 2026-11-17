#jeepney simulation

route = ["Bayan", "Sm", "Dll"]
passengers = []
SEATS = 8
FARE = 14
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("1 sakay 2 priority seat 3 para po!")
    print("4 baba sa pinto 5 baba sa harap")
    print("6 seat check 7 babalikan 8 exit")
    choice = input("choice: ")

    if  choice == "1":
        if len(passengers) == SEATS:
            print("puno na!")
        else:
            name = input("name:")
            passengers.append(name)
            total = total + FARE
            print(name,"boarded at the back.")

    elif choice == 2:
        if len (passengers) == SEATS:
            print("puno na!")
        else:
            name = input("name:")
            passengers.insert(0,name)
            total = total + FARE
            print(name,"took the priority seat.")

    elif choice == "3":
        name = input("who is getting off")
        if name in passengers:
            passengers.remove(name)
            print(name,"got off. ingat!")
        else:
            print(name,"is not on this jeepney.")

    elif choice == "4":
        if len(passengers) == 0:
            print("the jeepney is empty")
        else:
            left = passengers.pop()
            print(left,"got off at the door.")

    elif choice == "5":
        if len(passengers) == 0:
            print("the is empty")
        else:
            front = passengers.pop(0)
            print(front<"got off at the front.")

    elif choice == "6":
        for i in range(len(passengers)):
            print("SEAT", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Ruote:", route)

    elif choice == "8":
        print("Tatal fare today:", total)
        break
    else:
        print("invalid choice")