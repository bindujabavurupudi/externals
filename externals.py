print ("To find the sum of squares of two numbers.")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1Square = num1 * num1
num2Square = num2 * num2
print ("The square of ", num1, " is ", num1Square, ".", sep="")
print ("The square of ", num2, " is ", num2Square, ".", sep="")
sum = num1Square + num2Square
print ("The sum of the squares of ", num1, " and ", num2, " is ", sum, ".", sep="")