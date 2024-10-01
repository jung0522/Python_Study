'''
for i in range(1, 9):
    if i < 8:
        print(f"{i} * n", end ="\t")
    else:
        print(f"{i} * n")
        
for n in range(1, 11):
    for i in range(1, 9):
        if i < 8:
            print(i*n, end ="\t")
        else:
            print(i*n)
'''
for n in range(2, 11):
    for i in range(1, 9):
        if i < 9:
            print("%2d * %2d = %2d" % (n, i, n*i), end = " ")
    print()
