"""
Day 3 - Loops Practice
Author: Shravani
Topic: for loop and while loop
Description: Practice looping and number analysis.
"""

n = int(input("Enter a positive number: "))

print("\nNumbers from 1 to", n)
total = 0

# Using for loop
for i in range(1, n + 1):
    print(i, end=" ")
    total += i

print("\nSum of numbers:", total)

print("\nEven numbers:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

# Using while loop (reverse counting)
print("\n\nReverse counting:")
count = n
while count > 0:
    print(count, end=" ")
    count -= 1