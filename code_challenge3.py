#code_challenge3


name = input("input name:  ")
Type_item = input("The items is:   ")
is_frag = bool(input("input the fragile yes/no:    "))
w = float(input("input the weight kg:   "))
d = float(input("input the distance  km:  "))
is_express = bool(input("is it express yes/no;   "))
is_international = bool(input("is it international yes/no? :  "))
base_cost = (w * 2.50) + (d * 0.15)

print("-------> Summary of the item <--------")    
print("sender:", name)
print("Item:", Type_item)
print("Is it Fragile;", is_frag)
print("weight:", w)
print("distance", d)


if w <= 2 and d <= 100 and not is_express and not is_international:
    print("Free shipping")
    print("the total cost; 0.00 $ \n")
elif is_express and is_international:
    print("Shipping rate international express" )
    print("the total cost:", (base_cost * 1.40) + 50 )
elif is_express or (is_international and w > 20):
    print("shipping rate; Express or Heavy international")
    print("the total cost:", (base_cost * 1.20)+ 25 )
elif w > 30 or d > 1000: 
    print("shipping rate: Oversized")
    print("the total cost:", base_cost + 30 )
elif is_frag == True:
    print("the frag is true \n")
else:
    print("Shipping rate: Standard")
    print("the total cost:", base_cost)