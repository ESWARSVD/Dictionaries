#Python – Reverse Dictionary Keys Order
'''
test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
OrderedDict([('gfg', 4), ('best', 5), ('is', 2)])

'''

test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
 

print("The original dictionary : " + str(test_dict))

res = dict(reversed(list(test_dict.items())))
 

print("The reversed order dictionary : " + str(res))