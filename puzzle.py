def gorizontal_checking(board: list[str]) -> bool:
    """
    The function do check if elem in list have more than one similar digt
    :param board: board of game
    :return: bool
    >>> gorizontal_checking([ "**** ****", "***1 ****", "**  3****", "* 4 1****",\
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
def validate_board(board: list) -> bool:
    """
    Function checks if the board
    has the same numbers in lines,
    rows and same blocks
    
    >>> validate_board([
        "**** ****",
        "***1 ****",
        "**  3****",
        "* 4 1****",
        "     9 5 ",
        " 6  83  *",
        "3   1  **",
        "  8  2***",
        "  2  ****"
    ])
    False
    >>> validate_board([
        "**** ****",
        "***1 ****",
        "**  3****",
        "* 4 1****",
        "     9 5 ",
        " 6  83  *",
        "3   6  **",
        "  8  2***",
        "  2  ****"
    ])
    True
    """
    if isinstance(board, list):
        return (
            gorizontal_checking(board) and
            gorizontal_checking(transformer(board)) and
            gorizontal_checking(blockchecker(board)))
    return False
