class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_no_duplicate_bounded(axis: list[str] | tuple[str]) -> bool:
            nums = []
            for elem in axis:
                if elem != ".":
                    if int(elem)<=9 and int(elem)>0:
                        nums.append(int(elem))
                    else:
                        return False
            
            hmap = {}
            for num in nums:
                hmap[num] = hmap.get(num,0)+1
                if hmap[num]>1:
                    return False
                else:
                    continue
                
            return True
        
        rows = []
        for i,row in enumerate(board):
            rows.append(check_no_duplicate_bounded(row))
        
        cols = []
        col_board = list(zip(*board))
        for i,col in enumerate(col_board):
            cols.append(check_no_duplicate_bounded(col))

        
        block33 = []
        blocK33_bool = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):

                grid_rows = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                block33.append(grid_rows)
                blocK33_bool.append(check_no_duplicate_bounded(grid_rows))

        if all(blocK33_bool) and all(cols) and all(rows):
            return True
        else:
            return False






        