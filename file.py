
import csv
dict1={}

with open('1.txt') as code:
    read=csv.reader(code,delimiter=':')
    for v in read:
        if(v[0]=="#"):
            continue
        else:
            dict1[v[0]]=int(v[3])

#print dict1

for v,x in dict1.items():
    print v, '=' ,x
    
    
