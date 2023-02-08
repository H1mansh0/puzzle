def gorizontal_checking(board):
    pass

def transformer(board: list) -> list:
    '''
    This function returns list of shifted rows to columns.
    >>> transformer(["**** ****","***  ****","  3****","* 3 1****","     9 5 "," 6  60  *","3  98  ","  8  2***","  4  ****"])
    ['****  3  ', '***  6   ', ' 3   84', '*     9  ', '  31 68  ', '****90 2*', '****   ', '****5 ***', '**** ****']
    >>> transformer('Hello!')
    False
    '''
    if not isinstance(board,list):
        return False
    columns = []
    for i in range(len(board[0])):
        columns.append(''.join([j[i] for j in board]))
    return columns

def blockchecker(board):
    pass

def validate_board(board) -> bool:
    pass
