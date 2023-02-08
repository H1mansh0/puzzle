def gorizontal_checking(board):
    pass

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
        return gorizontal_checking(board) and transformer(board) and blockchecker(board)
    return False
