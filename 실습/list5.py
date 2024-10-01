numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lists = [] 
for n in range(3):
    lists.append(list())
for i in numbers:
    lists[(i % 3) -1].append(i)
    # lists[ (i + 2) % 3].append(i)
        
print(lists)