def electronic_board(phrases, second):
    s = second % 28
    if s <= 14:
        return '_' * (14 - s) + phrases[0:s]
    return phrases[s-14:] + '_' * (s - 14)