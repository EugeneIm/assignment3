class Car:
    def __init__(self, make, model, year, cost, price):
    
        '''
        Initialize the car details
        '''
        
        self._make = make
        self._model = model
        self._year = year
        self._cost = cost
        self._price = price

    def calc_profict(self):
        '''
        Returns the projected profit. 
        '''
        return self._price - self._cost
    
    def get_details(self):
        pass
        #Returns a formatted string with the car details. The string should look like:

        #2015 Honda Civic for sale for $9999.99

    
    def reduce_price(self, reduction):
        #reduce the value of (self._price) by the reduction amount.
        #i.e. subtract reduction from the price value
    

    