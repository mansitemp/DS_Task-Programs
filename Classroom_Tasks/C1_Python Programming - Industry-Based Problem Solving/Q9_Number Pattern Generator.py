#Program for Number Pattern Generator
#Create an increasing sequence of numbers across 5 rows
n= 5
print("Sequential number pattern: ")

#Generate each row from 1 through n
for i in range(1,6):

    #Build the sequence for the current row
    for j in range(1,i+1):
        print(j, end="")

    #Move the cursor to the next line
    print()

#Repeated Number Pattern
#Displays the row number repeatedly according to its position
print("Repeated number pattern: ")

#Determine the number of rows in the pattern
for i in range(1,6):

    #Repeat the current number based on the row position
    for j in range(1,i+1):
        print(i, end="")

    #Start a new line after completing each row
    print()