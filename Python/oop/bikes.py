# Attributes: Characteristics shared by all instances of the class type. Take our User class, for example.
# All users have a name and an email. NOUNS

# Methods: Actions that an object can perform. A user, for example, might be able to make a purchase.
# A method is like a function that belongs to a class. VERBS


class Bike(object):
  def __init__(self, price, max_speed, miles=0):
    #attributes
    self.price = price
    self.max_speed = max_speed
    self.miles = miles

  #methods
  def displaying_info(self):
    print "Current price:" + str(self.price)
    print "Max speed:" + str(self.max_speed)
    print "Total miles:" + str(self.miles)
    return self

  def ride(self):
    print "Riding"
    self.miles += 10

  def reverse(self):
    print "Reversing!"
    self.miles -= 5
    if self.miles < 0:
        self.miles = 0


huffy = Bike(200,"25 mph")
ninja = Bike(7000,"118 mph")
ducati= Bike(14000,"177 mph")


# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

huffy.ride()
huffy.ride()
huffy.ride()
huffy.reverse()
huffy.displaying_info()

ninja.ride()
ninja.ride()
ninja.reverse()
ninja.reverse()
ninja.displaying_info()

ducati.reverse()
ducati.reverse()
ducati.reverse()
ducati.displaying_info()
