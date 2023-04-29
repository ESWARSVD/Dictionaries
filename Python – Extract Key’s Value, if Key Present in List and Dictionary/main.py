#Python – Extract Key’s Value, if Key present in List and Dictionary

'''
Input : givenlist = ["Gfg", "is", "Good", "for", "Geeks"], given_dict = {"Gfg" : 5, "Best" : 6}, K = "Gfg" 
Output : 5 
Explanation : "Gfg" is present in list and has value 5 in dictionary. 

Input : givenlist = ["Good", "for", "Geeks"], given_dict = {"Gfg" : 5, "Best" : 6}, K = "Gfg" 
Output : None 
Explanation : "Gfg" not present in List.
'''


givenlist = ["Gfg", "is", "Good", "for", "Geeks"]
 

given_dict = {"Gfg" : 2, "is" : 4, "Best" : 6}
 

K = "Gfg"
 


result = None
if all(K in sub for sub in [given_dict, givenlist]):
    result = given_dict[K]
 

print("Extracted Value : " + str(result))