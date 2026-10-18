#Program for Employee Performance Analyzer
#Set up the values for highest and lowest score
highest_score = 0
lowest_score = 100

#Repeat the evaluation for each of the 6 employees
for i in range(1, 7):

    # Read the employee's performance score from the user
    score = int(input("Enter performance score: "))

    #Assign a performance category according to the score
    if score >= 90:
        category= "Excellent"
    elif score >= 75:
        category= "Good"
    elif score >= 50:
        category= "Average"
    else:
        category= "Poor"

    #Display the employee's score classification
    print("Employee", i, ":", category)

    #Compare and store the highest score recorded so far
    if score > highest_score:
        highest_score = score

    #Compare and store the lowest score recorded so far
    if score < lowest_score:
        lowest_score = score

#Display the final performance results
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)