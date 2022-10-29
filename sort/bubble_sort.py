def getEntries():
    global entry
    entry = ''
    entry = list(map(int, input("Type your entry: ").split(',')))
    print("Your entry is", entry, "\n")

def sort():
    steps = 0
    for i in range (len(entry)-1, 0, -1):
        steps += 1
        for n in range(0, i):
            if entry[n] > entry[n+1]:
                memory = entry[n]
                entry[n] = entry[n+1]
                entry[n+1] = memory
    print("Your sorted sequence:", entry, "\nSteps taken:", steps)
    print("Comma-only form:", end=' ')
    for j in range(0, len(entry)):
        if j == len(entry)-1:
            print(entry[j])
        else:
            print(entry[j], end=',')

getEntries()
sort()