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


'''''
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
 

'''
inp = input("type what you want to add in file : ")
file1= open("output.txt" + inp ,'a')
read1 = file1.read()
print(read1)
file1.close()
# the text file is not present in pc so showing the error
# and how to add in input i dont know so can you help me
# unable to create the file in vs code sorry 