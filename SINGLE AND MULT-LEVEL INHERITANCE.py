class Animal:
    def speak(self):
        return "Some generic sound"
class Dog(Animal):
    def speak(self):
        return "Bark"
dog = Dog()
print(dog.speak())  # Output: Bark

class Vehicle:
    def describe(self):
        return "This is a vehicle."
class Car(Vehicle):
    def describe(self):
        return "This is a car with 4 wheels."
class SportsCar(Car):
    def describe(self):
        return "This is a sports car."
s = SportsCar()
print(s.describe())  # Output: This is a sports car.

class Device():
    def describe(self):
        return "This is a device"

class Computer(Device):
    def describe(self):
        return "This is a Computer"

class Laptop(Computer):
    def describe(self):
        return"This is a laptop"

obj = Laptop()
print(obj.describe())

#MULTIPLE INHERITANCE AND MRO
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"


class C(A):
    def show(self):
        return "C"


class D(B, C):  # Multiple inheritance
    pass


d = D()
print(d.show())  # Output: B
print(D.mro())  # Shows method resolution order

# REAL WORLD EXERCISE
class Vehicle:
    def fuel_type(self):
        print("Unknown")

class ElectricVehicle:
    def fuel_type(self):
        print("Electric")

class GasolineVehicle:
    def fuel_type(self):
        print("Gasoline")

class HybridCar(ElectricVehicle, GasolineVehicle):
            pass

obj = HybridCar()
obj.fuel_type()
print(HybridCar.__mro__)

#THE DIAMOND PROBLEM IN INHERITANCE
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass

print(D.mro())
print(D().show())

#Real-world Exercise: Corporate Hierarchy
class Employee:
    def get_role(self):
        print("Employee")

class Manager:
    def get_role(self):
        print("This is the manager")

class BoardMember:
    def get_role(self):
        print("I am a boardmember")

class Director(Manager, BoardMember):
    pass

obj = Director()
obj.get_role()
print(Director.__mro__)
