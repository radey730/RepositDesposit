#NUMPY- First program - use of randint
import numpy as np
import random 
#generate a random array ranging from -5 to 5
numpy_ar=np.random.randint(10,size=10)-5

print("Original array") 
print(numpy_ar) #print the Original array
#iterate through all numpy_array elements
for i in range(0,10):
    #replaces array element with "777" if a positive integer
    if(numpy_ar[i]>0):
        numpy_ar[i]=777;
print("Second array")
print(numpy_ar) #print new array with all positive numbers replaced with 777


#Second Program - use of trigonomic functions + lens function
from random import random
import numpy as np
# create an array of angles
#initialize array of arbitrary length 
#Iterate through array with for loop 
#Use if statement to check if value is 0 
#If it is 0, set index to random value 

angles = np.array([1,2,3])
for i in range(len(angles)):
    if(angles[i]==0):
        i = random
  
# conversion of degree into radians using deg2rad function
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






#Third program - round function
in_array = np.array([.5, 1.5, 2.5, 3.5, 4.5, 10.1])
for i in range(len(in_array)):
    if in_array[i<1]:
        in_array[i] = np.random.uniform(1,10)
print ("Input array : \n", in_array)
 
round_off_values = np.round_(in_array)
print ("\nRounded values : \n", round_off_values)