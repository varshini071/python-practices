#Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
#important revise again

vol = input("enter the string: ")
n=int(input("enter the value n: "))
if len(vol) < 2:
    print(vol * n)
else:
    print(vol[:2]*n)
   