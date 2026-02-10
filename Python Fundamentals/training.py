#input and output
name=input("what is your name?") #return string
print(name)
num = int(input("Enter a number: "))
print(num, "is of type", type(num))
x,y=input("enter two numbers: ").split()
print(x,y)
li = input("Enter elements separated by space: ").split()
print("List:", li)    #list of strings
list=[]
num=int(input("Enter the number of the elements: "))
for i in range(num):
    element=input(f"Enter the element {i+1}: ")
    list.append(element)
print(list) #list of integers
n = int(input("Enter the number of elements: "))
a = [input(f"Enter element {i+1}: ") for i in range(n)]
print("List:", a)
print("Hello World") #print string
print(4)  #print numbers
print(3*3)
print("Dana",22)    #print strings+numbers
print("Dana",end=" ")
print("is here")#print at the same line
#//////////////////////////////////////////////////////////////////////
#comments
#this is a comment
"""
this is a
multiline
comments
"""
#////////////////////////////////////////////////////////////////////
#variables
age=22
_name='dana'
my_name='dana'

x=5
y="dana"
#is the same as
y='dana'
x="hi"#overwrite
print(x)
print(y)
print(type(x))
a=5
A='hello'
print(a)
print(A)
x = 10
del x   #delete variable
x=5
y=x
x=10
print(y)
a, b = 5, 10
a, b = b, a     #swaping
print(a, b)
word = "Python"
length = len(word)
print("Length of the word:", length)
#local variables
def greet():
    msg = "Hello!"
    print("Inside function:", msg)

greet()
#print("Outside function:", msg)  ->  (error)

#Global Variables
msg = "Python is awesome!"
def display():
    print("Inside function:", msg)
display()
print("Outside function:", msg)
#Use of Local and Global variables
def fun():
    s = "hello"
    print(s)
s = "hi"
fun()
print(s)

#Assign Function to a Variable
def a():
  print("hi")

var=a          # assigning function to a variable
var()
#Insert a Variable into a String
a = "Python"
res = f"This is {a} programming!"
print(res)

a = "Hello"
b = "world"

res = "{} {}".format(a, b)
print(res)

res = a + " " + b
print(res)

a = "Python"
res = "This is %s programming!" % a
print(res)
#///////////////////////////////////////////////////////////////////////
#casting
z=float(3)#casting
print(z)

a = 5.9
n = int(a)

print(n)
print(type(n))

a = 5
n = str(a)

print(n)
print(type(n))


b = 't'
# print(int(b))  ->ValueError
print(type(b))

a = 5
b = 't'
#n = a+b ->TypeError

#//////////////////////////////////////////////////////////////////////////
#Python Data Types
a = 5    #int
b = 5.0     #float
c = 2 + 4j       #complex
s = 'Welcome to the Geeks World'    #string
print(s)
print(s[1])             #the second letter
print(s[2])              #the third
print(s[-1])             #the last

a = [1, 2, 3]      #list
tup2 = ('hi', 'dana')      #tuple
data=True #bool
s2 = {"hi", "hello", "hi"}     #set
print(s2)
for i in s2:
   print(i, end=" ")
print("hi" in s2)          #return True/False

d = {'name': 'dana', 'age': '22'}        #dict
print(d['name'])
print(d.get('age'))
#////////////////////////////////////////////////////////////////////
#string
s = "Danaishere"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string

s = "hello everyone"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("everyone", "dana")  # replace word
print(s1)
print(s2)
print(len(s))
print(s.upper())
print(s.lower())

s = "   Gfg   "
print(s.strip())

s = "Python is fun"
print(s.replace("fun", "awesome"))

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello "
print(s * 3)  #Hello Hello Hello

s="danaarabasi"
print("dana" in s)

s1 = "Apple"
s2 = "apple"
print(s1.lower() == s2.lower())

s = "hello world"
print(s.startswith("hello"))
print(s.endswith("world"))
#////////////////////////////////////////////////////////////////////////////////
#list
aa = [1, 2, 3, 4, 5]
bb = ['apple', 'banana', 'cherry']
cc = [1, 'hello', 3.14, True]
print(aa[0])
print(aa[-1])
print(aa[1:4])   # elements from index 1 to 3

aa.append(10)
aa.insert(0, 5)
aa.extend([15, 20, 25])
aa.clear()

