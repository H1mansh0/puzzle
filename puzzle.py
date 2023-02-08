def gorizontal_checking(board: list[str]) -> bool:
    """
    The function do check if elem in list have more than one similar digt
    :param board: board of game
    :return: bool
    >>> check_digits([ "**** ****", "***1 ****", "**  3****", "* 4 1****",\
     "     9 5 "," 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    r = [i.replace('*', '') for i in board]
    for i in r:
        i = i.replace(' ', '')
        for k in i:
            if i.count(k) > 1:
                return False
    return True


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

