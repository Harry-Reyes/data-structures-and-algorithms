# Data Structures and Algorithms

## Harry Reyes | BSIS 2

---

## Linear Search Algorithm

### Functions

1. getEntries() - User is requested to input a string list in a format of numbers separated by commas and the value converts into an integer list. Then, a number to find is requested.

2. searchFrom_left() - It is the first implementation of the linear search algorithm script which compares numbers by index from left to right.

3. searchFrom_right() - This is the second implementation of the script. The comparison is the same, but the list is reversed to say that it started from the lastest index.

4. use_isFound() - The variable isFound(), from searchFrom_left(), is used to confirm if any index matches with a number. It prints the index of a matching number and the steps made.

### Flow

- **Starting Point:** getEntries()
- **Next:** searchFrom_left()
- **Ending Point:** use_isFound()
        # if isFound() = true: searchFrom_right()