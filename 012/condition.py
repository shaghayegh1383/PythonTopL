#condition
#also you can use "is" instead of ==

print ("Enter your Rank :")
userRank = int(input())
if userRank == 1:
    print ("You got Gold medal")
elif userRank == 2:
    print ("You got Silver medal")
elif userRank == 3:
    print ("You got Bronze medal")
else:
    print("You got no medal")

#difference between == and is
list_1 = [ 'a' , 'b' , 'c' ]
list_2 = list_1
list_3 = list(list_1)

print(list_1)
print(list_2)
print(list_3)

#The == operator => values are equal
print(list_1 == list_2)
print(list_1 == list_3)

# The is operator => point to the same object
print(list_1 is list_2)
print(list_1 is list_3)