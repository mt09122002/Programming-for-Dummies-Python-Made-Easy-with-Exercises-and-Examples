# Explanation: Defines a function to calculate factorial, demonstrating function usage.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial(number)}")
