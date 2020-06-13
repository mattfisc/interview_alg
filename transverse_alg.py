
def spiral(grid):

         firstRow= 0
         lastRow = len(grid)
         firstCol = 0
         lastCol = len(grid[0])

         i=0

         while firstRow < lastRow and firstCol < lastCol:
             for i in range(firstCol,lastCol):
                 print(grid[firstRow][i],end=" ")
             firstRow+=1

             for i in range(firstRow,lastRow):
                 print(grid[i][lastCol-1],end=" ")
             lastCol-=1

             if firstRow < lastRow:
                 for i in range(lastCol-1,firstCol-1,-1):
                     print(grid[lastRow-1][i],end=" ")
                 lastRow-=1

             if firstCol < lastCol:
                 for i in range(lastRow-1,firstRow-1,-1):
                     print(grid[i][firstCol],end=" ")
                 firstCol+=1







grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

spiral(grid)