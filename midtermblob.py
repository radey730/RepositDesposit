#Second Program - use of trigonomic functions + lens function
import numpy as np
from random import randint, random
#If it is 0, set index to random value 
# create an array of angles
angles = np.array([0,1,3])
#Iterate through array with for loop 
for i in range(len(angles)): 
    if(angles[i]==0): #Use if statement to check if value is 0 
        (angles[i])=randint(1,10) #replaces 0 with random value
  
print(angles)
# conversion of degree into radians using deg2rad function
radians = np.deg2rad(angles)

# sine of angles
print("Sine of angles in the array:")
sine_value = np.sin(radians)
print(np.sin(radians))