#!/usr/bin/env python3

#Author: John Marques
#Author ID: jfpessoa-marques-fil
#Date Created: 2026/05/28

str1 = 'Hello World!!'
str2 = 'Seneca College'
num1 = 1500
num2 = 1.50
 
def first_five(string):
    # Accepts a single string argument
    # Returns a string that contains the first five characters
    return string[0:5]
 
def last_seven(string):
    # Accepts a single string argument
    # Returns a string that contains the last seven characters
    return string[-7:]
 
def middle_number(number):
    # Accepts an integer as argument
    # Returns a string containing the second and third characters in the number
    return str(number)[1:3]
 
def first_three_last_three(string1, string2):
    # Accepts two string arguments
    # Returns a single string with first three chars of string1 + last three chars of string2
    return string1[0:3] + string2[-3:]
 
if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
