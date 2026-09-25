#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

n = int(input("enter n value: "))

if n > 17:
    result = 2 * abs(n - 17)
else:
   result =abs(n-17)

print(result)