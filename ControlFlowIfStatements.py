# Explanation: This if-else structure checks divisibility, introducing conditionals.

number = int(input("Enter a number: "))
if number % 2 == 0 and number % 5 == 0:
    print("The number is divisible by both 2 and 5.")
else:
    print("The number is not divisible by both.")
