while True:
    steps = [x for x in input()]
    def vecAdd(a,b):
        return [a[0] + b[0],a[1]+b[1]]
    value = [1,1]

    beforeLeft = [1,0]
    beforeRight = [0,1]
    if steps[0] == "L":
        beforeLeft =[1,1]
    else:
        beforeRight = [1,1]

    for step in steps:
        if step == "L":
            beforeLeft = value
        else:
            beforeRight = value
        temp = value.copy()
        if step == 'L':
            value = vecAdd(beforeLeft,beforeRight)
            beforeLeft = temp
        else:
            value = vecAdd(beforeLeft,beforeRight)
            beforeRight = temp


    print("{} / {}".format(value[0],value[1]))
