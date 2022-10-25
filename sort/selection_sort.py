def getEntries():
    global entry
    entry = ''
    entry = list(map(int, input("Type your entry: ").split(',')))
    print("Your entry is", entry, "\n")

def sort():
    steps = 0
    i = 0
    n = len(entry)
    while i < n - 1:
        steps += 1
        minIndex = i
        j = i + 1
        while j < n:
            if entry[j] < entry[minIndex]:
                minIndex = j
            j += 1
        memory = entry[minIndex]
        entry[minIndex] = entry[i]
        entry[i] = memory
        i += 1
    print("Your sorted sequence:", entry, "\nSteps taken:", steps)
    print("Comma-only form:", end=' ')
    for k in range(0, len(entry)):
        if k == len(entry)-1:
            print(entry[k])
        else:
            print(entry[k], end=',')

getEntries()
sort()