a = [10, 20, 30, 40, 50]

a.remove(30)
val = a.pop(1)
del a[0]

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[1][2])

squares = [x**2 for x in range(1,6)]
#///////////////////////////////////////////////////////////////////////
#tuple
tup=('dana',22)
tup1=tuple('dana')
print(tup1[0])
print(tup1[1:4])

a,b=tup

tup3=(2003,'asal')
tup4=tup+tup3
print(tup4)
del tup4
tup4=(1,2,3,4)
x,*y,z=tup4

#////////////////////////////////////////////////////////////////////////////
#Dictionary
data = { "name": "dana", "age": 22 }
print(data)
print(data["name"])
print(data.get("age"))

data[1] = "Python dict" #adding new dict
data["age"] = 23 #updata

del data["age"]
val = data.pop(1)
key, val = data.popitem()
d.clear()

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
#/////////////////////////////////////////////////////////////////////
#set
set1 = {1, 2, 3, 4}
# Add one item
set1.add(5)

# Add multiple items
set1.update([6, 7])

for i in set1:
    print(i, end=" ")

set1.remove(3) # if the item doesn't exist -->KeyError
set1.discard(4) #no error
val = set1.pop() # بتشيل عنصر عشوائي  (it the set is empty-->KeyError)
set1.clear()

fset = frozenset([1, 2, 3, 4, 5])
#//////////////////////////////////////////////////////////////////////
#arrays
import numpy as np
a = np.array([1, 2, 3, 4])
print(a * 2)
res = np.array([[1, 2], [3, 4]])
print(res * 2)

import array as arr
a = arr.array('i', [1, 2, 3]) #the same datatype
print(a[0])

a.append(5)
print(a)
a.insert(1, 4)  # Insert 4 at index 1
print(*a)

a.remove(1) #remove the value 1
print(a)
a.pop(2)   # remove item at index 2
print(a)

print(a.index(2))  # index of 1st occurrence of 2
print(a.index(1))  # index of 1st occurrence of 1

count = a.count(2) #كم رة عندي رقم 2

a.reverse() #بعكس ال array

a.extend([6,7,8,9,10]) #بضيف عال array مجموعة عناصر

#////////////////////////////////////////////////////////////////
#Operators
# Variables
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b) #integer
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

a = True
b = False
print(a and b)
print(a or b)
print(not a)

a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

a = 10
b = 20
c = a
print(a is not b)
print(a is c)

a, b = 10, 20
min = a if a < b else b #Ternary Operator

#//////////////////////////////////////////////////////////////////
#Conditional Statements
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

marks = 45
res = "Pass" if marks >= 40 else "Fail"

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

#//////////////////////////////////////////////////////////////
#loops
li = ["dana", 1, 2]
for x in li:
    print(x)
tup = ("dana", "arabasi", 2)
for x in tup:
    print(x)
s = "abc"
for x in s:
    print(x)
d = dict({'x': 123, 'y': 354})
for x in d:
    print("%s  %d" % (x, d[x]))
set1 = {10, 30, 20}
for x in set1:
    print(x)

cnt = 0
while cnt < 3:
    cnt = cnt + 1
    print("Hello")

for letter in 'danaarabasi':
    if letter == 'a' or letter == 's':
        continue
    print('Current Letter :', letter)

for letter in 'danaarabasi':
    if letter == 'a' or letter == 's':
        break

print('Current Letter :', letter)

for letter in 'danaarabasi':
    pass
print('Last Letter :', letter)

#//////////////////////////////////////////////////////////
#functions
def fun():
    print("Welcome")
fun()

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)

def student(fname, lname):
    print(fname, lname)
student(fname='Dana', lname='Arabasi')
student('Dana','Arabasi')


def f1():
    s = 'hi everyone'
    def f2():
        print(s)

    f2()
f1()

def cube(x): return x*x*x
cube_l = lambda x : x*x*x  #Anonymous Functions
print(cube(7))
print(cube_l(7))

def myFun1(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun1(lst)
print(lst)   # list is modified

def myFun2(x):
    x = 20
a = 10
myFun2(a)
print(a)     # integer is not modified


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) #Recursive Function

print(factorial(4))

#/////////////////////////////////////////////////////////
#oop
#Classes and Objects

class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)
print(dog1.name)
print(dog1.species)








