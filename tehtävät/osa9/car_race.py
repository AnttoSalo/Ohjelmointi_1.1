import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, speed_change):
        new_speed = self.speed + speed_change
        if new_speed < 0:
            self.speed = 0
        elif new_speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = new_speed

    def travel(self):
        self.distance += self.speed

    def print_car_details(self):
        print("{:<15}{:<15}{:<15}{:<15}".format(
            self.registration_number, self.max_speed, self.speed, self.distance))


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasCar(Car):
    def __init__(self, registration_number, max_speed, fuel_tank_size):
        super().__init__(registration_number, max_speed)
        self.fuel_tank_size = fuel_tank_size


class Race:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars

    def hour_forward(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.travel()

    def print_status(self):
        print("{:<15}{:<15}{:<15}{:<15}".format(
            "Rekisterinumero", "Huippunopeus", "Nopeus", "Matka"))
        for car in self.cars:
            car.print_car_details()

    def race_over(self):
        return any(car.distance >= self.length for car in self.cars)


# Periytymis tehtävä
electric_car = ElectricCar("ABC-15", 180, 52.5)
gas_car = GasCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gas_car.accelerate(80)

for i in range(3):
    electric_car.travel()
    gas_car.travel()

print("Electric car distance: {} km".format(electric_car.distance))
print("Gas car distance: {} km".format(gas_car.distance))


# Romuralli tehtävä
cars = []
for i in range(1, 11):
    registration_number = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(registration_number, max_speed)
    cars.append(car)

race = Race("Suuri romuralli", 8000, cars)

hours = 0
while not race.race_over():
    race.hour_forward()
    hours += 1
    if hours % 10 == 0 or race.race_over():
        print("Tunti", hours)
        race.print_status()

print("Kilpailu ohi!")
race.print_status()
