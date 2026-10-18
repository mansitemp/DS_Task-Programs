#Program for Login Security System
#Define correct password and attempt limit
correct_password=9009
max_attempts=3

#Limit login attempt and accept password
for attempts in range(1,4):
    password= int(input("Enter password: "))

    #Verify the entered password
    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect password")

        #Lock the account after maximum failed attempts
        if attempts == max_attempts:
            print("Account Locked")