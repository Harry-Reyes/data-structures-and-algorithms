def getEntries():
    global entry
    global entry_numberToSearch
    entry = ''
    entry_numberToSearch = 0
    entry = list(map(int, input("Type your entry: ").split(',')))
    entry_numberToSearch = int(input("Number to search: "))
    print("Your entry is", entry)
def searchFrom_left():
    global isFound
    global stepsFrom_left
    global entry_index
    entry_index = 0
    isFound = False
    stepsFrom_left = 0
    while entry_index <= len(entry)-1:
        stepsFrom_left += 1
        if entry_numberToSearch == entry[entry_index]:
            isFound = True
            break
        else:
            entry_index += 1
def searchFrom_right():
    global stepsFrom_right
    stepsFrom_right = 0
    i = 0
    entry_reversed = list(reversed(entry))
    while i <= len(entry_reversed)-1:
        stepsFrom_right += 1
        if entry_numberToSearch == entry_reversed[i]:
            break
        else:
            i += 1
def use_isFound():
    if isFound == False:
        print("Not found")
        exit()
    else:
        searchFrom_right()
        print("Index:", entry_index, "\nSteps taken:\nFrom left =", stepsFrom_left, "\nFrom right =", stepsFrom_right)
getEntries()
searchFrom_left()
use_isFound()