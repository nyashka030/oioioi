import random


class Cat:

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 10
        self.energy = 10
        self.alive = True


    def eat(self):
        print(f"{self.name} is eating.")
        self.hunger -= 3
        self.happiness += 2
        self.energy += 1

    def play(self):
        print(f"{self.name} is playing.")
        self.hunger += 1
        self.happiness += 3
        self.energy -= 2

    def sleep(self):
        print(f"{self.name} is sleeping.")
        self.hunger += 1
        self.happiness += 1
        self.energy += 5

    def is_alive(self):
        if self.hunger >= 10 or self.happiness <= 0 or self.energy <= 0:
            print(f"{self.name} has passed away. ")
        self.alive = False

    def end_of_day(self):
        print(f'{self.name} - Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}')

    def live(self, day):
        print(f'Day {day} of {self.name}\'s life')
        action = random.choice(["eat", "play", "sleep"])
        if action == "eat":
            self.eat()
        elif action == "play":
            self.play()
        else:
            self.sleep()
        self.end_of_day()
        self.is_alive()

whiskers = Cat(name="Whiskers")
for day in range(365):
    if not whiskers.alive:
        break
whiskers.live(day)



