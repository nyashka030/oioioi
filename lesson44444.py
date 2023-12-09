
class Grandparent:

    def about(self):
        print('i am grandparent')

    def about_myself(self):
        print('i am grandparent')

class Parent(Grandparent):

    def about_myself(self):
        print('i am parent')


class Child(Parent):

    def __init__(self):
        super().about()
        super().about_myself()

c = Child()

class Computer:

    def __init__(self, model, *args, **kwarg):
        super().__init__(*args, **kwarg)
        self.model = model
        self.memory = 128

class Display:

    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)
        self.resolution = '4k'

class SmartPhone(Display, Computer):

    def info(self):
        print(self.resolution)
        print(self.memory)

iphone = SmartPhone(model='25 pro max SUPERRR')
iphone.info()