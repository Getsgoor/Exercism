def is_triangle(sides):
    for i in range(3):
        if sides[i] + sides[(i+1)%3] < sides[(i+2) %3]:
            return False
    return bool(sides[0]*sides[1]*sides[2])
        


def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a == b == c and is_triangle(sides)


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return  (a == b or b == c or c ==a) and is_triangle(sides)

def scalene(sides):
    return not equilateral(sides) and not isosceles(sides) and is_triangle(sides)
