class Calculator:
    def sum (self , a , b):
      return a + b
  
    def subtract (self , a , b):
      return a - b
  
    def multiply (self , a , b):
      return a * b
  
    def division (self , a , b):
      return a / b
  
myCalc = Calculator()

print (myCalc.division(6 , 2))