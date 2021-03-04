my_favorite_animal = 'flying squirrel'
my_favorite_number = 10
#print(type(my_favorite_animal))
#print(my_favorite_animal)

#Numbers
#print(5*2)
#print(30 // 5)  
#inter division see repo for more examples

#Strings
name= "John"
#print(type(name))
#print(name)
full_name="John\nDoe"
#print(full_name)
middle_name = 'O\'riely'
#print(middle_name)

#print(name * 3)

#mixing classes - string # - interpolation
#format okay not best
class_number = 22

#print("I am teaching WDI {}.".format(class_number))
#best - f tells to import variable into {}
class_number = 29
#print(f"I am teaching SEI {class_number}.")

#Booleans
#double == is more strict in Python, not === like JavaScript
#print(2==2)
x=10
y=20
#print(x==10 and y==20)
#print(x==10 or y==30)
#print(not(x==10 and y==20))  #is opposite with not

#None - equivalent to null
#print(type(None))

#Conditionals
#height=int(input('How tall are you?')) #Input value in console

#if height < 4:
#    print('too short')
#elif height > 4 and height < 7:
#    print('you are good')
#else:
#    print('too tall')

#input - prompts user for an input 
#like a method such as input(prompt)

#Bouncer
#age = int(input("What is you age?"))
#print(age)

#if age >= 21:
#   print('welcome')
#elif age >= 18:
#    print('in, don\'t drink')
#else:
#    print('cannot come in')
    
#print (2 ** 3)
#print(((16 / 4) * (2 + 1)) ** 2)     
#print(("a milli " + "a milli ") * 3)
#print(("a milli " * 4) / 2)
#my_favorite_number = 13
#print(f"My favorite number is: {my_favorite_number}")  

#my_favorite_number = 13
#print("My favorite number is: {}".format(my_favorite_number))

#print(False==False)

#age = input()
#if age:
#    print("My age is: " + age)

#List - collection of related values
#number = [1, 2, 3]
# print (type(number)) # class list
# print (number)
# number.append(4)
# print (number)
# number.pop()
# print (number)
# print (number[0])
# number.pop(0)
# print (number)
# number.extend(number)
# print (number)
#print(number)
#dir(number)  suppossed to give operations you can use

# vowels = ['a', 'i', 'u', 'e']
# vowels.insert(3,'o')
# print(vowels)
# vowels = sorted(vowels)
# #sorted(vowels)
# print(sorted(vowels))
# print (vowels)

# numbers = [3, 4, 5]
# numbers.remove(3)  #removes first matching number
# print(numbers)

#Dictionary - like an object
sei_class= {
  "teacher": "Jimmy",
  "students": ["Yacko", "Wacko", "Dot"],
  "classroom": 2,
  "in_session": True,
  "schedule": {
    "morning": "Python Basics",
    "afternoon": "Enumerables"
  }
}
# print(sei_class['teacher'])
# print(sei_class['schedule'])
# #print(dir(sei_class))
# print(sei_class['schedule']['afternoon'])

#Keys
# print(sei_class.keys()) #show me
# print(list(sei_class.keys())) # give me an actual list

#Ranges - generate lists of numbers
# inclues first number but not last
# do not need starting point, will start at zero
#print(list(range(1,10)))
# Loops
# for i in range(1, 10):
#     print(i)
#add step
# for i in range(1, 10, 2):
#     print(i)

#length
#print(len(sei_class))  #gives 5, highest level

# planeteers = ["Earth", "Wind", "Captain Planet", "Fire", "Water"]
# rangers = ["Red", "Blue", "Pink", "Yellow", "Black"]
# #print(planeteers[2])

# planeteers.append('Heart')
# print(planeteers)

# planeteers.extend(rangers)
# print(planeteers)

#Functions

    # def - the Python equivalent of function
    # double - the function name in the above example
    # number - the parameter name in the above example
    # Use a : instead of curly brackets {}

# def double(number):
#     return number * 2

# print(double(3))

# def double(number=5):
#     return number * 2

# print(double())

# def verify(number):
#     if (number>0):
#         print('it is positive')
#     else:
#         print('it is negative')
        
# verify(3)

temperature = input('What is your temperature?')
unit = input('What the unit, F, C or K ?')


if unit == ("f" or "F"):
  converted_to_C = (int(temperature) - 32)/1.8
  converted_to_K = (int(temperature) +459.67)/1.8
  print('Temperature in Celcius:', converted_to_C)
  print('Temperature in Kelvin:', converted_to_K)
elif unit == ("c" or "C"):
  converted_to_F = (int(temperature)*1.8)+32
  converted_to_K = (int(temperature) +273.15)
  print('Temperature in Fahrenheit:', converted_to_F)
  print('Temperature in Kelvin:', converted_to_K)
else:
  converted_to_C = (int(temperature) -273.15)
  converted_to_F = (int(temperature)*1.8)-459.67
  print('Temperature in Celcius:', converted_to_C)
  print('Temperature in Fahrenheit:', converted_to_F)












