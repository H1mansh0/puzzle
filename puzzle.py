def gorizontal_checking(board):
    pass

def transformer(board):
    pass

def blockchecker(board):
    '''
    This function returns True if blocks is True.
    >>> blockchecker(["**** ****","***  ****","**  3****","* 3 1****","     9 5 "," 6  60  *","3  98  **","  8  2***","  4  ****"])
    ['****  3   4  ****', '***  6  8  2***', '** 3   98  **', '*     60  *', '  31 9 5 ', '*******', '*****', '***', '*']
    >>> blockchecker('Text!')
    False
    '''
    if not isinstance(board,list):
        return False
    columns = transformer(board)
    rows = board

    new_rows = []
    for i in range(len(columns)):
        new_row = columns[i][:-i-1]+rows[-i-1][i:]
        new_rows += [new_row]
    return new_rows

def validate_board(board) -> bool:
    pass
