def getEntries():
    global entry
    entry = ''
    entry = list(map(int, input("Type your entry: ").split(',')))
    print("Your entry is", entry)
def sort():
    print("\nno\n")
getEntries()
sort()