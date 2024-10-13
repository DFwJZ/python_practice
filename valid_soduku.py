from typing import List
from collections import defaultdict

class Solution:
    def isValidSoduku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squres = defaultdict(set)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squres [(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squres[(r//3, c//3)].add(board[r][c])

        return True
                


def main():
    solution = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(solution.isValidSoduku(board))

if __name__ == '__main__':
    main()   

