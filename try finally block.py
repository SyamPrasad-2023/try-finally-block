#Try finally block
try:
    print("rasing exception...")
    raise ValueError
except:
    print("exception caught...")
finally:
    print("performing clean-up with finally...")
    
# program having finally block to re-rise an exception that will be an outer try except block
try:
    print("dividing two strings...")
    try:
        quo="abc"/"def"
        print(quo)
    finally:
        print("this is the finally block...")
except TypeError:
    print("here type error is handled,which is raised in inner try")

try:
    f= open("file1.txt")
    x=f.readline()
    print(x)
except:
    print("file does not exit")
    raise
    
# assertion
a=int(input("enter the temp in c"))
f = (a*9/5)+32
assert (f<=32),"its freezing"
print("temperature in fahrenheit= ", f)

#write a program that prompts the user to enter a num and print its square
num= int(input("enter a number:"))
try:
    output=num *num
    print(output)
except KeyboardInterrupt:
    print("program has been intrupted")

i=0
n=0
while True:
    try:
        n= n+1
        if n==51:
            raise StopIteration
    except StopIteration: 
        break
    else:
        print(n, end=" ")

try:
    size=int(input("enter size:"))
    user_list=[]
    for i in range(size):
        val=int(input(f"enter the element{i+1}:"))
        user_list.append(val)
    index=int(input("enter index access elements:"))
    print("Element at index", index,  "is", user_list[index])
except ValueError:
    print("Eroor : please enter only integers")
except IndexError:
    print("Error : index.....out of range...")

'''syntax:
    [expression for var in range() if condition]'''
# 1 4 9 16....1000
print([num**2 for num in range(1,11)])
print([x for x in range(1,11)if x%2==0])

words=['apple','bananna','cherry']
print([word.upper() for word in words])
        
    