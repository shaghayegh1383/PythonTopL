print (" How many kilometers do you want to convert? ")
#kms / 1.60934  "50"/1.60934
kms = input()

miles = float (kms) / 1.60934

#round(miles,n) n=>tedad ragham ashar
miles = round (miles,3)

print (f"{kms} km is {miles} miles")