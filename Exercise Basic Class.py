"""
Write a Python class,

MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.

Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type

If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class
"""

class MedPlus:
    def __init__(self,name = str,batch = int,price = float):
        self.name = name
        self.batch = batch
        self.price = price
    def valid(self):
        if type(self.name) == str and type(self.batch) == int and type(self.price) == float:
            return "Valid"
        else:
            return "Invalid Input"
name =input()
batch = (input())
price = (input())
A = MedPlus(name,batch,price)
print(A.valid())
        