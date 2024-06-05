# Figure out costs of a trip -- units: liters, kilometers

# kilometers to drive
distance = int(input("How far is your trip in kilometers? "))

# liters-per-km usage of car: liters used % distance
liters_per_km = float(input("How many liters does your vehicle get per km? "))

# price per liter of fuel -- allow for int or float responses
cost_per_liter = float(input("How much do you pay for gas per liter on average? "))

def trip_calculator(distance, liters_per_km, cost_per_liter):
# calculate how many liters burned on the trip
    required_fuel = distance * liters_per_km

# Cost of fuel
    fuel_price = required_fuel * cost_per_liter
    return fuel_price

total_cost = trip_calculator(distance, liters_per_km, cost_per_liter)
print(f"The cost for a {distance} km trip is {total_cost} ")