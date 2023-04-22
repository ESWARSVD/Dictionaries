#Python – Swapping Hierarchy in Nested Dictionaries
'''
Input : test_dict = {‘Gfg’: { ‘a’ : [1, 3, 7, 8], ‘b’ : [4, 9], ‘c’ : [0, 7]}} 
Output : {‘c’: {‘Gfg’: [0, 7]}, ‘b’: {‘Gfg’: [4, 9]}, ‘a’: {‘Gfg’: [1, 3, 7, 8]}}
Input : test_dict = {‘Gfg’: {‘best’ : [1, 3, 4]}} 
Output : {‘best’: {‘Gfg’: [1, 3, 4]}} 
 '''

dict_= {"Gfg": { "a" : [1, 3, 7, 8], "b": [4, 9], "c" : [0, 7]}} 
result=dict()


for key,value in dict_.items():
    for key_,val_ in value.items():
        if key_ not in result:
            temp = dict()
        else:
            temp = result[key_]
        temp[key] = val_
        result[key_] = temp
print(result)