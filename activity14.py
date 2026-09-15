age = int(input("age:"))
is_employed = bool(input("employed:"))
credit_score = float(input("credit score:"))
annual_income = float(input("annual salary:"))
has_collateral = bool(input("do you  have collateral (True/False)"))

base_rate = 0.0

if age >= 21 and is_employed == True:
        print("approved")
elif credit_score >= 750:
        print("high credit score")
        if annual_income >= 100000:
              print("high annual income")
        base_rate = 4.5    
        print("Your base rate is", base rate)   
    else:
        base_rate = 5.0
        print("your base rate is",base_rate)
elif credit_score >= 600 and credit score<= 750 :
    print("your credit score is less than 750")
   if has_collateral == True
         print("you have collateral")
         base_rate = 7.0
         print(your base rate is", base_rate")
    elif annual_income <= 40000:
        print("low annual income")
        base_rate = 9.0
        print(your base rate is", base_rate)
    else:
        base_rate = 8.0
        print("your base rate is", base rate)

else:
     print("Rejected: Fails baseline criteria")