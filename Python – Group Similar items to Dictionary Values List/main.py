#Python – Group Similar items to Dictionary Values List

'''
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]} 
Explanation : Similar items grouped together on occurrences. 

Input : test_list = [7, 7, 7, 7] 
Output : {7 : [7, 7, 7, 7]} 
Explanation : Similar items grouped together on occurrences.
'''

arr=input("Enter a list of numbers:").split()

dict_={}

for num in range(len(arr)):
    key=arr[num]
    if num in dict_:
        continue
    else:
        val=[]
        for num1 in arr:
            if num1==key:
                val.append(num1)
        dict_[key]=val

print(dict_)