# Indicate the type of expression. Choose between: int, float, bool, NoneType, String, List, Function_Or_Method

#>>> 2+3
type(2+3) # open idle and type it there to get the results for each of the listed things
#>>> 6/2
type(6/2)

# Indicate the result of the following operations (there will be 5 or 6 of these in the exam)
# Assume that the operations are executed in order. What will each print display
a=2
b=3
c="abc"
print(a,b,c)
print(a,b,c,sep=",")
a+=2
a==5
print(a)
print(c*(a-b))
d=c.find("b")
print(d)
print(d and b)
print(d==True)
e = str(a) + str(b) + str(c) + str(d)
print(e)
print(e[1::2])
print(e+e[::-1])

Write a function that takes the name of a text file as parameter. Print out the 3 letter words that start with "b"
