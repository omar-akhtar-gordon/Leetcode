class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        col=len(board[0])
        row=len(board)

        def findnei(r,c):
            nei=0
            for x in range(r-1,r+2):
                for y in range(c-1,c+2):
                    if ((x==r and y==c) or x<0 or y<0 or x==row or y==col):
                        continue
                    if board[x][y] in [1,3]:   
                        nei+=1
            return nei
                    
                  
        for x in range(row):
            for y in range(col):
                nei=findnei(x,y)
                if board[x][y]==1:
                    if nei in [2,3]:
                        board[x][y]=3
                elif nei==3:
                    board[x][y]=2
        
        for x in range(row):
            for y in range(col):
                if board[x][y]==1:
                    board[x][y]=0
                elif board[x][y] in [2,3]:
                    board[x][y]=1
                    
        





        