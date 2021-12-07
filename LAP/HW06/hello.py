import numpy as np

def rref(A, m):
    ans = []
    # augMat = A
    # t = len(A)
    # for i in range(0, t):
    #     if augMat[i][i] == 0:
    #         c = 1
    #         while (i + c) < t and augMat[i + c][i] == 0:
    #             c += 1
    #         if (i + c) == t:
    #             break
    #         j = i
    #         for k in range(0, len(A[0])):
    #             temp = augMat[j][k]
    #             augMat[j][k] = augMat[j + c][k]
    #             augMat[j + c][k] = temp
    #     for j in range(0, t):
    #         if i != j:
    #             ratio = augMat[j][i] / augMat[i][i]
    #             for k in range(0, len(A[0])):
    #                 augMat[j][k] = augMat[j][k] - ratio * augMat[i][k]
    # count = 0
    # print("Aug = ", augMat)
    count = 0
    t=4
    m=2
    A = [
            [0, 2, 3, 4, 2],
            [0, 5, 6, 7, 4],
            [0, 8, 9, 10, 8],
            [0,0,0,0, 0]]
    augMat = [[1,0,0,0, 0], [0,1,0,0, 0],[0,0,0,0, 0],[0,0,0,0, 0]]
    for i in range(0, t):
        temp = augMat[i]
        for k in range(0, len(temp)):
            if temp[k] != 0.0:
                break
        index = k
        for j in range(0, t):
            ans[j][count] = A[j][index]
        count = count + 1
        if count == m:
            break
    print(ans)
    return ans
A = np.array( [
            [0, 2, 3, 4, 2],
            [0, 5, 6, 7, 4],
            [0, 8, 9, 10, 8]])
print(rref(A,3))
