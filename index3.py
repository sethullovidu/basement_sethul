nlist=[]
while True :
    fname=input(" enter your first name :")
    if fname == "-999":
        print(nlist)
        break
    lname=input("enter your last name :")
    age=int(input("enter your age :"))
    gpa=float(input("enter your GPA :"))
    person={
        'Name':fname,
        'Last Name':lname,
        'Age':age,
        'GPA':gpa
    }
    nlist.append(person)