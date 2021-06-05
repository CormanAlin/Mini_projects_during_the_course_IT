#Exercitiul 1 Find all numbers between 2000 and 3200 which are divisible by 7 but are not a multiple of 5
i = 2000
list = []
while i < 3200:
  if i % 7 == 0 and i % 5 != 0:
    list.append(i)
  i += 1
print(list)

#Exercitiul 2 Draw a game board with the size given by the user. If the user says 3 and 4, it should look like this
# --- --- --- ---
#|   |   |   |   |
# --- --- --- ---
#|   |   |   |   |
# --- --- --- ---
#|   |   |   |   |
# --- --- --- ---
x = input("Give the row number")
y = input("Give the colum number")
top = " ---"
side = "|   "
i = 0
while i < int(x):
  print(top * int(y))
  print(side * int(x) + "|")
  i += 1
print(top * int(y))

#Exercitiul 3 Generate the first 30 numbers of the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers. First 2 numbers are 0 and 1, after that list[x] = list[x-1] + list[x-2]
#The result should be this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
x = input("How many numbers? ")
list = [0, 1]
while len(list) < int(x):
  new = list[len(list) - 1] + list[len(list) - 2]
  list.append(new)
print(list)