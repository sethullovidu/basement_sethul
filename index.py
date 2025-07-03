# test1
i=7
print(i)
print(int(i)*4)

# getting user inputs
usern=input("enter your name :")
userge=int(input("enter your age :"))
usergpa=float(input("enter your GPA :"))
userexp=int(input("enter your  Experiance :"))

# conditions
if usergpa>=2 and userexp>=2:
    print("you can apply ")
else:
    print("rejected")

    #create fuctions
def sum (num1,num2):
    print(num1+num2)
def subs (num1,num2):
    print(num1-num2)
def mul (num1,num2):
    print(num1*num2)
def devi (num1,num2):
    print(num1/num2)

print("""
    calculator
    enter two numbers then enter logic operation 
    1. addition
    2. substraction 
    3. multiplication
    4. devision
                """)
    # userinputs
num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
    # display options

    # useroption
userop=int(input("enter your option :"))
    # conditions
if userop==1:
    # call fuction
    sum(num1,num2)
elif userop==2:
     # call fuction
    subs(num1,num2)
elif userop==3:
     # call fuction
    mul(num1,num2)
elif userop==4:
     # call fuction
    devi(num1,num2)

# displaying square
n=5
for i in range(n):
    print("*"*10)

# displaying r traingle
for i in range(1,n+1):
    print(i*"*")
print("-"*20)
# displaying d traingle
for i in range(n,0,-1):
    print(i*"*")
# displaying diamonad
# fist half
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
# second half
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# importing numpy
import numpy as np
# creating array
nrr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# displaying created array
print(nrr)
# shape of array
print(nrr.shape)
# size of array
print(nrr.size)
# displaying all elements by row-wise
for c in range(len(nrr)):
  print(nrr[c])
# row-major order traversal
for c in range(len(nrr)):
  for l in range(len(nrr[c])):
    print(nrr[c][l])

#  Replace all elements greater than 6 with 0
import numpy as np
nrr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
for c in range(len(nrr)):
  for l in range(len(nrr[c])):
    # print(nrr[c][l])
    sub=nrr[c][l]
    if sub > 6 :
      sub=0
      print(sub)
    else :
      print(sub)
# method ii
nrr[nrr > 6] = 0
print(nrr)

# creating random 2*3 array between 0 and 10 
import numpy as np
arr = np.random.randint(0, 10, (2, 3))
print(arr)

import numpy as np
# Create a 2*3 array with random numbers between 0 and 1
array = np.random.rand(2, 3)

print(array)


# create empty list
nlist=[] 
# getting user inputs
luser=input("enter your name :")
# inserting username to list
nlist.append(luser)
print(nlist)

# creating list
nlist = []
# creating infinity loop
while True:
    # getting user inputs
    luser = input("Enter your name (or -999 to stop): ")
    # user request to stop enter -999
    if luser == "-999":
        break
    # inserting user inputs to lsit
    nlist.append(luser)
# displying list after loop breaks
print("Names entered:", nlist)
print("")



