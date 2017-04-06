class Animal(object): #parent class
  def __init__(self, name, health):
    self.name = name
    self.health = health #if argument is not passed in the __init__ statement it can be set here

  def walk(self):
    self.health -= 1
    return self

  def run(self):
    self.health -= 5
    return self

  def display_health(self):
    print "Name:" + str(self.name)
    print "Health:" + str(self.health)
    return self

#instantiated panda
panda = Animal("Bash",100)

panda.walk().walk().walk().run().run().display_health()

class Dog(Animal): #more specific classes that inherit from the Animal class
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
    def pet(self):
        self.health += 5
        return self
fido = Dog("Mar", 150)
fido.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name,health)

    def display_health(self):
        print "This is dragon"
        super(Dragon, self).display_health()
        return self

    def fly(self):
        self.health -= 10
        return self

drag = Dragon("Scorch",170)
drag.walk().walk().walk().run().run().fly().fly().display_health()

gremlin = Animal("Grrr", 1000)
gremlin.walk().walk().walk().walk().walk().walk().display_health()
#AttributeError: 'Animal' object has no attribute 'fly'
