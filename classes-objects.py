__author__ = 'Ingrid Marie'

class Things(): # Main class
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass

class Sidewalks(Inanimate):
    def pedestrian(self):
        print('Pesestrian Walking')
    def cycle(self):
        pass
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()



reginald = Giraffes()
harold = Giraffes()
samora = Mammals()
ali = Sidewalks()
reginald.dance_a_jig()
harold.eat_leaves_from_trees()
reginald.breathe()
samora.eat_food()

harold.find_food()
