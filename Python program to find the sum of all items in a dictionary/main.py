#Python program to find the sum of all items in a dictionary

'''
Input : {a: 100, b:200, c:300}
Output : 600

Input : {x: 25, y:18, z:45}
Output : 88
'''

mydict={"a": 100, "b":200, "c":300}

total_sum=0

for dic in mydict:

    total_sum=total_sum+mydict[dic]

print("toatal sum:",total_sum)