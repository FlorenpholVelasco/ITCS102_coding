age = int(input("age:"))
rev = float(input("Revenue:"))
cc = int(input("Credit score:"))
yrs = float(input("Years in business:"))
has_defaults = bool(input("File for bankruptcy:"))
collateral = input("What is your collateral:")

max_loan = 0
base_fee = 0
c_value = 0

if age >= 21 and has_defaults == False and yrs >= 2.0:
    print("Baseline Passed")
    if cc >= 720:
        print("Credit score accepted")
        max_loan = rev * 3

    
        if rev >= 500000:
            print("Revenue above 50k")
            base_fee = max_loan * 0.015
            print("Base fee is set to", base_fee)

            if yrs >= 5.0:
                base_fee = max_loan * 0.02
                print("Years in business is lower than 5 years so your base fee is", base_fee)
                

        else:
            print("Revenue is below 50k")
            base_fee = max_loan * 0.025
            print("Base fee is set to", base_fee)

        if c_value >= max_loan:
             print("Collateral",collateral,"With a value of",c_value,"is ACCEPTED")
        else:
             print("Collateral REJECTED")

        if c_value % 5000 != 0:
             base_fee += 250
             print("Additional charge added to Base Fee, total Base Fee is", base_fee)
        else:
             print("Collateral value is divisible by 5000")

             
    elif cc <= 620 and cc < 720:
            print("Credit score is i range with 620 and 720")
            max_loan = rev * 1.5
    
    elif cc < 620:
            print("Credit score is too low")

    
    
    else:
        print("Invalid")

    
else:
    print("Baseline Failed")