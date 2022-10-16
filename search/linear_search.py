def getEntry():
    print("Type in your entry.")
    entry = input(str())
def convert_entry_to_int_array():
    global entry
    global looking_for
    global memory
    entry = ""
    comma = ','
    steps = 0
    index = 0
    i = 0
    isDone = False
    entry = chr(entry)
    for isDone in range(False, True):
        for comma in range(','):
            if entry[index] == ',':
                index += 1
            elif entry[index] == '':
                isDone = True
                return
        memory[index] = entry[index]
        print("Memory value '", memory[index], "' retrieved")
getEntry()
convert_entry_to_int_array()