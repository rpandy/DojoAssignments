class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12

    def setTax(self):
        if self.price > 10000:
            self.tax = .15

    def display_all(self):
        print "Price:" + str(self.price)
        print "Speed:" + str(self.speed)
        print "Fuel:" + str(self.fuel)
        print "Mileage:" + str(self.mileage)
        print "Tax:" + str(self.tax)

accord = Car(25000, "45 mph", "Full", "45mpg")
civic = Car(8000, "25 mph", "Not Full", "45mpg")
model_s = Car(50000, "85 mph", "Full", "45mpg")
corolla = Car(13000, "35 mph", "Not Full", "45mpg")
golf = Car(7000, "75 mph", "Empty", "45mpg")
gti = Car(25000, "95 mph", "Half", "45mpg")


#where do we put the return self statement in order to chain methods

accord.setTax()
accord.display_all()

civic.setTax()
civic.display_all()

model_s.setTax()
model_s.display_all()

corolla.setTax()
corolla.display_all()

golf.setTax()
golf.display_all()

gti.setTax()
gti.display_all()
