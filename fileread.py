"""
NEW FILE ITERATING : WORKING
"""
# IN this code we will try to creat a file using for loop
from sys import argv
script, filename = argv
print(f"So, according to {script} you have a filename {filename}. ")
print("Would you like to put change in it? Y/N ")
ans = input("> ")
if ans == "Y":
    target = open(filename, 'w')
    print(f"You can enter 3 lines in {filename}") # here line has too much repeatition
    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")
    lines = [line1, line2, line3,]
    for line in lines:
        target.write(line)

    target.close()

    can_read = open(filename, 'r')
    print(can_read.read())
else:
    print("Do you wish to create a new file? Y/N ")
    response2 = input("> ")
    if response2 == "Y":
        filename2 = input()
        print("Please suggest a filename: ", filename2 )
        print(f"So, your filename is {filename2}")
        new_file = open(filename2, 'x')
        print("Now you can add 2 lines in the file.")
        line1_new = input("line 1: ")
        line2_new = input("line 2: ")
        space = "\n"
        new_file.write(f"{line1_new} {space} {line2_new} {space}")
        print("Wait a sec....ok done!")
        print("Here is your file")
        new_file.close() #it will save edited text don't use
        #filename2 as it is a string andstring has no attribute

        read_it = open(filename2, 'r') #we use this here to get it back to default readable function:
        print(read_it.read())