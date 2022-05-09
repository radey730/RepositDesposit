def fare_calculator(kilometers,base): 
#calculate the fare
    z=kilometers*1000 #multiply kilometers x 1000 to find meters
    z=z//140 #take your result from the previous answer and divide it by 140 
    z=z*0.25 #take the new result and multiply it by 0.25
    x=base+z #add base and z to find x 
    return x
kilometers=float(input("Enter total kilometers: ")) #enter the amount of kilometers traveled 
base=4.00 #constant base
print("The total fare is {:.2f}".format(fare_calculator(kilometers,base))) #prints the total fare (cost)