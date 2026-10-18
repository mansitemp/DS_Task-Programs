def analyze_marks(*marks):
    sum=0
    highest=0
    passing_marks_count=0

    for mark in marks:
        sum +=mark
        if mark>=highest:
            highest=mark
        if mark>=40:
            passing_marks_count +=1

    average_marks= sum/len(marks)
    return (sum,highest,passing_marks_count,average_marks)

#Main program:
(sum,highest,passing_marks_count,average_marks)=analyze_marks(12,3,40,42)
print("Sum of marks entered:", sum)
print("Highest marks:", highest)
print("Number of passing marks:", passing_marks_count)
print("Average marks:", average_marks)

