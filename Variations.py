#!/usr/bin/env python3.7

# Python implementation here

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

words = message.split()
print("Words", words)

sorted_words = sorted(words)
print("Alphabetic First Words:", sorted_words[0])
print("Alaphabetic Last Words:", sorted_words[-1])

