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
# Step 1: Writing user input to output.txt
with open("output.txt", "w") as file:
    user_input = input("Enter text to write to file: ")
    file.write(user_input + "\n")

# Step 2: Appending additional data
with open("output.txt", "a") as file:
    additional_input = input("Enter additional text to append: ")
    file.write(additional_input + "\n")

# Step 3: Reading and displaying the final content
with open("output.txt", "r") as file:
    content = file.read()

print("\nFinal content of the file:")
print(content)