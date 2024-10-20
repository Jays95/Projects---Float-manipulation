import math
# List that would store all the floats
numbers=[]
# Prompt the user to enter 10 floats 
for i in range(10):
# prompt user to enter a float of various numbers     
    num = float(input(f"Enter a float number {i+1}:"))
    numbers.append(num)
    
# Find the total of all the numbers 
total = round(sum(numbers),2)
print(f"Total : { total}")

# Find the index of the maximum number aswell as the max number that was entered
max_num = max(numbers)
print(f"This is our max number: {max_num}")
max_index = numbers.index(max_num)
print(f"Index of the maximum amount of number: {max_index}") 

# Find the index of the minimum number and the mininum number entered
min_num = min(numbers)
print(f"This is our min number: {min_num}")
min_index = numbers.index(min_num)
print(f"Index of minimum number : {min_index}")

# Calculating the average and round off to two decimal places 
average = round(sum(numbers)/len(numbers),2)
print(f"Average (rounded to 2 decimal places): {average}")    

# Find the median number
sorted_numbers = sorted(numbers)
if len(sorted_numbers) % 2 == 0: 
    median_1 = sorted_numbers[len(sorted_numbers)//2 - 1]
    median_2 = sorted_numbers[len(sorted_numbers)//2]
    median = (median_1 + median_2)/2   
else:
    median= round(sorted_numbers[len(sorted_numbers)//2],2)
print(f"Median : {median}")