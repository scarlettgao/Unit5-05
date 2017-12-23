# Created by: Scarlett Gao
# Created on: Nov 2017
# Created for: ICS3U
# This program displays finding the average of a 2D array with random numbers

from numpy import random

def two_dimesion_loop_average(array):
    # finds average in passed 2D array
    total = 0
    
    for row in array:
      for column in row:
          total = total + column
    average = total / (len(array[0]) * len(array))
    
    return average

rows_number = int(raw_input('Enter desired number of rows: '))
if rows_number < 0:
    rows_number = int(raw_input('Invalid number'))
else:
    pass

columns_number = int(raw_input('Enter desired number of columns: '))
    
table = []

for rows in range(0, rows_number):
    table.append([])
    for columns in range(0, columns_number):
        table[rows].append(random.randint(0, 50+1))
        
average_of_elements_table = two_dimesion_loop_average(table)

print(table)
print('The average of the numbers in the table is ' + str(average_of_elements_table) + '.\n')
