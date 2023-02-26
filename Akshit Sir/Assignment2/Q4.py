
def compound_interest(principal_amount, interest_rate, year_of_investment):

    # Calculates compound interest
    Amount = principal_amount * \
        (pow((1 + interest_rate / 100), year_of_investment))
    CI = Amount
    print("Compound interest is", CI)


principal = int(input("Enter the principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))
compound_interest(principal, rate, time)
