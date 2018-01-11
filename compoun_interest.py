# This program is to calculate final amount using compound interest
principal_amount = int(input("Enter Principal amount\n")) #pricipal amount 
number_times = 12                          #number of times the interest is compunded per year
interest_rate = float(input("Enter Interest Rate as decimal\n"))                #annual nomial interest rate (as a decimal
years = int(input("Enter number of years\n")) #Requesting user to enter the years
year_time = number_times*years                #calculates exponent
rate_time = float(1+ (interest_rate / number_times))
second_half = rate_time**year_time
formula = (principal_amount * second_half)

print (formula)
