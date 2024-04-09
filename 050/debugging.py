#common pdb commands
# l --> list of your commands
# n -->next line
# c --> continue = finishes debugging
# p--> print ...


import pdb
pdb.set_trace()

number1 = int (input( 'please enter a number :'))
number2 = int (input( 'please enter a number :'))
result = number1 + number2
print (f"result is {result}")