i = 0
lis = []

## To get 10 integers
while i < 10:				# Loop to ensure 10 numbers are inputted
    x = input("Please enter an integer:")
    try:               			# try block to ensure user entered integers only
        y = int(x)
        lis.append(y)
        i = i + 1
    except:
        print("You did not input a valid integer. Only integer is allowed.")
        continue

## To display entered integers
print("You have entered following numbers:")
for i in range(len(lis)):       	# for loop to print numbers in the list one-by-one
    print(lis[i])

## To find minimum
index = 0
min = lis[index]

while index < 10:              		# Loop to compare all the numbers to find minimum
    if min > lis[index]:
        min = lis[index]
    index = index + 1
print("Minimum Number is:", min)

## To find maximum
index = 0
max = lis[index]

while index < 10:              		# Loop to compare all the numbers to find maximum
    if max < lis[index]:
        max = lis[index]
    index = index + 1
print("Maximum Number is:", max)

## To calculate Range
num_range = max - min         		# Range is difference between Maximum and Minimum number
print("Range of the inputted numbers:", num_range)

## To calculate Mean of all numbers 
add = 0

for i in range(len(lis)):       	# for loop to get the sum of numbers in the list
    add = add + lis[i]

mean = add/len(lis)
print("Mean of the inputted numbers is:", mean)

## To calculate Variance
sum = 0

for i in range(len(lis)):        	# for loop to get the sum of squared differences from the mean
    sum = sum + (lis[i] - mean)**2

var = sum/len(lis)
print("Vaiance of the numbers is:", var)

## To calculate Standard Deviation
sd = var**0.5                    	# Standard deviation is square root of variance
print("Standard Deviation is:", sd)
