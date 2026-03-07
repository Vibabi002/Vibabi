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

