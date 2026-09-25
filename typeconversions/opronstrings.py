w = "bonjour zib zub zap"
'''w=w[-1::-1]#this is slicing the string from index -1 to the end of the string with a step value of -1   
print(w[6])#this is indexing the string to get the character at index 6
print(w[-4:-1])#this is slicing the string from index -4 to -1
print(w[::2])#here we only alloted step value of 2 so it will print every second character in the string
print(w[-1::-2])#this is slicing the string from index -1 to the end of the string
print(w[-1::-1])#this is slicing the string from index -1 to the end of the string with a step value of -1
'''
t=len(w)
print(t)
#for a in range(t):
    #print(w[a])#this is indexing the string to get the character at index a
    
t=len(w)
print(" ") #this is another type of reversing a string using for loop

for a in range(t-1,-1,-1):
    print(w[a])#this is indexing the string to get the character at index a