money = 6767

#computation here
a = money // 1000
b = (money % 1000) // 500
c = (money % 1000 % 500) // 200
d = (money % 1000 % 500 % 200) // 100
e = (money % 1000 % 500 % 200 % 100) // 50
f = (money % 1000 % 500 % 200 % 100 % 50) // 20
g = (money % 1000 % 500 % 200 % 100 % 50 % 20) // 10
h = (money % 1000 % 500 % 200 % 100 % 50 % 20 % 10) // 5
i = (money % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5) // 1

#prints here
print("1000 = ",a)
print(" 500 = ",b)
print(" 200 = ",c)
print(" 100 = ",d)
print("  50 = ",e)
print("  20 = ",f)
print("  10 = ",g)
print("   5 = ",h)
print("   1 = ",i)
print("Total money deposited -->",money)