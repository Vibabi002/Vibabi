import random




class Job:
    
    def __init__(self, name:str = "test_job", salary:float = 1):
        self.name = name
        self.salary = salary

    """сеттеры(изменяют значения параметров)"""
    
    def set_name(self, name:str):
        self.name = name

    
    def set_salary(self, salary:float):
        self.salary = salary



class Human:
    
    def __init__(self, name:str = "name", job:Job = None,
                 home = None, car = None, money:float = 0):
        self.name = name
        self.job = job
        self.home = home
        self.happiness = 100
        self.satiety = 100
        self.car = car
        self.money = money

    """сеттеры(изменяют значения параметров)"""
    
    def set_name(self, name:str):
        self.name = name


    def set_home(self, home):
        self.home = home

    
    def set_car(self, car):
        self.car = car

  
    def set_job(self, job:Job):
        self.job = job

    """функции"""
    
    def eat(self):
        self.satiety += 10

    
    def work(self):
        self.money += self.job.salary




musorshik = Job("musorshik", 300000)
futbolist = Job("futbolist", 200000)
TEMSHIK = Job("TEMSHIK", 50000)


Murad  = Human(
    "Murad", musorshik, "kazaxstan", "samosval", 0)
Vidadi = Human("Vidadi", futbolist, "badamdar_dacha", "Tesla", 50000)
Rasul = Human("Rasul", TEMSHIK, "28may", "Porsche", 25000)


people_list = [Murad, Vidadi, Rasul]

Murad.eat() 
Murad.work() 
musorshik.set_salary(4000)
musorshik.set_name("developer")

for person in people_list:
    print(f"Job:\n\tName: {person.job.name} \n\tSalary: {person.job.salary}")
    print(f"Human:\n\tName {person.name} \n\tJob: {person.job.name}({person.job.salary}) \n\tHome: {person.home} \n\tCar: {person.car} \n\tHappiness: {person.happiness} \n\tSatiety: {person.satiety} \n\tMoney: {person.money}")
