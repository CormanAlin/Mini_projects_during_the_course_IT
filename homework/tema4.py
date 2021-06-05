#Exercitiul 1

list = [1, 10, 9, 8, 8, 7, 8, 11, 2, 7, 89, 8, 90, 24, 8, 5]
x = list.count(8)
print(x)

#Exercitiul 2

list = []
i = 0
while i <= 50:
    list.append(i)
    i += 1
list.reverse()
print(list)

#Exercitiul 3

list = ["a", "b", "c", "a", "d", "e", "b", "a"]
while "a" in list:
  list.remove("a")
print(list)

#Exercitiul 4

list = []
i = 123
while i <= 231:
  list.append(i)
  i += 1
print(list)

#Exercitiul 5
list = []
i = 500
while i <= 560:
  list.append(i)
  i += 2
print(list)

#Exercitiul 6
list = []
i = 999
while i >= 901:
  list.append(i)
  i -= 2
print(list)

#Exercitiul 7 calculatorul nu alege una din cele 3 variante
import random
print("Sunteti pregatiti de jocul piatra/foarfece/hartie?")
print("Va rugam selectati una din variantele de mai sus prin tastarea literei corespunzatoare")
print(" [P] - Piatra")
print(" [F] - Foarfeca")
print(" [H] - Hartie")
scor_user = 0
alegere_user = 0
scor_calculator = 0
alegere_calculator = 0
for i in range(1):
  user_choice = input("Alegerea ta este: ")
  print("Alegerea calculatorului este:" + str(alegere_calculator))
if alegere_user == alegere_calculator:
  print("Egalitate")
elif alegere_user == "P":
  if alegere_calculator == "F":
    print("Ai castigat jocul")
elif alegere_user == "F":
  if alegere_calculator == "H":
    print("Ai castigat jocul")
elif alegere_user == "H":
  if alegere_calculator == "P":
    print("Ai castigat jocul")



#Exercitiul 8
user_number = input("Give me a number between 1 and 10")
list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
is_user_input_right = False
for element in list:
  if user_number == element:
    is_user_input_right = True
    break
  if is_user_input_right:
  print("your number is between 1 and 10")
  else:
  print("number is good")

#Exercitiul 9
list = ["Timisoara", "Oradea", "Bucuresti", "Brasov", "Constanta", "Cluj"]
new_list = []
for element in list:
  new_list.append("oras " + element)
print(new_list)

#Exercitiul 10
list = [10, 99, 876, 23, -40, 78, -2000]
print(sum(list))

#Exercitiul 11
password = input("give me a password: ")
if len(password) < 10:
  print("weak")
elif len(password) > 20:
  print("strong")
else:
  print("medium")

def tema4(a, b):
  return a + b
