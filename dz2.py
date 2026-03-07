class Pet:
    def _init_(self, name1, type1, birthyear1):
        self.name = name1
        self.type = type1      # cat или dog
        self.birthyear = birthyear1
        self.hunger = 50
        self.energy = 50
        self.mood = 50
        self.hobbies = []

    def eat(self):
        print(f"{self.name} is eating")
        self.hunger -= 20
        self.energy += 10

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.energy += 30

    def play(self):
        print(f"{self.name} is playing")
        self.energy -= 20
        self.mood += 20
        self.hunger += 10

    def show_info(self):
        print(f"{self.type} : {self.name}")
        print(f"age: {2026 - self.birthyear}")
        print(f"hunger: {self.hunger}")
        print(f"energy: {self.energy}")
        print(f"mood: {self.mood}")
        print(f"hobbies: {self.hobbies}")