'''''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
try:

    file1= open("sample,txt",'r')
    read1 = file1.read()
    print(read1)
    file1.close
except FileNotFoundError :
    print("These file does not exist")
finally:
    print("this is my assignment pls approve it \n" "Thank You")