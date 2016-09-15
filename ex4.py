# Assignment the numbers of cars to a variable 'cars'.
cars = 100
# Assignment the numbers of free places in car to a variable 'space_in_a_car'.
space_in_a_car = 4.0
# Assignment the numbers of drivers to a variable 'drivers'.
drivers = 30
# Assignment the number of passangers to a variable 'passangers'.
passangers = 90
# Counting the number of cars which are not in use and assignment it
# in a variable 'cars_not_driven' by substraction of number of cars and drivers.
cars_not_driven = cars - drivers
# Assignment the number of cars which are in use in a variable 'cars_driven'
# base on the numbers of drivers.
cars_driven = drivers
# Counting the carpool capacity and assignment it in a variable
# 'carpool_capacity' by multiplication of cars in use and free space in each car.
carpool_capacity = cars_driven * space_in_a_car
# Counting the avarage number of passangers in each car and assignment it in a
# variable 'avarage_passangers_per_car' by division of passangers and cars in use.
avarage_passangers_per_car = passangers / cars_driven

# Printing the sentence with cars variable.
print "There are", cars, "cars avaliable."
# Printing the sentence with drivers variable.
print "There are only", drivers, "drivers avaliable."
# Printing the sentence with cars_not_driven variable.
print "There will be", cars_not_driven, "empty cars today."
# Printing the sentence with carpool_capacity variable.
print "We can transport", carpool_capacity, "people today."
# Printing the sentence with passangers variable.
print "We have", passangers, "to carpool today."
# Printing the sentence with avarage_passangers_per_car variable.
print "We need to put about", avarage_passangers_per_car, "in each car."
