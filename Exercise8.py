#Luna Alsalman 588512
#exercise 8

people_list = ["jake", "zac", "ian", "ron", "sam", "dave"]  #creating a list of names

#prompting the user to enter a name, removing spaces and converting to lowercase
name = input("Enter a name you'd like to check: ").strip().lower()

#checking if the entered name (in lowercase) is in the people_list
if name in people_list:  
    #if found, print a message confirming the name is on the list, capitalizing the first letter
    print(f"{name.capitalize()} is on the list!")  
else:
    #if not found, print a message indicating the name couldn't be found, capitalizing the first letter
    print(f"{name.capitalize()} couldn't be found in the list.")
