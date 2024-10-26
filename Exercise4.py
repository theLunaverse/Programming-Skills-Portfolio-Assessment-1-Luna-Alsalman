#Luna Alsalman 588512
#exercise 4

import random  #importing the random module for shuffling

#defining a dictionary of countries and their capitals
questions = {"Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid",
"Netherlands": "Amsterdam", "Belgium": "Brussels", "Portugal": "Lisbon",
"Switzerland": "Bern", "Austria": "Vienna", "Greece": "Athens"}

#asking for the capital of France 
answer = input("What is the capital of France? ").strip().lower() #removing spaces, and converting the input to lowercase

#checking if the answer is "paris"
if answer == "paris":
    print("Correct!")  #if the answer is correct, print "Correct!"
else:
    print("Wrong! The correct answer is Paris.")  #otherwise, print the correct answer

#converting the dictionary into a list of country-capital pairs
countries = list(questions.items())  
random.shuffle(countries)  #shuffling the list for random question order

#looping through the shuffled list of countries and capitals
for country, capital in countries:
    #asking for the capital of the current country, removing spaces, and converting to lowercase
    answer = input("What is the capital of " + country + "? ").strip().lower()
    
    #checking if the answer matches the correct capital
    if answer == capital.lower():
        print("Correct!")  #if correct, print "Correct!"
    else:
        print("Wrong! The correct answer is " + capital)  #if wrong, print the correct capital
