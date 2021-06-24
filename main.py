from car import car

car1 = Car("Honda", "Civic", 2020, 15000.0, 20000)
print(car1.get_details())
print("First Car’s Initial Profit is $%.2f" % car1.calc_profit())
car1.reduce_price(1000)
print("First Car’s New Profit is $%.2f" % car1.calc_profit())
