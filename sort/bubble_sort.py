def getEntries():
    global entry
    entry = ''
    entry = list(map(int, input("Type your entry: ").split(',')))
    print("Your entry is", entry, "\n")

def sort():
    steps = 0
    i = len(entry)-1
    while i > 0:
        n = 0
        steps += 1
        while n < i:
            if entry[n] > entry[n+1]:
                memory = entry[n]
                entry[n] = entry[n+1]
                entry[n+1] = memory
            n += 1
        i -= 1
    print("Your sorted sequence:", entry, "\nSteps taken:", steps)
    print("Comma-only form:", end=' ')
    for j in range(0, len(entry)):
        if j == len(entry)-1:
            print(entry[j])
        else:
            print(entry[j], end=',')

getEntries()
sort()