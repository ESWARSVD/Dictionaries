#Python  Remove all duplicates words from a given sentence

'''
Input : Geeks for Geeks
Output : Geeks for

Input : Python is great and Java is also great
Output : is also Java Python and great

'''


sentence=input("Enter a sentence:").split()

dict_={}

for string in sentence:
    if string in dict_:
        dict_[string]=dict_[string]+1
    else:
        dict_[string]=1

uniqe_list=[]

for str in dict_:
    uniqe_list.append(str)

print(*uniqe_list)













