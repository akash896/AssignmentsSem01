def get_product(Fx, Gx):
    map = {}
    for i in Gx:
        for j in Fx:
            prod = i + j
            if prod in map:
                map[prod] = map[prod] + 1
            else:
                map[prod] = 1
    res = []
    for i in map:
        if map[i] % 2 == 1:
            res.append(i)
    return res

def get_mod(FxGx, Mx):
    Ax = FxGx
    if Mx[0] > Ax[0]:
        return Ax
    map = {}
    for i in Ax:
        if i in map:
            map[i] = map[i] + 1
        else:
            map[i] = 1

    diff = Ax[0] - Mx[0]
    for j in Mx:
        new_j = j + diff
        if new_j in map:
            map[new_j] = map[new_j] + 1
        else:
            map[new_j] = 1
    newFxGx = []
    for i in map:
        if map[i] % 2 == 1:
            newFxGx.append(i)
    newFxGx.sort(reverse=True)
    return get_mod(newFxGx, Mx)


if __name__ == '__main__':
    in1 = str(input())  # input 1st polynomial
    in2 = str(input())  # input second polynomial
    Fx, Gx = ([], [])
    Mx = [128, 7, 2, 1, 0] # mod polynomial values
    fx = in1.split(" ")
    gx = in2.split(" ")
    for i in fx:    # creating Fx with 1st input
        Fx.append(int(i))
    for j in gx:    # creating Gx with 2nd input
        Gx.append(int(j))

    FxGx = get_product(Fx, Gx)
    FxGx.sort(reverse=True)
    result = get_mod(FxGx, Mx)
    print(result)

"""
SAMPLE 1
in1 = "123 120 118 115 39 10 3 1"
in2 = "120 32 11 3" 
output = [122, 119, 118, 116, 115, 113, 111, 110, 109, 108, 107, 71, 50, 38, 35, 34, 32, 28, 27, 25, 23, 22, 20, 19, 14, 12, 10, 9, 7, 5, 4, 3, 1]

SAMPLE2
in1 = "119 23 10 2"
in2 = "118 31 39 11 2 0"
output = [121, 120, 119, 116, 111, 110, 109, 62, 54, 49, 37, 34, 33, 32, 31, 30, 29, 25, 24, 22, 21, 20, 15, 14, 12, 10, 9, 7, 3, 2, 1, 0]


"""