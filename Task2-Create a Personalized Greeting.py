"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""
__author__ = "Sumit Srivastava"
__copyright__ = "Sumit Srivastava"
__email__ = "sumit.srivastava56@gmail.com"
__date__ = "01-05-2026 [DD-MM-YYYY]"

import email

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
full_name = first_name + " " + last_name
print("Hello", full_name+"! Welcome to the Python Program")
