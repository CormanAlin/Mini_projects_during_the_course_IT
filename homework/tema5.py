#Exercitiul 1
import sys
args = sys.argv
# print(args)
numbers = args[1:]
# print(numbers)
def is_number(value):
  try:
    int(number)
    return True
  except:
    return False
sum = 0
for number in numbers:
  if is_number(number):
    sum += int(number)
print(sum)

#Exercitiul 2
x = input(" Enter a number between 50 and 100\n")
print(x)
try:
  number = int(x)
  if number < 50:
    print("Your number is below 50")
  elif number > 100:
    print("Your number is above 100")
  else:
    print("Good job")
except:
  print(" You should enter a number")

#Exercitiul 3 pentru a face from ex3 sau alt nume trebuie sa denumim un fisier separat cu acelasi nume unde punem def-ul apoi in altul punem from
def is_even(number):
  if int(number) % 2 == 0:
    return False
  else:
    return True

from ex3 import is_odd
x = input("Give me a number: ")
if is_odd(x):
  print("Impar")
else:
  print("Par")

#Exercitiul 4
import random
while True:
  user_guess = input("Guess number between 1 and 10")
  if user_guess == "STOP":
    break
  computer_guess = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  print("Computer guessed " + str(computer_guess))

