while True:
    isbn = [x for x in input()]
    missing = isbn.index("?")
    total = 0
    next = 0
    for i,x in enumerate(isbn):
        if x != "?":
            if x == "X":
                total += 10
            else:
                total += (10-i) * int(x)

    for i in range(1,11):
        if (total + (10 - missing) * i ) % 11 == 0:
            next = i
            break
    if next == 10:
        print("X")
    else:
        print(next)





