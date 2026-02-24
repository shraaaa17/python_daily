"""
Day 5 - Strings Practice
Author: Shravani
Topic: String operations
Description: Practice working with strings in Python.
"""

text = input("Enter a sentence: ")

print("\n--- String Analysis ---")

# Basic properties
print("Length of string:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])

# Case conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# Counting vowels
vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# Reversing the string
reversed_text = text[::-1]
print("Reversed string:", reversed_text)