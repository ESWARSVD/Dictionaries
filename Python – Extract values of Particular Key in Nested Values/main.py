#Python – Extract values of Particular Key in Nested Values

''''
Input : test_dict = {'Gfg' : {“a” : 7, “b” : 9, “c” : 12}, 'is' : {“a” : 15, “b” : 19, “c” : 20}, 'best' :{“a” : 5, “b” : 10, “c” : 2}}, key_ = “b” 
Output : [9, 10, 19] 
Explanation : All values of “b” key are extracted. 

Input : test_dict = {'Gfg' : {“a” : 7, “b” : 9, “c” : 12}, 'is' : {“a” : 15, “b” : 19, “c” : 20}, 'best' :{“a” : 5, “b” : 10, “c” : 2}}, key_ = “a” 
Output : [7, 15, 5] 
Eplanation : All values of “a” key are extracted.


'''

test_dict = {'Gfg': {'a': 7, 'b': 9, 'c': 12},'is': {'a': 15, 'b': 19, 'c': 20},'best': {'a': 5, 'b': 10, 'c': 2}}

key_ = "c"
 

reesult = []
 
for value in test_dict.values():
     
    if key_ in value:
         
        reesult.append(value[key_])
 
# printing reesult
print("The extracted values : " + str(reesult))