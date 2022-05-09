#program that reads input, stops after input of 'q' and computes averages of inputted numbers
#outputs sum, count, and averages of inputted numbers 
 
sum_num = 0
count_num = 0
 
while True: #program to input numbers will run unless q is inputted 
    num_entered = input("Enter a num_entered, or press q to stop: ") #user is supposed to input numbers or 'q' to stop 
    if num_entered =='q': #reads if 'q' is entered
        break #stops the program only when 'q' is read as the input
    num_entered = int(num_entered) #so that the sum is calculated by the value of number-input, not the count
    count_num += 1 #count of numbers inputted
    sum_num += num_entered #sum of the value all numbers entered
    avg_num = sum_num / count_num #averages computed by sum and count of numbers inputted
    
print(f"The sum of the input is: {sum_num}" ) #prints the message that the sum of the numbers is whatever it was calculated to be
print(f"The average of the input is: {avg_num}" ) #prints the message that the average of the numbers is whatever it was calculated to be
print(f"The count of the input is: {count_num}" ) #prints the message that the count of the numbers is whatever it was calculated to be
 
#IT WORKSSS!!! 