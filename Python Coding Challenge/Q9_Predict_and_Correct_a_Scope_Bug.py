#Corrected code:
score = 50

def update():
    global score
    print(score)
    score = score + 10

update()
print(score)

#Answer the Following Questions:
#1. Why does the original code raise an error?
#The original code raises an rrror because Python considers 'score' as a local variable due to the assignment inside the function, making it unavailable to print before it is defined.
#2. What is the correct use of the "global" keyword here?
#The correct use of the global keyword tells Python to refer the variable from the outer global scope instead of creating a new local one.
#3. What will the output be after correcting the code?
#The final output after correcting the code will be:
# 50
# 60
