#Program for Prime Number Detector
print("Prime numbers between 1 and 50 are: ")

#Outer loop: Iterates through each number from 2 to 50
for dividend in range(2,51):

    #Inner loop: Checks if 'dividend' can be divided by any number smaller than itself
    for divisor in range(2,dividend):
        if (dividend % divisor) == 0:
            break #Stops checking if divisor is found
    else:
        print(dividend)