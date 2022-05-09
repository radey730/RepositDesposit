import numpy as np
from random import randint

#NUMPY- First program - use of randint function
#generate a random array ranging from -5 to 5
numpy_ar=np.random.randint(10,size=10)-5

print("Original array:") 
print(numpy_ar) #print the Original array
#iterate through all numpy_array elements
for i in range(0,10):
    #replaces array element with "777" if a positive integer
    if(numpy_ar[i]>0): #checks if array element is above 0
        numpy_ar[i]=777; #replaces positive array element with 777
print("Second array:")
print(numpy_ar) #print new array with all positive numbers replaced with 777






#Second Program - use of trigonomic functions 

import numpy as np
from random import randint
#If it is 0, set index to random value 
# create an array of angles
angles = np.array([0,1,3])
#Iterate through array with for loop 
for i in range(len(angles)): 
    if(angles[i]==0): #Use if statement to check if value is 0 
        (angles[i])=randint(1,10) #replaces 0 with random value
print("angles array:")
print(angles)

#use deg2rad function
radians = np.deg2rad(angles) #conversion of degree into radians 

print("Sine of angles in the array:")
sine_value = np.sin(radians) # sine of angles
print(sine_value)
  
print("Inverse Sine of sine values:")
print(np.rad2deg(np.arcsin(sine_value))) # inverse sine of sine values
  


#Third program - round function
float_ar = np.array([.5, 1.5, 2.8, 3.5, 4.3, 10.1]) #generates an array of floats
for i in range(len(float_ar)): #iterates through the array
    if (float_ar[i]<1): #checks if array element is less than 1
        float_ar[i]=np.random.uniform(1.0,10.0) #replaces element less than 1 with a random float, ranging from 1.0 to 10.0
print ("Unrounded array")
print(float_ar) #prints array after replacing elements that are less than 1
 
round_ar = np.round_(float_ar) #rounds all elements in float_ar and stores new array in 
print ("Rounded values")
print(round_ar) #prints new array with rounded values