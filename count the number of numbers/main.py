#count the number of numbers
'''
input=[2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,8]
output={1:1,2:2,3:2,4:2,5:2,6:2,7:2,8:3,9:1}
'''

list_=input("Enter a list of numbers:").split(",")
list_.sort()
dict_={}
for num in list_:
    if num in dict_:
        dict_[num]=dict_[num]+1
    else:
        dict_[num]=1

print(dict_)