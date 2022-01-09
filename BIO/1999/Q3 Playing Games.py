while True:
    n = int(input())
    scores = [int(x) for x in input().split()]
    m = int(input())
    finals = [int(x) for x in input().split()]
    arr = [[]]
    arr[0] = [0,[]]
    arr += [[None,[]]] * (max(finals)+1)
    for i in range(1,len(arr)):
        minWays = 9999
        bestScore = None
        for score in scores:
            if i - score >= 0:
                if arr[i-score][0] is not None:
                    if arr[i-score][0] < minWays:
                        minWays = arr[i-score][0]
                        bestScore = score
        if bestScore is not None:
            ways = arr[i-bestScore][0] + 1
            path = arr[i-bestScore][1] + [bestScore]
            arr[i] = [ways,path]

    for final in finals:
        turns = arr[final][0]
        points = arr[final][1]
        counts = {}
        if turns == None:
            print("Impossible")
        else:
            for point in points:
                counts[point] = points.count(point)
            print(str(turns),  " ".join([str(point) + "x" +str(counts[point]) for point in set(points)]))


