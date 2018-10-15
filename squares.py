
def list_squares(n):
    "returns a lists of squares"
    li = []
    for i in range(1, n+1):
        li.append(i**2)
    return li

for i in list_squares(4):
    print(i)





