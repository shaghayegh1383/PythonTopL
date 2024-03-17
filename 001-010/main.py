#why the output is like this?
print(4.9-7.0)

#This method show the type
#"class" str?
print(type('shaghayegh'))

#class int
print(type(10))

#other operators
#** power
print(3**2)

#% baghimande / kharejghesmat // kharejghesmat sahih
print( 68 % 6 )
print( 68 / 6 )
print(( 68 - ( 68 % 6 )/6 ))
#another way
print(68 // 6)
#naming variables
x = 100
y = 200
print( x + y )

#or
x , y = 100 , 100
print(y-x)


#Single and Double Quotation
sentence = "Shaghayegh said : 'Hi' "
sentence = 'Shaghayegh said : "Hello" '

#\'  \'
sentence = 'shaghayegh said : \'salam\' '
print(sentence)

courseName = 'Python'
courseName += ' course '
print (courseName)

#string interpolation => formatting strings
userName = "Shaghayegh"
userFamily = "Mousavi"
Result1 = "user name is "+ userName + " and user Family is "+ userFamily
print(Result1) 

Result2 = f" user name is {userName} and user family is {userFamily}"
print(Result2)

#string indexes
print(userName[2])

#string interpolation
myweight = 40 #int
myweightFloat = float (myweight)
print (type(myweightFloat))
print(myweightFloat) #float

