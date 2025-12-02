def square(number):
    """Calculate the number of grains of wheat on one of the squares of a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.
parameter ! number, the square we want to know the number of grain
Return : the number of grain on it"""
    
    if (number < 1 or number > 64):
        raise ValueError("square must be between 1 and 64")
        
    if (number != 1):
        return 2 * square(number-1)
    return 1


def total():
    """The total of grain on the chessboard"""
    return 2 ** 64 - 1