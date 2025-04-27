class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        columns=defaultdict(set)
        box=defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y]== ".":
                    continue 
                
                boxcheck=(x/3)*3 + (y/3)

                if board[x][y] in rows[x] or board[x][y] in columns[y] or board[x][y] in box[boxcheck]:
                    return False
                
                rows[x].add(board[x][y])
                columns[y].add(board[x][y])
                box[boxcheck].add(board[x][y])
        
        return True
