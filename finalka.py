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


name_list = ["Murad", "Vidadi", "Rasul"]
surname_list = ["Abdinov", "Aliyev", "Huseynov"]
age_list = [12, 14, 13]

class Person:
    def __init__(self, birthyear1, name1, surname1, pol1):
        self.birthyear = birthyear1
        self.name = name1
        self.surname = surname1
        self.pol = pol1
        self.hobbies = []

Murad = Person(2013, "Murad", "Abdinov", "M")
Vidadi = Person(2011, "Vidadi", "Aliyev", "M")
Rasul = Person(2012, "Rasul", "guseyinov", "M")



class Student:
    def __init__(self, name1, surname1, birthyear1, avg_grade1, course1 = "MKA"):
        self.name = name1
        self.surname = surname1
        self.birthyear = birthyear1
        self.course = course1
        self.hobbies = []
        self.avg_grade = avg_grade1

    def study(self):
        print(f"{self.name} is studying")

    def show_info(self):
        print(f"{self.name} {self.surname} : {self.course}")
        print(f"avg_grade: {self.avg_grade}")
        print(f"age: {2026 - self.birthyear}")
        print(f"hobbies: {self.hobbies}")

Vidadi = Student("Vidadi", "Aliyev", 2011, 10, "PKO")
Vidadi.show_info()
Vidadi.study()

Rasul = Student("Rasul", "Guseyinov", 2011, 11, "PKO")
Rasul.show_info()
Rasul.study()

Murad = Student("Murad", "Abdinov", 2013, 6, "PKO")
Murad.show_info()
Murad.study()

students = [Vidadi,Murad,Rasul]
import sqlite3



"""простое подключение"""

connection = sqlite3.connect("db.sl3")


cur = connection.cursor()

print(connection)
print(cur)

connection.close()



"""создание таблицы"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()


cur.execute("CREATE TABLE students (name TEXT);")


connection.commit()
connection.close()



"""добавление элементов в таблицу"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()


cur.execute("INSERT INTO students (name) VALUES ('Murad')")
cur.execute("INSERT INTO students (name) VALUES ('Vidadi')")
cur.execute("INSERT INTO students (name) VALUES ('Rasul')")


connection.commit()
connection.close()



"""вывод элементов из таблицы"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()


cur.execute("SELECT name FROM students")


connection.commit()
res = cur.fetchall()
print(res)
connection.close()



"""удаление элемента"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()


cur.execute("DELETE FROM students WHERE(name == 'Vlad')")


connection.commit()
connection.close()



"""обновление элемента"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()


cur.execute("UPDATE students SET name='Murad Otlichnik' WHERE(name == 'Murad Temshik')")


connection.commit()
connection.close()



"""удаление таблицы"""
connection = sqlite3.connect("db.sl3")
cur = connection.cursor()


cur.execute("DROP TABLE students")


connection.commit()
connection.close()

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive ()

Vidadi = Student(name="Vidadi")

for day in range(365):
    if Vidadi.alive == False:
        break

Vidadi.live(day)