#Find all duplicate characters in string
'''
Input : hello
Output : l

Input : geeksforgeeeks
Output : e g k s

'''

string=input("Enter a string:")
dict_={}

for str in string:
    if str in dict_:
        dict_[str]=dict_[str]+1
    else:
        dict_[str]=1

dup_=[]
for str in dict_:
    if dict_[str]>1:
        dup_.append(str)
    else:
        continue

print("duplicate words in the string: ")
print(*dup_)
