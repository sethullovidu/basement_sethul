
nlist=[]
while True: 
    fname=input("enter your first name :")
    lname=input("enter your last name :")
    age=int(input("enter your age :"))
    person={
        'Name':fname+" "+lname,
        'Age':age
        }
    nlist.append(person)
    print(nlist)

