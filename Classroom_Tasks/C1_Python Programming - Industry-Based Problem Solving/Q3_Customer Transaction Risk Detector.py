#Program for Customer Transaction Risk Detector
#Intialize variables as risk counters
low_risk=0
medium_risk=0
high_risk=0

#Read and evaluate transaction amounts
for t in range(1,11):
    amount=float(input("Enter transaction amount: ₹"))

    #Validate and classify each transaction according to the risk limits
    if amount<0:
        print("Error! Amount can't be negative")
    elif amount>50000:
        print("High risk")
        high_risk +=1
    elif amount<=50000 and amount>=20000:
        print("Medium risk")
        medium_risk +=1
    elif amount<20000:
        print("Low risk")
        low_risk +=1
    else:
        print("Invalid input")

#Display results for all valid transactions
    print("Number of low risk transactions: ", low_risk)
    print("Number of medium risk transactions: ", medium_risk)
    print("Number of high risk transactions: ", high_risk)
