#grouping of scores
'''
input: r:1,b:2,r:3
output: [('b',2),()'r',4)]
'''

mydict_ict=input("Enter a dict list:").split(",")
dict_={}
for i in mydict_ict:
    pair=i.split(":")
    n,v=pair[0],int(pair[1])
    if n in dict_:
        dict_[n]=dict_[n]+v
    else:
        dict_[n]=v
result=list(sorted(dict_.items()))
print(result)