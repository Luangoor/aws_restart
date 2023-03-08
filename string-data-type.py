myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print("_"*50)
firstString = "El agua"
secondString = " moja."
thirdString = firstString + secondString
print(thirdString)
print("_"*50)
name = input("What's your name? ")
#print(name)
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))