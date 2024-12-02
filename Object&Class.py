class Car:
    # pass
    def __init__(self, maker, model, year, color):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('This car' + ' ' + car_1.model + ' is moving')
    def stop(self):
        print('This car is stopped')

car_1 = Car('Bens', 'GLK', 2023, 'White')
car_2 = Car('Toyota', 'Landcrucher', 2024, 'black')
print(car_1.maker, car_1.model, car_1.year, car_1.color)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
car_1.drive()
car_1.stop()

# print(car_2.maker)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

# car_2.drive()
# car_2.stop()