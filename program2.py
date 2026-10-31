# Python Project for the Checking of the Palindrome
#example is the RACECAR:

string = input("Enter a string to check whether the give string is Palindrome : ")

if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")