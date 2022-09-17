records = [1,2,3,4,5,6,7,8,9,10]
target = 16

def linear_search(records, target):
    for record in records:
        if record == target:
            return records.index(record)
    
    return False

print(linear_search(records, target))