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

def transformer(board):
    pass

def blockchecker(board):
    pass

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
