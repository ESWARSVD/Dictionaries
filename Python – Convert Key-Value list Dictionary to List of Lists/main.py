#Python – Convert Key-Value list Dictionary to List of Lists

''''
input: {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
output:[['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]

'''



dict_ = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
 
 
result = []
for key, val in dict_.items():
    result.append([key] + val)
 
# printing result
print("The converted list is : " + str(result))