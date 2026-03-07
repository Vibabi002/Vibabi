import logging

# настройка логирования
logging.basicConfig(
    filename="simulation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Sim:
    def _init_(self, name):
        self.name = name
        self.energy = 100
        logging.info(f"Sim {self.name} created with energy {self.energy}")

    def eat(self):
        self.energy += 10
        logging.info(f"{self.name} eats. Energy = {self.energy}")

    def work(self):
        self.energy -= 20
        logging.info(f"{self.name} works. Energy = {self.energy}")

    def sleep(self):
        self.energy = 100
        logging.info(f"{self.name} sleeps. Energy restored to {self.energy}")


# симуляция
sim = Sim("Alex")

sim.work()
sim.eat()
sim.sleep()
sim.work()