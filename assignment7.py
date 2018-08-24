#Q=1
dicttt={}
n=int(input("Enter number of items:"))
for x in range(n):
    key=input("Enter key ")
    value=input("Enter value ")
    dicttt[key]=value
print(dicttt)
val=input("Enter value to find")
for y,z in dicttt.items():
    if(z==val):
        print("Key of value",val,"is",y)


#Q=2
dict = {'arpit': {'c':'10', 'c++': '20', 'ds': '30'},
          'ankit': {'c':'40', 'c++': '50', 'ds': '60'}}
print(dict['arpit']['c'],dict['arpit']['c++'],dict['arpit']['ds'])
print(dict['ankit']['c'],dict['ankit']['c++'],dict['ankit']['ds'])
