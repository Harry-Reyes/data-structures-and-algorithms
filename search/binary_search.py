def getEntries():
    global entry
    global entry_numberToSearch
    entry = ''
    entry_numberToSearch = 0
    entry = list(map(int, input("Type your entry: ").split(',')))
    entry_numberToSearch = int(input("Number to search: "))
    print("Your entry is", entry, "\n")

def check_list():
    for i in range(len(entry)-1):
        if entry[i] > entry[i + 1]:
            raise Exception("List not sorted")

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