# Python code to demonstrate trigonometric function
from random import random
import numpy as np
  
# create an array of angles
#angles = np.array([0, 30, 45, 60, 90, 180]) 

#initialize array of arbitrary length 
#Iterate through array with for loop 
#Use if statement to check if value is NIL or 0 
#If it is NIL or 0, set index to random value 

angles = np.array([1,2,3])
for i in range(len(angles)):
    if angles[i]:
        i = random
  
# conversion of degree into radians
# using deg2rad function
radians = np.deg2rad(angles)

# sine of angles
print('Sine of angles in the array:')
sine_value = np.sin(radians)
print(np.sin(radians))
  
# inverse sine of sine values
print('Inverse Sine of sine values:')
print(np.rad2deg(np.arcsin(sine_value)))
  
# hyperbolic sine of angles
print('Sine hyperbolic of angles in the array:')
sineh_value = np.sinh(radians)
print(np.sinh(radians))
  
# inverse sine hyperbolic 
print('Inverse Sine hyperbolic:')
print(np.sin(sineh_value)) 
  
# hypot function demonstration
base = 4
height = 3
print('hypotenuse of right triangle is:')
print(np.hypot(base, height))












#Load numpy and create a random 2D array of size 5x4 with numbers between -5 and 5 using random.rand() function. 
# Then write a double nested for loop (a for loop within a for loop) and also use an if statement to replace all positive numbers in the array with 20.
from random import random
import numpy as np
#actually random.randint(10,size=(5,4)) produce the number from 0 to 10, so by subtracting 5 from it, then it will produce -5 to 5
numpy_array=np.random.randint(10,size=(5,4))-5
#print the Original array
print("Original numpy")
print(numpy_array)
#traverse through all numpy_array elements row
for i in range(0,5):
    #traverse through all columns
    for j in range(0,4):
        #if the element is positive then replace it with 20
        if(numpy_array[i][j]>0):
            numpy_array[i][j]=20;
#print after replacement
print("After replace")
print(numpy_array)







#Third program
#Create a list that contains 10 numbers of your choice with values between 0 and 10. 
# Write a while loop and also use an if statement to replace all numbers which are below 5 with a -5.
#declaring the user_list
user_list=list()
#prompting the user for 10 elements
print("Enter 10 elements that you want between 0 to 10 :")
#loopin till 10
for i in range(0,10):
    #prompting the user and reading the number into element
    element=int(input("Enter number:"))
    #append the element to list
    user_list.append(element)
#print the Original array
print("Original numpy")
print(user_list)
i=0;
#whiule loop till length of user_list
while(i<len(user_list)):
    #if the element is less than 5, then replace it by -5
    if(user_list[i]<5):
        user_list[i]=-5
    i=i+1
#print after replacement
print("After replace")
print(user_list)

#From Function
#Using python, make a 100 x 100 matrix using the following methods:

import numpy as np 


A = [] #matrix that will be filled using for loops
for i in range(100): #for loop with range of 100
    A.append([]) #fills matrix
for j in range(100): #for loop with range of 100
    A[i].append(1) #fills matrix

print(np.array(A)) #print the matrix

#use shape = (100, 100) to create the matrix, use any lambda expression you like
B = np.fromfunction(lambda i, j: i+j, (100, 100), dtype=int)
print(B)

#x needs shape (100, 1) for broadcasting to work
x = np.ones((100, 1))
y = np.ones(100)
C = x + y
print(C)