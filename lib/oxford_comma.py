def oxford_comma(items):
    length = len(items)
    if length < 2:
        return ''.join(items)
    elif length == 2:
        return ' and '.join(items)
    else:
        not_last = ', '.join(items[0:-1]) + ', and ' + str(items[-1])
        return not_last
