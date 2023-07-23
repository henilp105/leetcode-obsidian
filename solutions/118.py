class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = [[1], [1, 1]]

        if numRows<3:
            return t[:numRows]
        for i in range(numRows-2):
            t.append([])
            t[i+2].append(1)
            for j in range(len(t[i+1])-1):
                t[i+2].append(t[i+1][j]+t[i+1][j+1])
            t[i+2].append(1)
        return t