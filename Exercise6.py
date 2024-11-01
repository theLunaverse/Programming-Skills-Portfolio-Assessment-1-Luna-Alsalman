#Luna Alsalman 588512
#exercise 6

correct = "12345"  #defining the correct password as a variable called 'correct'
max_attempts = 5  #setting the maximum number of allowed attempts
attempts = 0  #initializing the attempt counter to zero

#starting a loop that continues until the number of attempts reaches the maximum
while attempts < max_attempts:
    password = input("Enter the password: ")  #prompting the user to enter the password
    
    if password == correct:  #checking if the entered password matches the correct password
        print("Access granted.")  #printing a message if the password is correct
        break  #exiting the loop if access is granted
    else:
        attempts += 1  #increase the attempt count by 1
        remaining = max_attempts - attempts  #calculating the remaining attempts
        if remaining > 0:  #checking if there are attempts left
            #printing the number of remaining attempts using an f-string for formatted output
            print(f"Incorrect password. You have {remaining} attempts left.")

        else:
            #printing a message when the maximum attempts are reached
            print("Maximum attempts reached. You will be reported to Authorities.")