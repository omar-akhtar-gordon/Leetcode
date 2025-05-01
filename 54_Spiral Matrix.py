class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        left=0
        right=len(matrix[0])
        top=0
        bottom=len(matrix)
        total=bottom*right

        while len(result)<total:
            for x in range(left,right):
                result.append(matrix[top][x])
            top+=1

            for x in range(top,bottom):
                result.append(matrix[x][right-1])
            right-=1

            if not(left<right and top<bottom):
                break
            
            for x in range(right-1, left-1,-1):
                result.append(matrix[bottom-1][x])
            bottom-=1

            for x in range(bottom-1,top-1,-1):
                result.append(matrix[x][left])
            left+=1

        return result
            



        