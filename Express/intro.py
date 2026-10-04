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


# Python Sets

# Creating a set
fruits = {"apple", "banana", "mango", "orange"}

print("Fruits:", fruits)

# Adding an element
fruits.add("grapes")
print("After adding:", fruits)

# Removing an element
fruits.remove("banana")
print("After removing:", fruits)

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Checking membership
print("Is 3 present?", 3 in set_a)