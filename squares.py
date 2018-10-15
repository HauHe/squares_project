<<<<<<< Updated upstream

def list_squares(n):
    "returns a lists of squares"
    li = []
    for i in range(1, n+1):
        li.append(i**2)
    return li

for i in list_squares(4):
=======
def list_powers(n, m):
    "returns a lists of squares"
    li = []
    for i in range(1, n+1):
        li.append(i**m)
    return li

for i in list_powers(4, 3):
>>>>>>> Stashed changes
    print(i)





