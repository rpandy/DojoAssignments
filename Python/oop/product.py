class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sellItem(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price = self.price + (self.price * tax)

    def returnedItem(self,reason):
        self.status = reason
        if self.status == "defective":
            self.price = 0
        elif self.status == "returned in box":
            self.status = "for sale"
        elif self.status == "opened box":
            self.price = self.price - (self.price * .20)
        return self

    def displayInfo(self):
        print "Price:" + str(self.price)
        print "Item Name:" + str(self.item_name)
        print "Weight:" + str(self.weight)
        print "Brand:" + str(self.brand)
        print "Cost:" + str(self.cost)
        print "Status: " + str(self.status)
        return self

basketball_shoes = Product(200, "Jordan 4s", "16 oz", "Jordan", 40)

# basketball_shoes.returnedItem("defective")
# basketball_shoes.addTax(.08)
basketball_shoes.sellItem().displayInfo()
