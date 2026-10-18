#Program for Fraudulent Transaction Detector
#Initialize counters for suspicious transactions and their total value 
suspicious_transactions=0
total_value=0

#Process exactly 8 transactions
for i in range(1,9):
    transaction=float(input("Enter transaction amount: "))

    #Transaction exceeding 1,00,000 is considered suspicious
    if transaction>100000:
        print("Suspicious transaction detected!")
        suspicious_transactions +=1
        total_value += transaction

#Display final results
print("Number of suspicious transactions: ", suspicious_transactions)
print("Sum of suspicious transactions: ",total_value)