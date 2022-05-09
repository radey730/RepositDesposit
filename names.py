names_list=['Frank Harrelson', 'Bob Charles', 'Bob Franklin', 'Bob Brody', 'Frank Charles', 'Bob Harrelson', \
'Mack Dobson', 'John Jones', 'Rob Franklin', 'Tom Simpson', 'Rob Harrelson', 'John Brody', \
'Frank Jones', 'John Harrelson','Frank Charles', 'Tom Charles', 'Frank Franklin', 'Frank Charles', \
'John Charles', 'John Franklin', 'Frank Dobson', 'Diane Jones', 'Bob Dobson', 'Tom Harrelson', \
'Rob Simpson', 'Tom Brody', 'Rob Harrelson', 'John Charles', 'Bob Dobson', 'Bob Brody']
#list of names

names=[n.split(" ") for n in names_list] #makes it easily passable to lambda function

print("Names are", names) #prints list of names

sorted_names = sorted(names, key = lambda x:x[1]) # sorts list according to the last name

print("Sorted names according to last name", sorted_names) #prints new list of names after being sorted through

five_two= list(map(lambda x:x[1][0:5]+x[0][0:2], names)) # creating user id with 5 characters of last name and 2 characters of first name.

print("User names are",five_two) #prints user names