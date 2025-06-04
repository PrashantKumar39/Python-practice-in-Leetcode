myDict =  {'name' : "Prashant", "Addres" : "Chennai", "Mobile No" : 6266}
# print(myDict)


def traverseDict(dict):
    for key in dict: # ------------------------------>    O(N)
        print(key, dict[key]) # --------------------->    O(1)
traverseDict(myDict)

# The Time Complecity is O(N)
# The Space Complecity is O(1)
        