#CALCULATOR

#Function to add two numbers

def add(a, b):

    return a + b

# function to substract two numbers

def subtract(a, b):

    return a- b

# function to multiplies two numbers

def multiply(a, b):

    return a * b

#  function to divides two numbers

def divide(a, b):

    return a/ b

print("Choose an operation to perform.")

print("1.Add")

print(".Subtract")

print("3.Multiply")

print("4.Divide")

while True:

    # take input from the user

    choice = input("Enter choice(1/2/3/4): ")

    

    if choice in ('1', '2', '3', '4'):

        try:

            num1 = float(input("Enter first number: "))

            num2 = float(input("Enter second number: "))

        except ValueError:

            print("Invalid input. Please enter a number.")

            continue

        if choice == '1':

            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':

            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':

            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':

            print(num1, "/", num2, "=", divide(num1, num2))

        

        # check if user wants another calculation

        # break the while loop if answer is no

        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation == "no":

          break

    else:

        print("Invalid Input")
