#Q=1
dict={1:'arpit',2:'ram',3:'mohit'}
list=[]
for i in dict.keys():
    list.append(i)
print(list)


#Q=2
dict = {'arpit': {'c':'10', 'c++': '20', 'ds': '30'},
          'ankit': {'c':'40', 'c++': '50', 'ds': '60'}}
print(dict['arpit']['c'],dict['arpit']['c++'],dict['arpit']['ds'])
print(dict['ankit']['c'],dict['ankit']['c++'],dict['ankit']['ds'])
