# This program will be a financial calculator both an investment calculator
# and a home loan repayment calculator.

# Imports need to make the program work.
import math

# This is used to ask the user to choose between 'investment' or 'bond'.
user_selection = input(
    "Choose either 'investment' or 'bond' from the menu below to"
    "proceed:\n\ninvestment \t- to calculate the amount of interest"
    "you'll earn on an investment.\nbond \t- to calculate the amount"
    "you'll have to pay on a home loan.\n: ").lower()

# If checks to determin if the user wants to check for a 'investment' or
# a 'bond', depending on their answer each if block will trigger different
# questions to determin their intrest or bond repayments.
if user_selection == "investment":
    deposit = float(input("How much money are you do you wish to"
                            " invest, e.g. '100': R"))
    intrest = float(input("What is the intrest rate please enter it as "
                            "just a number no '%' sign needed, e.g. '8': "))
    intrest_as_decimal = intrest / 100
    years = int(input("Please enter the number of years you "
                        "plan to invest for, e.g. '5': "))
    investment_type = input("What type of investment is it 'simple' or "
                            "'compound' intrest: ").lower()

    # This if block is used to compare the investment type and calculate
    # the amount of intrest they will get depending on the investment type.
    if investment_type == "simple":
        intrest_amount = round(deposit * ( 1 + intrest_as_decimal * years), 2)

        print(f"If you invest R{deposit} \nFor {years} years at an intrest "
                f"rate of {intrest}% \nYou will have a total investment "
                f"of R{intrest_amount}")

    elif investment_type == "compound":
        intrest_amount = round(deposit * math.pow((1 + intrest_as_decimal),
                                years), 2)

        print(f"If you invest R{deposit} \nFor {years} years at an intrest "
                f"rate of {intrest}% \nYou will have a total investment "
                f"of R{intrest_amount}")

# This else block is for the bond repayment calculation asking questions to be
# used in the formula to to calculate how much to repay.
elif user_selection == "bond":
    value = float(input("What is the current value of the house: R"))
    intrest = float(input("What is the current intrest rate: "))
    months = int(input("How many months do you plan to take to repay the "
                        "total bond: "))
    intrest_as_monthly = (intrest / 100) / 12
    print(intrest_as_monthly)
    bond_amount = round((intrest_as_monthly * value) / (1 -
                        (1 + intrest_as_monthly) ** (-months)), 2)
    print(f"If the value of the house is {value} \nWith an intrest amount of "
            f"{intrest}% \nIf you want to pay it off in {months} months. "
            f"\nYou will need to repay R{bond_amount} each month.")

            #x = (i.P)/(1 - (1+i)^(-n))