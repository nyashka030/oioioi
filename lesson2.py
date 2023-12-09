import random


#n = 10
#x = 1.5

#print(type(n))
#print(type(x))


#class Student:

    #def __init__(self, name, height=170):
       # self.name = name
      #  self.height = height
     #   print('I am alive.')
    #def grow(self, value = 1):
   #     self.height += value


  #  def __str__(self):
 #       return  f'My name {self.name}. My height is {self.height}'



#nick = Student(name="Nick")
#print(nick.height)

#alex = Student(name="Alex", height=190)
#alex.grow(15)
#print(alex)


class Student :

    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 0
        self.alive = True

    def study(self):
        print("time to learn smth new")
        self.progress += 0.12
        self.gladness -= 5

    def sleep(self):
        print("its time to sleep")
        self.gladness += 3

    def chill(self):
        print("Time to relax")
        self.gladness += 4
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Oppss..")
            self.alive = False
        else :
            self.gladness <= 0
            print("Depression...")
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Proggres - {self.progress}')

    def live(self, day):
        print(f'Day {day} of {self.name} life')
        rnd = random.randint(1, 3)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.sleep()
        else:
            self.chill()

        self.end_of_day()
        self.is_alive()

nick = Student(name='Nick')
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)
