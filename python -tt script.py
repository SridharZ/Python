import random
import sys
import os



Input = str(input('Enter name'))
rev = (Input)[::-1] #reverse the string
if Input == rev:
    print(rev, 'is an palindrome')
else:
    print(rev,'is Aint palindrome')











