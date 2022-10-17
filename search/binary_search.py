def getEntries():
    global entry
    global entry_numberToSearch
    entry = ''
    entry_numberToSearch = 0
    entry = list(map(int, input("Type your entry: ").split(',')))
    entry_numberToSearch = int(input("Number to search: "))
    print("Your entry is", entry)
def binary_search():
    global m
    global steps
    steps = 0
    l = 0
    r = entry.index(entry[-1])
    m = int((l+r)/2)
    while m != entry_numberToSearch:
        steps += 1
        if entry[l] > entry[r]:
            print("List not sorted")
            exit()
        elif m < entry_numberToSearch:
            l = m + 1
            m = int((l+r)/2)
        elif m > entry_numberToSearch:
            r = m - 1
            m = int((l+r)/2)
    print("Index:", entry.index(m), "\nSteps taken:", steps)
getEntries()
binary_search()