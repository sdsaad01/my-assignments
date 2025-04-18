'''''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''

student = { 
     'Ram' : 89, 
     'Sham' : 85,
     'raju' : 78,
     'Henry':70 
    }
studenm = input("Please input the name of student : ")
if studenm in student :
    print("mark's of {} : {}".format(studenm,student[studenm]))
else:
    print("student name not found ..")


"""""
problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
num = [1,2,3,4,5,6,7,8,9,10]
a= num[0:5]
b= a[::-1]
print("original list =" , num)
print("Extracted list ", a )
print("Reverse list of extracted one ",b)