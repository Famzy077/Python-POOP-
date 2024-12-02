class store:
    def __init__(self, fruit, liquid, jeweries, gadget):
        self.fruit = fruit
        self.liquid = liquid
        self.jeweries = jeweries
        self.gadget = gadget
    
    def buy(self): 
        print('I bought' + ' ' + storeDetails.jeweries + ' '+'last night')
    # buy()
storeDetails = store('Mango', 'Veleta_Wine', 'Diamond', 'Mac-Book pro')
print(storeDetails.fruit)
print(storeDetails.liquid)

storeDetails.buy()