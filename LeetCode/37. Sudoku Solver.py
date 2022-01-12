class Solution(object):
    def isValid(self, board,i,j,k):
        for p in range(9):
            if(board[i][p]==k or board[p][j]==k):
                return False

            if(board[3*(i//3)+p//3][3*(j//3)+p%3]==k):
                return False;
        return True



    def solve(self,board):
        l=["1","2","3","4","5","6","7","8","9"]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=="."):
                    for k in l:
                        if(self.isValid(board,i,j,k)):
                            board[i][j]=k;
                            if(self.solve(board)==True):
                                return True;
                            else:
                                board[i][j]=".";
                    return False;

        return True;                                




    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solve(board);

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    ob=Solution();
    ob.solveSudoku(board)
    print(board)