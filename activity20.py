from getpass import getpass

isLogin = False 

while isLogin == False:
    username = input("what is your username:")
    password = getpass("what is your password")

    if username == "mahalkobebeko" and password == "jhenina":
        print("access granted")
        isLogin = True
    else:
        print("access denied")