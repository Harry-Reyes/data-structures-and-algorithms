def getEntries():
    global entry
    global entry_numberToSearch
    entry = ''
    entry_numberToSearch = 0
    entry = list(map(int, input("Type your entry: ").split(',')))
    entry_numberToSearch = int(input("Number to search: "))
    print("Your entry is", entry, "\n")

def searchFrom_left():
    global isFound
    global attemptsFrom_left
    global entry_index
    isFound = False
    attemptsFrom_left = 0
    for entry_index in range(len(entry)):
        attemptsFrom_left += 1
        if entry_numberToSearch == entry[entry_index]:
            isFound = True
            break

def searchFrom_right():
    global attemptsFrom_right
    attemptsFrom_right = 0
    for i in range(len(entry)-1, 0, -1):
        attemptsFrom_right += 1
        if entry_numberToSearch == entry[i]:
            break

def use_isFound():
    if isFound == False:
        print("Not found")
        exit()
    else:
        searchFrom_right()
        print("Index:", entry_index, "\nAttempts made:\nFrom left =",
              attemptsFrom_left, "\nFrom right =", attemptsFrom_right)

getEntries()
searchFrom_left()
use_isFound()