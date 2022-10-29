def getEntries():
    global entry
    entry = ''
    entry = list(map(int, input("Type your entry: ").split(',')))
    print("Your entry is", entry, "\n")

def sort():
    steps = 0
    n = len(entry)
    for i in range(0, n-1):
        steps += 1
        minIndex = i
        for j in range(i+1, n):
            if entry[j] < entry[minIndex]:
                minIndex = j
        entry[i], entry[minIndex] = entry[minIndex], entry[i]
    print("Your sorted sequence:", entry, "\nSteps taken:", steps)
    print("Comma-only form:", end=' ')
    for k in range(0, len(entry)):
        if k == len(entry)-1:
            print(entry[k])
        else:
            print(entry[k], end=',')

getEntries()
sort()