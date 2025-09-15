class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in board: 
            store = {}
            for j in i:
                if j not in store:
                    store[j] = 1
                elif j == '.':
                    continue 
                else:
                    return False

        for i in range(len(board[0])):
            store2 = {}
            for j in board:
                if j[i] not in store2:
                    store2[j[i]] = 1 
                elif j[i] == '.':
                    continue
                else:
                    return False
        key = {
            0 : {
                0 : [],
                1 : [],
                2 : []
            },
            1 : {
                0 : [],
                1 : [],
                2 : []
            },
            2 : {
                0 : [],
                1 : [],
                2 : []
            }
        }
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in key[i//3][j//3]:
                    key[i // 3][j//3].append(board[i][j])
                elif board[i][j] == '.':
                    continue
                else:
                    return False

        return True