# Given a chess board having  cells (nxn), we need to place  queens 
# in such a way that no queen is attacked by any other queen. 
# A queen can attack horizontally, vertically and diagonally.        
    
def bactrackNQueens(col, comb, res):
    if col >= len(comb):
        res.extend(comb)
        return True
    for i in range(len(comb)):
        if isSafe(i, col, comb):
            comb[i][col] = 'Q'
            if (bactrackNQueens(col+1, comb, res)):
                return True
            comb[i][col] = '.'
    return False

# If you need all possible combinations i.e., permutations,
# the above bactrack logic looks like this.
# def bactrackNQueens(self, col, comb, res):
#     if col >= len(comb):
#         res.append(copy.deepcopy(comb))
#         return

#     for i in range(len(comb)):
#         if self.isSafe(i, col, comb):
#             comb[i][col] = 'Q'
#             self.bactrackNQueens(col+1, comb, res)
#             comb[i][col] = '.'


def isSafe(row, col, board):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1),
                    range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

if __name__ == '__main__':
  n = 4
  comb = []
  res = []
  for i in range(n):
      row = []
      for j in range(n):
          row.append('.')
      comb.append(row)
  if n == 1:
      print ([['Q']])
  bactrackNQueens(0, comb, res)
  print(res)