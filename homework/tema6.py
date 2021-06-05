#Exercitiul 1 Are the following if statements True or False:
a = True and False
print(a)
b = False or True
print(b)
c = 10 >= 10 and 67 > 66
print(c)
d = 10 < 10 and 10 >= 9
print(d)
e = -1 < -2 or -2 > -1
print(e)
f = True or False and True
print(f)
g = True and False or False and True
print(g)
h = not True and not False
print(h)
i = not True or True
print(i)
j = False and not False
print(j)

#Exercitiul 2 What values should x,y have so the following if statements are True? What about False?
x = 10
a =  x > 6 and x < 12
print(a)
x = 13
a = x > 6 and x < 12
print(a)

x = 11
y = 12
b = x > 10 or y > 10
print(b)
x = 9
y = 10
b = x > 10 or y > 10
print(b)

x = 8
c = x < 9 or True
print(c)
x = 10
c = x < 9 or True
print(c)

y = 100
d = y > 99 and False
print(d)
y = 98
d = y > 99 and False
print(d)

x = 9
e = x > 10 and x < 10
print(e)
x = 11
e = x > 10 and x < 10
print(e)

x = False
f = not x
print(f)
x = True
f = not x
print(f)

x = 9
g = x > 10 or x < 10
print(g)
x = 11
g = x > 10 or x < 10
print(g)

x = 16
y = 50
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)
x = 11
y = 90
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)

#Exercitiul 3 Exercises with lists
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
#a. eliminate all elements from list3
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
print(list1, list2, list3)
list3.clear()
print(list3)
#b. eliminate all 3 from list1
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
print(list1, list2, list3)
list1.remove(3)
print(list1)
#c. sort list1 from the biggest number to the lowest
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
print(list1, list2, list3)
list1.sort(reverse=True)
print(list1)
#d. sort list2 without "Zz"
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
print(list1, list2, list3)
list2.remove("Zz")
list2.sort()
print(list2)
#e. make list3 in the recverse order
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
print(list1, list2, list3)
list3.reverse()
print(list3)
#f. eliminate last 3 elements from list 2, last element from list3 and last 2 elements from list1
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
print(list1, list2, list3)
list2.pop(), list2.pop(), list2.pop()
print(list2)
list3.pop()
print(list3)
list1.pop(), list1.pop()
print(list1)
#g. how many "b" values are in list2
list1 = [1, 3, 45, -7, 89, 1, 12, 33, 1]
list2 = ["a", "cd", "b", "b", "f", "oj", "Zz"]
list3 = [1, 2, "a", 34, "bgh", "#"]
print(list1, list2, list3)
list2 = list2.count("b")
print(list2)

#Exercitiul 4 Exercises with dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 'A'}
#a.remove last element
print(dict1)
dict1.popitem()
print(dict1)
#b. print all keys for the values above 2
for key,value in dict1.items():
  if value > 2:
    print(key)
#c. remove all keys for the values above 2
keys_to_be_removed = []
for key,value in dict1.items():
  if value > 2:
    keys_to_be_removed.append(key)
for key in keys_to_be_removed:
  dict1.pop(key)
print(dict1)
#d. print all the values remaining
print(dict1.values())
#e. remove all remaining elements from dict
dict1.clear()
print(dict1)

#Exercitiul 5 Make a "piatra, foarfece, hartie" game.
while True:
  x = input("Foarfece, piatra sau hartie?")
  if x.split().lower() == "stop":
    break
  else:
    print("Please select a valid option")


#Exercitiul 6
import random
while True:
  user_guess = input("Guess a number between 100 and 199: ")
  if user_guess == "stop":
    break
  elif not user_guess.isdigit():
    print("please enter a number")
  elif int(user_guess) < 100:
    print("Your number in below 100")
  elif int(user_guess) > 199:
    print("Your number is above 199")
  else:
    print("You need to enter a number")
  computer_guess = random.randint(100, 199)
  print("Computer guessed " + str(computer_guess))






