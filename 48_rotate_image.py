class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        left=0
        right=len(matrix)-1

        while left<right:
            for x in range(right-left):
                top=left
                bottom=right

                placehold=matrix[top][left+x]

                matrix[top][left+x]=matrix[bottom-x][left]

                matrix[bottom-x][left]=matrix[bottom][right-x]

                matrix[bottom][right-x]=matrix[top+x][right]

                matrix[top+x][right]=placehold
            right-=1
            left+=1
