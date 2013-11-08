#. Vacation Expenditure Calculation example
#. Author: @dspk

#. A function that takes the variable nights as input; assume hotel costs 120/night
def hotel_cost(days):
    return days * 120

#. A function that takes a string, city, as input.    
def plane_ride_cost(city):
    if city == "Los Angeles":
        return 145
    elif city == "San Francisco":
        return 225
    elif city == "Seattle":
        return 222
    else:
        return 385

#. A function that returns the cost for renting a car for said number of days. 
#. Every day you rent the car is $45.
#. If you rent the car for 3 or more days, you get $20 off your total.
#. 7 or more days, you get $55 off your total.
def rental_car_cost(days):
    c_cost = 45*days
    if days >= 3 and days < 7 :
        c_cost = c_cost - 20
    if days >= 7 :
        c_cost = c_cost - 55
    return c_cost
    
#. A function that returns the sum of all costs
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
#. Cost of a trip to "New York City" for 5 days with an extra 800 dollars of spending money
print trip_cost("New York City", 5, 800), "is the cost of a trip to NYC for 5 days"


bill = hotel_cost(5)

#. A function that returns the minimum payment that you can make with your total balance. 
def get_min(balance, rate):
    return  rate*balance
    
print get_min(bill, 0.02)

#. A function that takes the input balance and returns balance with interest 
def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
    new_bal = balance - payment 
    new_balance = add_monthly_interest(new_bal)
    return "You still owe: " + str(new_balance)

print make_payment(150, bill)
