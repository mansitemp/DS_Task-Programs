#Program for ATM Withdrawal Analysis
#Initialize variables
successful_transactions = 0
rejected_transactions = 0

#Iterate through ten withdrawal attempts
for i in range(1, 11):

    #Capture the amount requested for the current transaction
    amount = int(input("Enter withdrawal amount: ₹"))

    #Reject transactions with zero or negative values
    if amount <= 0:
        print("Transaction Rejected: Invalid amount.")
        rejected_transactions += 1

    #Ensure the requested amount follows the denomination rule
    elif amount % 500 != 0:
        print("Transaction Rejected: Amount must be a multiple of ₹500.")
        rejected_transactions += 1

    #Verify that the requested amount is within the permitted limit
    elif amount > 20000:
        print("Transaction Rejected: Maximum withdrawal limit is ₹20,000.")
        rejected_transactions += 1

    else:
        print("Transaction Successful.")
        successful_transactions += 1

#Present the totals after all withdrawal attempts are completed
print("Successful transactions:", successful_transactions)
print("Rejected transactions:", rejected_transactions)