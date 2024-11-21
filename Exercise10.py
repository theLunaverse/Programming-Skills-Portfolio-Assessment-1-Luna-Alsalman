#Luna Alsalman 588512
#exercise 10

def even_odd(num):  #defining a function that checks if a number is even or odd
    if num % 2 == 0:  #checking if the number is divisible by 2
        return f"{num} is an even number."  #returning a string indicating the number is even
    else:
        return f"{num} is an odd number."  #returning a string indicating the number is odd

def main():  #defining the main function
    i = int(input("Enter a number please: "))  #prompting the user for a number and converting it to an integer
    result = even_odd(i)  #calling the even_odd function and storing the result
    print(result)  #printing the result from the even_odd function

if __name__ == "__main__":  #checking if the script is being run directly
    main()  #calling the main function