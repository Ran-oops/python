#声明4个类
class animal:
    def say(self):
        print('animal start')
        print('animal end')
class human(animal):
    def say(self):
        print('human start')
        animal.say(self)
        print('human end')
class bird(animal):
    def say(self):
        print('bird start')
        animal.say(self)
        print('bird end')

class birdhuman(bird,human):
    def say(self):
        print('birdhuman start')
        human.say(self)
        bird.say(self)
        
        print('birdhuman end')

bh=birdhuman()
bh.say()
print(birdhuman.__dict__)
print(bh.__dict__)
print(birdhuman.__mro__)        