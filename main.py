
import random
"""
class Human :
    def __init__(self, name='Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []


    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers: ")
            for passenger in self.passengers:
                print(passenger.name)
        else:
             print(f"There are no passengers in {self.brand}")

vasya = Human("Vasya")
petya = Human("Petya")

car = Auto("Mercedes")

car.add_passengers(vasya)
car.add_passengers(petya)
car.print_passengers_names()

-------------------------------------------sims-------------------------------------------------------
"""


class Human :
    def __init__(self, name="Human", job=None,home=None, car=None):
        self.name =name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)


    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5


    def work(self):
        if self.car.drived:
            pass
        else:
             if self.car.fuel < 20:
                self.shopping("fuel")
                return
             else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.gLadness_Less
        self.satiety -= 4

    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                 self.to_repair()
                 return

        if manage == "fuel" :
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Yay! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

def chill (self):
    self.gladness += 10
    self.home.mess += 5

def clean_home(self):
    self. gladness -= 10
    self.hone.ness += 5
def to_repair(self):
    self.car.strength += 100
    self.money -= 50


def days_indexes(self, day):
    day = f"Today {day} of {self-name}'s lie"
    print (f"{day: ^50) ", "in")
    human_indexes = self.name +
    print(f"{human_indexes:^50} , "\n")
    print(f"Money - {self. money}")
    print(ersetiety - (sett setiety!")
    print(f"oladness - (sett gLadness)")
    home _indexes = "Hono indexes"
    print (r*-(hone_indexess+50)"
    print(r*Food - (sett-home.rood)")
    print(+"Ness - (self.hone.ness)n)
    car _indexes = ("(sett-car.brand) con indoxes"
    print(r* (car _indexess"50), «in)
    print (F*Fuel - (sett-car.fuel)")
    print (restrength (sett. car. strength)

class Auto :
    pass

class Haus :
    pass

