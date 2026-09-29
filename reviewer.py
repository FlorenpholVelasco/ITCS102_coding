age = int(input("Age: "))
rev = float(input("Revenue: "))
cc = int(input("Credit score: "))
yrs = float(input("Years in business: "))
has_defaults = input("Filed for bankruptcy (yes/no): ").strip().lower() == "yes"
collateral = input("What is your collateral: ")
c_value = float(input("Collateral value: "))

max_loan = 0
base_fee = 0

if age >= 21 and not has_defaults and yrs >= 2.0:
    print("Baseline Passed")
    if cc >= 720:
        print("Credit score accepted")
        max_loan = rev * 3
        if rev >= 500000:
            print("Revenue is 500,000 or above")
            base_fee = max_loan * 0.015
        else:
            print("Revenue is below 500,000")
            base_fee = max_loan * 0.025
        print("Base fee is set to", base_fee)

        if c_value >= max_loan:
            print("Collateral", collateral, "with a value of", c_value, "is ACCEPTED")
        else:
            print("Collateral REJECTED")

        if c_value % 5000 != 0:
            base_fee += 250
            print("Additional charge added, total base fee is", base_fee)
        else:
            print("Collateral value is divisible by 5000")
    elif 620 <= cc < 720:
        print("Credit score is in range 620 to 719")
        max_loan = rev * 1.5
        if yrs >= 5.0:
            base_fee = max_loan * 0.02
        else:
            base_fee = max_loan * 0.035
        print("Your base fee is", base_fee)
    else:
        print("Credit score is too low")
else:
    print("Baseline Failed")