# 2. User Input Data Processor
#Objective: The aim of this assignment is to process and format user input data.

#Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
#Both should be at least 2 characters long. If not, print an error message.

print("Welcome to the input length validator. Let's see how many characters are in your name!")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

def count_characters(first_name, last_name):
    first_name_count = len(first_name)
    last_name_count = len(last_name)
    if first_name_count < 2:
        return print("\nError, first name must be more than 2 characters long. Please try again")
    if last_name_count < 2:
        return print("\nError, last name must be more than 2 characters long. Please try again")
    if first_name_count and last_name_count > 2:
        return print(f"\nYour first name has {first_name_count} characters and your last name has {last_name_count} characters.")

count_characters(first_name, last_name)