cars = 100   # of cars available
space_in_a_car = 4 # of spaces available in a car
drivers = 30  # of drivers available to drive the cars.
passengers = 90  # of passengers that want to ride
cars_not_driven = cars - drivers # of cars that are sitting idle
cars_driven = drivers # of cars that are being driven currently
carpool_capacity = cars_driven * space_in_a_car #Calculates carpool_capacity in the avaiable cars
average_passengers_per_car = passengers / cars_driven # of passengers available per car.


print("There are", cars, "cars available.")  # print the # of cars available.
print("There are only", drivers, "drivers available") #prints the # of drivers available.
print("There will be", cars_not_driven, "empty cars today.") # prints the # of cars that will not be driven
print("We can transport", carpool_capacity, "people today.") # prints the # people capacity for carpool.
print("We have", passengers, "to carpool today.") # prints the # of passengers available.
print("We need to put about", average_passengers_per_car, "in each car.") # prints average # of passegers in each car.
