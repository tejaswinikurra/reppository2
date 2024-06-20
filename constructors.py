class Computer:
    def __init__(self):
        self.name = "teju"
        self.age = "19"
    #def update(self):
        #self.name="lilly"

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        

obj1 = Computer()
#obj1.age = 30
obj2 = Computer()

if obj1.compare(obj2):
    print("they are same")

#obj1.update()

obj1.compare(obj2)
print(obj1.name)
print(obj2.age)
print(obj1.age)