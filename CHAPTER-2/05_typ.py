#Type() Function
a = 31 #For interger
t = type(a) # Class <int>
print(t)
#For float num
a = 31.2
t = type(a) #class <int>
print(t)
#For String
a = "Mngl"
t = type(a) #Class <int>
print(t)
a = "31.2"# This is a string bcz the num is under the double qouet ""
t = type(a) #class <int>
print(t)

#Guys this is very interesting for the both string and float num we can convert the string into float num by using float() function
a = "31.2"
b = float(a) # a but the type should be float
t = type(a)
print(t)