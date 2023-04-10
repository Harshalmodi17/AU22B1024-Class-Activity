"""
Write a Python class,

MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class
"""

class MedPlus:
    def __init__(self, name: str, batch: int, price: float):
        try:
            if type(name) != str:
                raise TypeError("Name should be a string")
            if type(batch) != int:
                raise TypeError("Batch number should be an integer")
            if type(price) != float:
                raise TypeError("Price should be a float")
        except TypeError as e:
            print(f"Error: {e}")
            return
        self.name = name
        self.batch = batch
        self.price = price
        
    def set_name(self, name: str):
        try:
            if type(name) != str:
                raise TypeError("Name should be a string")
        except TypeError as e:
            print(f"Error: {e}")
            return
        self.name = name
        
    def set_batch(self, batch: int):
        try:
            if type(batch) != int:
                raise TypeError("Batch number should be an integer")
        except TypeError as e:
            print(f"Error: {e}")
            return
        self.batch = batch
        
    def set_price(self, price: float):
        try:
            if type(price) != float:
                raise TypeError("Price should be a float")
        except TypeError as e:
            print(f"Error: {e}")
            return
        self.price = price
    def get_name(self):
        return self.name
    
    def get_batch(self):
        return self.batch
    
    def get_price(self):
        return self.price
        