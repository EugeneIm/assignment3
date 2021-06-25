class Car:
    def __init__(self, make, model, number_of_doors, number_of_wheels):
        """
        The constructor for the Car class.
        """
        self.make = make
        self.model = model
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

    def drive_forward(self):
        print("Driving forward!")

    def drive_backward(self):
        print("Driving backward!")

    def about(self):
        print(f"{self.make} {self.model} with {self.number_of_doors} doors and {self.number_of_wheels} wheels.")


my_cool_car = Car("Honda", "Civic", 2, 4)

print(my_cool_car.make)
print(my_cool_car.model)
print(my_cool_car.number_of_doors)
print(my_cool_car.number_of_wheels)

my_cool_car.drive_forward()
my_cool_car.drive_backward()
my_cool_car.about()
