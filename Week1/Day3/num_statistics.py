# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Accept 50 numbers from the user
numbers = []
for i in range(50):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Largest and smallest
largest = max(numbers)
smallest = min(numbers)

# Sum and average
total = sum(numbers)
average = total / len(numbers)

# Median
sorted_numbers = sorted(numbers)
mid1 = sorted_numbers[24]
mid2 = sorted_numbers[25]
median = (mid1 + mid2) / 2

# Even and odd count
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Prime count
prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

# Duplicate numbers
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Display results
print("\n===== NUMBER STATISTICS =====")
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Sum:", total)
print("Average:", average)
print("Median:", median)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Prime Count:", prime_count)
print("Duplicate Numbers:", duplicates)
print("Sorted Numbers (Ascending):", sorted_numbers)
print("Sorted Numbers (Descending):", sorted(numbers, reverse=True))