def getEntries():
    global entry
    global entry_numberToSearch
    entry = ''
    entry_numberToSearch = 0
    entry = list(map(int, input("Type your entry: ").split(',')))
    entry_numberToSearch = int(input("Number to search: "))
    print("Your entry is", entry)


def check_list():
    i = 0
    secondLast_index = len(entry)-2
    while i <= secondLast_index:
        if entry[i] > entry[i + 1]:
            print("List not sorted")
            exit()
        else:
            i += 1


def binary_search():
    global m
    global attempts
    attempts = 0
    l = 0
    r = len(entry)-1
    m = int((l+r)/2)
    while entry[m] != entry_numberToSearch:
        attempts += 1
        if entry[m] < entry_numberToSearch:
            l = m + 1
            m = int((l+r)/2)
        elif entry[m] > entry_numberToSearch:
            r = m - 1
            m = int((l+r)/2)
    print("Index:", m, "\nAttempts made:", attempts)


getEntries()
check_list()
binary_search()
