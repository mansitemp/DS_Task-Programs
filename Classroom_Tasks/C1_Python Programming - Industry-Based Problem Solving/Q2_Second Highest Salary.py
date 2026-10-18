#Program for Second Highest Salary
#Set counters
highest=0
second_highest=0

#Accept salary details for 5 employees
for n in range(1,6):
    salary= float(input("Enter salary of employee: "))

    #Compare and update salaries
    if salary>highest:           #For highest salary
        second_highest=highest
        highest=salary
    elif salary>second_highest:  #For second highest salary
        second_highest=salary

#Display the results
print("Highest salary: ", highest)
print("Second highest salary: ", second_highest)