#K’th Non-repeating Character in Python using List Comprehension and OrderedDict

'''
Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o

Input : str = geeksforgeeks, k = 4
Output : Less than k non-repeating
         characters in input.

'''


string=input("Enter a string:")
k=int(input("Enter a value:"))

dict_={}

for i in string:
    if i in dict_:
        dict_[i]=dict_[i]+1
    else:
        dict_[i]=1
result=[]
for i in (dict_):
    if dict_[i]>1:
        continue 
    else:
        result.append(i)
if len(result)<k:
    print("Less than k non-repeating characters in input.")
else:
    print(result[k-1])

