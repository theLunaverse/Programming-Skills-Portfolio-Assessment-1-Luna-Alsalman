#Luna Alsalamn 588512
#exercise 5

#creating a dictionary that maps month numbers to the number of days in that month
Monthdict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 
9: 30, 10: 31, 11: 30, 12: 31}

#starting an infinite loop to repeatedly ask for valid month input
while True:
    #asking the user to enter a month number (as a string)
    Month = input("Enter the month number (1-12): ")

    #checking if the input is a digit and if it's within the valid month range (1-12)
    if Month.isdigit() and 1 <= int(Month) <= 12:
        Month = int(Month)  #converting the input to an integer
        break  #breaking the loop if a valid month is entered
    else:
        # If input is invalid, asking the user to enter a valid month number
        print("Invalid input. Please enter a valid month number between 1 and 12.")

#checking if the entered month is February (month number 2)
if Month == 2:
    #starting another loop to ask if it's a leap year
    while True:
        #asking the user if it is a leap year and using `.strip()` to remove spaces
        #and `.lower()` to ensure the input is in lowercase
        leap_year = input("Is it a leap year? (yes/no): ").strip().lower()

        #checking if the input is either "yes" or "no"
        if leap_year in ["yes", "no"]:
            break  #breaking the loop if a valid answer is given
        else:
            #if input is invalid, asking the user to enter "yes" or "no"
            print("Invalid input. Please enter 'yes' or 'no'.")

    #using a ternary operator to set `feb_days` to 29 if leap year is "yes", otherwise 28
    feb_days = 29 if leap_year == "yes" else 28

    #using formatted strings to print the number of days in February
    print(f"The number of days in February is {feb_days}")
else:
    #for other months, using formatted strings to print the number of days
    print(f"The number of days in month {Month} is {Monthdict[Month]}")