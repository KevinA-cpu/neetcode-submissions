class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        length = numCols * numRows
        l,r = 0, length-1
        def getMatrixCoordinates(mid):
            return ( mid // numCols, mid % numCols)
        while(l <= r):
            mid = l + (r-l)//2
            i,j = getMatrixCoordinates(mid)

            if matrix[i][j] > target:
                r = mid - 1
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                return True
        
        return False