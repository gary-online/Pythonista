def get_perimeter(length, breadth):
    if length == 0 or breadth == 0:
        raise ValueError('Invalid Input!')
    return 2 * (length+breadth)