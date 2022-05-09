#importing pathlib and shutil modules
import pathlib
import shutil
#Creates a path object that represents current working directory, and if nothing is passed to Path method path of current directory will be created
current_directory=pathlib.Path()

#Prints current directory's path
print(current_directory.cwd())

#creates a new path object for folder_week11 folder 
folder_week11=current_directory/"folder_week11"

#Creates a new directory using the path created in the prior step.
#mkdir = Path method which can be called on folder path object to create folder
folder_week11.mkdir()

#creates a path that will be used to create week11.txt text file using folder_week11 path
week11_file=folder_week11/"week11.txt"
#creates the "week11.txt" file as a blank file.
#touch is a Path method which can be called on a file Path object to create a file
week11_file.touch()
#creates a string variable that will be used to write the text to the "week_11.txt" 
content_string="Test: Writing to file."
#opeing week11.txt file in write mode 
file=week11_file.open("w")
#writes content_string to file weekfile.txt
file.write(content_string)
#closes file
file.close()
#again opening weekfile.txt in read mode to print contents of ot
file=week11_file.open("r")
#prints contents of weekfile.txt
#\n is a newline character used to print newlines 
print("\ncontents of week11.txt are:",file.read())
#closes file
file.close()

#makes a new path for creating file_backups folder using folder_week11 path
file_backups=folder_week11/"file_backups"
#creates the file_backups folder using path created in the prior step
file_backups.mkdir()

#creates path for  week11_backup.txt file using file_backups path
week11_backup=file_backups/"week11_backup.txt"
#creates week_backup.txt file using path created in the prior step
week11_backup.touch()
#copies contents of week11.txt to week11_backup.txt file using shutil copy method
#copy is a shutil funcion which copies contents of first file passed to second file passed as argument
shutil.copy(week11_file,week11_backup)


#prints names of all text files in folder_week11 and its sub-directories using Pathlib's glob method
#here folder_week11.rglob("*.txt") paths to all txt files in folder_week11 and its sub-directories
print("\ntext files in folder_week11 directory: ")
# prints all paths returned by rglob method using for loop
for file in folder_week11.rglob("*.txt"):
        print(file)
        



# importing pathlib and shutil modules
import pathlib
import shutil
#creates a path object that represents current working directory
#if nothing is passed to Path method path of current directory will be created
current_directory=pathlib.Path()
#Prints out current directory's path
print(current_directory.cwd())
#creates a new path object for folder_week11 folder 
folder_week11=current_directory/"folder_week11"
#creates a new directory using the path created in the prior step.
#mkdir is a Path method which can be called on folder path object to create a folder
folder_week11.mkdir()

#creates a path that will be used to create week11.txt text file using folder_week11 path
week11_file=folder_week11/"week11.txt"
#creates the "week11.txt" file as a blank file.
#touch is a Path method which can be called on a file Path object to create a file
week11_file.touch()
#creates a string variable that will be used to write the text to the "week_11.txt" 
content_string="Test: Writing to file."
#open week11.txt file in write mode 
file=week11_file.open("w")
#writes content_string to file weekfile.txt
file.write(content_string)
#closes file
file.close()
#again opening weekfile.txt in read mode to print contents of ot
file=week11_file.open("r")
#prints contents of weekfile.txt
#\n is a newline character used to print newlines 
print("\ncontents of week11.txt are:",file.read())
#close file
file.close()

#makes a new path for creating file_backups folder using folder_week11 path
file_backups=folder_week11/"file_backups"
#creates the file_backups folder using path created in the prior step
file_backups.mkdir()

#creates path for  week11_backup.txt file using file_backups path
week11_backup=file_backups/"week11_backup.txt"
#creates week_backup.txt file using path created in the prior step
week11_backup.touch()
#copies contents of week11.txt to week11_backup.txt file using shutil copy method
#copy is a shutil funcion which copies contents of first file passed to second file passed as argument
shutil.copy(week11_file,week11_backup)


#prints names of all text files in folder_week11 and its sub-directories using Pathlib's glob method
#folder_week11.rglob("*.txt") paths to all txt files in folder_week11 and its sub-directories
print("\ntext files in folder_week11 directory: ")
# printing all paths returned by rglob method using for loop
for file in folder_week11.rglob("*.txt"): 
        print(file)