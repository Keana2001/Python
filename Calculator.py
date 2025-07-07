# prompt the user to enter the information needed
cost_of_airfare = float(input("What is the cost of the airfare: "))
cost_of_hotel_nights = int(input("Number of nights in hotel: "))
nightly_hotel_cost = float(input("Cost of nightly stays in hotel: "))
rental_car_days = int(input("Number of car rental days: "))
daily_car_rental_cost = float(input("Cost of rental car per day: "))

# Constants defined
TAX_RATE = 0.1 # 10% tax rate
HOTEL_TAX_RATE = 0.05 # 5% hotel tax rate

#  Total cost of each item calculated
total_airfare_cost = cost_of_airfare + (cost_of_airfare * TAX_RATE)
total_hotel_cost = (cost_of_hotel_nights * nightly_hotel_cost) + ((cost_of_hotel_nights * nightly_hotel_cost) * HOTEL_TAX_RATE)
total_car_rental_cost = rental_car_days * daily_car_rental_cost

# Calculation of total trip cost
total_trip_cost = total_airfare_cost + total_hotel_cost + total_car_rental_cost

# Total trip cost with message printed
print("The total cost of your trip is: $", format(total_trip_cost))
