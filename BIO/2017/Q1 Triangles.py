#Full Marks
def nextRow(row):
    if len(row) == 1:
        return (row[0])
    next = ""
    for i,block in enumerate(row):
        if i < len(row)-1:
            if block == row[i+1]:
                next += (block)
            else:
                lastCol = [colour for colour in colours if colour != block and colour != row[i+1]]
                next += (lastCol[0])
    return nextRow(next)
colours = ["R","G","B"]
while True:
    row = list(input())
    print(nextRow(row))