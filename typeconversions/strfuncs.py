#lower()
#upper()
#title
#capitalize()
#find()
#index()
#isaplha()
#isdigit()
#isalnum()

m = "Mala bhook lagali aahe"
n=m.lower()
print(n)

p= m.upper()
print(p)

a=m.title()
print(a)

r=m.capitalize()
print(r)

R = "bonjour"
print(R.find('o'))
print(R.find('o',2))#here we changed the starting point

print(R.index('u'))
print(R.index('u',3))

print(R.isalpha())
print(R.isdigit())

f="welcome123"
print(f.isalnum())


#strings 2 more functions are chr() and ord() which will work on ASCII value
y=chr(65)
print(type(y),y)

a=87
print(chr(a))


t=ord('A')
print(type(t),t)


#FORMATTING STRINGS
#named indexed
txt1 = "Welcome to {fname} {lname}".format(fname="funny", lname="honey")
print(txt1)

#numbered indexes
txt2 = "Welcome to {0} {1}".format("funny","honey")
print(txt2)

#empty placeholders
txt3 = "Welcome to {} {}".format("funny","honey")
print(txt3)


txt4 = "Welcome to {a:10} {b}".format(a=30,b=18)
print(txt4)#Welcome to         30 18 o/p
txt4 = "Welcome to {a:^10} {b}".format(a=30,b=18)
print(txt4)#Welcome to     30     18

