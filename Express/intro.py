# Find the sum of digits using recursion

def sum_of_digits(n):

    # Base case
    if n == 0:
        return 0

    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)


n = int(input("Enter a number: "))

result = sum_of_digits(n)

print("Sum of digits:", result)

