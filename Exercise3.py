#Luna Alsalman 588512
#exercise 3

info = {  #creates a dictionary to store user information
    'fullname': input("What is your full name? : "),  #gets full name from the user and store it in the 'fullname' key
    'hometown': input("Where are you from? : ")  #gets hometown from the user and store it in the 'hometown' key
}

age = input("How old are you? : ")  #asks the user for their age
while not age.isdigit():  #checks if the input is not a number
    age = input("Please enter numbers only. How old are you? : ")  #if not a number, the while asks for input again
info['age'] = int(age)  #converts the valid age input to an integer and store it in the 'age' key

print(f"\nName: {info['fullname']}\nHometown: {info['hometown']}\nAge: {info['age']}")  
#prints the user's information using an f-string with embedded variables for formatted output.

