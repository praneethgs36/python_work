import car as c
import electric_car as ec

my_mustang = c.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = ec.ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())