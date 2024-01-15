import math

# Instructions and menu options:
print("This program will help you calculate finances.")
print("investment: to calculate the amount of interest you'll earn on your investment")
print("bond: to calculate the amount you'll have to pay on a home loan")

# Ensure user entry is valid (either 'investment' or 'bond')
def valid_input():
    while True:
        user_input = input("Enter 'investment' or 'bond' from the menu above to proceed: ").lower()  # Convert input to lowercase for case-insensitivity

        if user_input == 'investment' or user_input == 'bond':
            return user_input
        else:
            print("Invalid input.")

# Program start:
calculation_type = valid_input()

if calculation_type == 'investment':
    # Run investment calculation program
    print("Running investment program...")
    depositing = (input("Please enter the amount you are depositing: "))
    interest_amount = (input("Please enter your interest rate as an integer: "))
    length_of_investment = (input("How many months do you plan on investing for?: "))
    simple_compound = input("Would you like simple or compound interest?: ")
    r = float(interest_amount) / 100.00
    P = float(depositing)
    t = float(length_of_investment)
    simple_a = int(P * (1.0 + r * t))
    compound_a = int(P * math.pow((1.0 + r),t))
    print(depositing)
    print(interest_amount)
    print(length_of_investment)
    print(simple_compound)
    if simple_compound.lower() == "simple":
        print(f"Your calculated simple interest is: {simple_a}")
    elif simple_compound.lower() == "compound":
        print(f"Your calculated simple interest is: {compound_a}")


elif calculation_type == 'bond':
    # Run bond calculation program
    print("Running bond program...")
    house_value=input("Enter the value of the house: ")
    interest_amount = (input("Please enter your interest rate as an integer: "))
    repayment_months = input("Enter the number of months you will take to repay the bond: ")
    H = float(house_value)
    i = float(interest_amount) / 12.0
    n = float(repayment_months)
    repayment = int((i * H) / (1.0 - (1.0 + i) ** (-n)))
    print(house_value)
    print(interest_amount)
    print(repayment_months)
    print(f"The amount you will have to repay each moth is: £{repayment}")