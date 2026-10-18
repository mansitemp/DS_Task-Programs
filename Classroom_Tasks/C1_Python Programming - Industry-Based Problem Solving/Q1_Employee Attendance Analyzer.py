#Program for Employee Attendance Analyzer
#Initialize variables as counters
total_days=int(input("Enter total working days: "))
present_days=0
absent_days=0

#Record the employee's attendance for each working day
for a in range(1,total_days+1):
    attendance=int(input("Enter your attendance as 1 for present and 0 for absent: "))
    if attendance==1:
        present_days +=1
    elif attendance==0:
        absent_days +=1
    else:
        print("Invalid input!")
        invalid= True
        break

#Perform calculations only when all inputs are valid
if invalid== False:

    #Calculating total present days
    total_present_days= total_days-absent_days
    print("Total present days: ",total_present_days)

    #Calculating total absent days
    total_absent_days= total_days-present_days
    print("Total absent days: ",total_absent_days)

    #Calculating attendance percentage
    attendance_percentage=(total_present_days/total_days)*100
    print("Employee's attendance percentage: ",attendance_percentage,"%")

    #Employee needs atleast 75% attendance to be eligible for bonus
    if attendance_percentage>=75:
        print("Employee is eligible for bonus")
    else:
        print("Employee is not eligible for bonus")