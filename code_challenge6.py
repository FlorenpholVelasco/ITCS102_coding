code = 1
size = int(input("size ="))
for x in range (1,size):
    for y in range (x):
        print(code, end = " ")
        code += 1
    print()
