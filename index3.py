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


# converting Javascript object notations to python
import json
# creating javascript obeject notation
tet='''{
  "name": "John",
  "age": 30,
  "isStudent":true,
  "from":"Mathara"
}'''
# Converting JSON to Python:
ctet= json.loads(tet)
# display output
print(ctet)



# converting python dictionary to JSON
# creating python dictionary
person={
    'Name': "sethul",
    'Age':17,
    'IsStudent':True,
    'from':"mathara"
}
# Converting dictionary to javascript object notation
cperson=json.dumps(person)
# display output
print(cperson)

# # Removing duplicates from  List
# creating list
mylist = ["a", "b", "a", "c", "c"]
#  removing duplicates
mylist = list( dict.fromkeys(mylist) )
# displaying none duplicates list
print(mylist)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# reversing a string
txt = "Hello World"[::-1]
print(txt)