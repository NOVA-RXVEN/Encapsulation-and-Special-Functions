class Computer:
    
    def __init__(self):
        self.__maxprice = 900
        
    def printPrice(self):
        print(f"Selling Price: {self.__maxprice}")
        
    def setMaxPrice(self, price):
        self.__maxprice = price
        
c = Computer()
c.printPrice()

c.__maxprice = 1500
c.printPrice()

c.setMaxPrice(15000)
c.printPrice()