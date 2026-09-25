#Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

string = input("enter the string: ")
print(string.startswith("Is"))
if string.startswith("Is"):
    print("string")
else:
    print("Is",string)