def minicalc(numbers):   #function to calculate the sum of numbers in the array
   total = 0          #the variable will start at 0
   for number in numbers:
      total += number       #adds the inputed numbers
   return total

#get the amount of numbers to calculate
numNums = int(input("How many numbers would you like to sum? "))

#the array of numbers to sum together
numbers = []

#getting the numbers TO calculate
for i in range(numNums):
   num = float(input(f"Number #{i + 1} to sum: "))
   numbers.append(num)  #stores all the numbers the user inputs


numSum = minicalc(numbers) #calls the previous function
print(f"The sum is: {numSum}")
