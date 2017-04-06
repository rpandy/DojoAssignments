

#OOP buzz words

#Encapsulation - inside a class. keeping all relevant things together
# allows oop to be more powerful than functions alone
# class can have the methods and attributes in one place which reduces outside dependencies. A clear API to interact with the class will also help reduce outside dependencies.

#Abstration - if we were coding a car it would be an intense project.
#it could be broken up into different modules. Steering module for instance. The steering module cannot be dependent upon the braking system. When building a large project we need a lot of individual pieces with their own defined jobs. Methods should be abstracted from any particular

#inheritance - the notion of having certain classes inherit from other classes in order to gain the functionality of another class without repeating ourselves. If the

#polymorphism - the ability of things to take more than one shape or form. being able to treat classes as if they are other classes even if theyre other classes.

class Coder(Person):
    def __init__(self, languages):
        super(Coder,self).__init__(name) # super shortens the attribute writing process
