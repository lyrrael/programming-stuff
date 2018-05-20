start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
  number = (number ** 2)
  square_list.append(number)

square_list.sort()


print square_list
