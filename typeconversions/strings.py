name = input("Enter your name: ")
print("Hello, " + name + "!",sep=",")

#for integer input output
n = int(input("Enter an number: "))
print("You entered:",n,sep="")

#for float input output
f = float(input("Enter a value of Pi: "))
print("Value of Pi:",f,sep="")

#for multiple inputs in a single line
x,y,z, = input("Enter three numbers : ").split()
print(x,y,z,sep=",")
sum = int(x) + int(y) + int(z)
print(sum,sep="")

#for specifying separator in output
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Name:", name, "Age:", age, sep=" ")
print(f"Name {name}, Age {age}")

#vowels and consonants count
string = input("Enter a string: ")
vowels = 0
consonants = 0
for char in string:
    if char in 'aeiouAEIOU':
        vowels += 1
    else:
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

#reverse a string
s=input("Enter a sentence: ")
words=s.split()
words.reverse()

print( " ".join(words))

#sum of 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum of", num1, "and", num2, "is:", sum)

#area of a circle
radius = int(input("Enter the radius of the circle: "))
a = 3.14 * (radius ** 2)
print("Area of the circle is:", a)
print("Area of the circle is: {:.2f}".format(a))

#quadratic equation
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))  
c=int(input("Enter the value of c: "))

root1 = 0
root2 = 0

d = (b**2) - (4*a*c)
root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)

print(f"Roots: ({root1}, {root2})")

#swapping of 2 numbers by using 3rd variable
a = int(input("Give a: "))
b = int(input("Give b: "))
c = a
a = b
b = c

print(f"the value of a is: {a}\n the value of b is: {b}")

#swapping of 2 numbers without using 3rd variable
a = 5
b = 10

a, b = b, a

print("a =", a)
print("b =", b)
#another way to do swapping of 2 numbers without using 3rd variable
a = int(input("Give a: "))
b = int(input("Give b: "))
a = a + b
b = a - b
a = a - b
print(f"the value of a is: {a}\n the value of b is: {b}")

#converting temperature units
c = int(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
k = c + 273.15
print("Temperature in Fahrenheit: ",f,"°F")
print("Temperature in Kelvin: ",k,"K")

#COUNT the no of words in a sentence given using split() method
s = input("Enter a sentence: ")
words = s.split()
word_count = len(words)
print("Number of words in the sentence:", word_count)

#removes all the spaces from a string
n=(input("Enter a string: "))
print( n.replace(" ", ""))

#two stringgs are anagrams or not
a = input("Enter a: ")
b = input("Enter b: ")
if sorted(a) == sorted(b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#tuple of 6 fruits names
fruits = ("apple", "banana", "mango", "grapes", "kiwi", "orange")
#accessing elements of the tuple
print(fruits[2])
print(fruits[-1])
print(fruits[1:5])


#max,min, sum of a elements in a tuple
a = (23,45,12,67,89,34)
print("Max:", max(a))
print("Min:", min(a))
print("Sum:", sum(a))

#print the names and marks of students using zip() function
names = ("Amit", "Sara", "John")
marks = (78, 92, 85)

for name, mark in zip(names, marks):
    print(name,"-", mark)

#count how many times elements repeated in a tuple
a =(2,4,6,4,8,4,10)
b = 4
count = a.count(b)
print(b , "appears", count, "times .")

#combine 2 tuples into a single tuple and convert it into a list
t1=(1, 2, 3)
t2=(4, 5, 6)
combined = t1 + t2
print(list(combined))

#take only the even numbers from the tuple and create a new tuple.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = tuple(num for num in a if num % 2 == 0)
print(even_numbers)

#print the large of a,b,c using conditional statements
a =15
b =47
c= 27
largest = a if a > b and a > c else b if b > c else c
print("The largest number is:", largest)