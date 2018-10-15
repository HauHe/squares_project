
# coding: utf-8

hello = "Hello world"


# In[1]:
#li = [1, 2, 3, 4]

def list_squares(n):
    "returns a lists of squares"
    li = []
    for i in range(n):
        #print(i**2, end='')
        li.append(i**2)
    #print()
    return li

for i in list_squares(15):
    print(i, end=' ')





