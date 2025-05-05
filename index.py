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