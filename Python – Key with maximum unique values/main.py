#Python – Key with maximum unique values
'''
Input : test_dict = {“Gfg” : [5, 7, 9, 4, 0], “is” : [6, 7, 4, 3, 3], “Best” : [9, 9, 6, 5, 5]} 
Output : “Gfg” 
Explanation : “Gfg” having max unique elements i.e 5. 

Input : test_dict = {“Gfg” : [5, 7, 7, 7, 7], “is” : [6, 7, 7, 7], “Best” : [9, 9, 6, 5, 5]} 
Output : “Best” 
Explanation : 3 (max) unique elements, 9, 6, 5 of “Best”.
'''


dict_ = {'Gfg' : [5, 7, 9, 4, 0], 'is' : [6, 7, 4, 3], 'Best' : [9, 9, 6, 5, 5]} 
 

print("The original dictionary is : " + str(dict_))
 

max_key = []
for sub in dict_:
    if len(set(dict_[sub])) == len(dict_[sub]):
        max_key.append(sub)
    
 
# printing result
print("Key with maximum unique values : " )
print(*max_key)