from os import error


list_data = [1,'string',3.1,[5,6,7],[8,9,10]]
index = list_data.index('string')
a=0
for x in range(4):
    print(list_data[a]) ##error
    a=a+1