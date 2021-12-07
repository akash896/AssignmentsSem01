import numpy as np
from sympy import *

class Solution:
    def __init__(self):
        pass

    def FindMIndependentColumns(self, m, A):
        # Write your code here. Please do not change the return statement.
        # A is a numpy array of dimensions d x n.
        # return a numpy array of dimensions d x m.
        ans = np.zeros((A.shape[0], m), dtype=np.float32)
        original_matrix = A.tolist()
        dim1 = len(A)
        dim2 = len(A[0])
        indCol = []
        AN = Matrix(A)
        ref = AN.rref()
        l_matrix = ref[0].tolist()
        for ind in range(m):
            column = []
            col = 0
            for index in range(dim2):
                if l_matrix[ind][index] == 1:
                    col = index
                    break
            for i in range(dim1):
                column.append(original_matrix[i][col])
            indCol.append(column)
            #print("indCol = ", indCol)
            verticalCol = []
            for i in range(len(indCol[0])):
                # print(i)
                row = []
                for item in indCol:
                    row.append(item[i])
                verticalCol.append(row)
            ans = np.array(verticalCol)
        #print("ans = ", ans)
        return ans

    def Wrapper(self, m, n, a):
        d = len(a) // n
        A = np.zeros((d, n), dtype=np.float32)

        c = 0
        for i in range(d):
            for j in range(n):
                A[i][j] = a[c]
                c += 1

        B = self.FindMIndependentColumns(m, A)

        res = []
        for i in range(d):
            for j in range(m):
                res.append(B[i][j])

        return res

ob = Solution()
m = 3
n = 5
a = [1, 0, 0, 1, 0,
     0, 1, 0, 0, 1,
     0, 0, 1, 1, 1]
print(ob.Wrapper(m, n, a))