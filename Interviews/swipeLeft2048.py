# * Empty squares are indicated by 0.
# * All number tiles slide all the way to the left.
# * When two identical numbers collide they combine to create the sum of the two numbers.

# The function should take a list of integers representing one row of the grid and return that row after swiping left once. For example:

# [0, 2, 4, 2] -> [2, 4, 2, 0]
# [4, 0, 0, 4] -> [8, 0, 0, 0]
# [2, 0, 2, 4] -> [4, 4, 0, 0]

def swipeLeft(row):
    # store length of row
    length = len(row)
    # remove all 0's from row
    row = [num for num in row if num != 0]
    # add 0's to end of row
    while len(row) < length:
        row.append(0)
    # combine like numbers and append 0's to end of row
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            row[i] = row[i] * 2
            row.pop(i+1)
            row.append(0)
    return row

def swipeRight(row):
    row = swipeLeft(row[::-1])
    row = row[::-1]
    return row

print(swipeRight([4, 2, 0, 2]))