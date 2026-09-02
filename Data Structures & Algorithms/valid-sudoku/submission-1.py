import copy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = len(board)
        rows = len(board[0])
        rowLookup = {}
        colLookup = {}
        subBoxes = {}

        keys=[]
        for i in range(0, 9):
            rowLookup[i] = {}
            colLookup[i] = {}
            keys.append(i)
            if len(keys) == 3:
                subBoxes.update(dict.fromkeys(keys, {}))
                keys = []

        subBox = copy.deepcopy(subBoxes)
        for i in range(cols):
            if i == 3 or i == 6:
                subBox = copy.deepcopy(subBoxes)

            for j in range(rows):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] not in rowLookup[i]:
                    rowLookup[i][board[i][j]] = True
                else:
                    return False

                if board[i][j] not in colLookup[j]:
                    colLookup[j][board[i][j]] = True
                else:
                    return False

                if board[i][j] not in subBox[j]:
                    subBox[j][board[i][j]]=True
                else:
                    return False

        return True    

