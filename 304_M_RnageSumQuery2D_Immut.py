# DP Memorization

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.originMat = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.__getOriginRegion(row2, col2) \
               - self.__getOriginRegion(row1 - 1, col2) \
               - self.__getOriginRegion(row2, col1 - 1) \
               + self.__getOriginRegion(row1 - 1, col1 - 1) 
        
    def __getOriginRegion(self, row: int, col: int) -> int:
        if row < 0 or col < 0:
            return 0
        
        if self.originMat[row][col] is None:
            self.originMat[row][col] = self.__getOriginRegion(row - 1, col) \
                                + self.__getOriginRegion(row, col - 1) \
                                + self.matrix[row][col] \
                                - self.__getOriginRegion(row - 1, col - 1)
        return self.originMat[row][col]
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
