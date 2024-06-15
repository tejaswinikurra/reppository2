class Bird:
    def intro(self):
        print("there are so many birds")
    
    def flight(self):
        print("all most all the birds can fly")
    
class Crow:
    def flight(self):
        print("crow can fly")
    
class Ostrich:
    def flight(self):
        print("ostrich cannot fly")
    
obj_bird = Bird()
obj_crow = Crow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()
obj_crow.flight()
obj_ost.flight()