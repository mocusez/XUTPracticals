# Testing Part
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers = numbers + [6, 5, 3]
print(numbers)
print(5 in numbers)

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "10"
print(numbers)

# Change the last element of numbers to 1
numbers[len(numbers) - 1] = 1
print(numbers)

# Get all the elements from numbers except the first two (slice)
partnumbers = numbers[2:]
print(partnumbers)

# Check if 9 is an element of numbers
print(9 in partnumbers)
