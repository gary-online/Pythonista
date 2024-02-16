def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)

def test_perimeter():
    assert rectangle_perimeter(5, 7) == 24