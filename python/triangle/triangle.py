
def equilateral(sides):
    a,b,c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a == b and a == c and c == b:
        return True
    else:
        return False


def isosceles(sides):
    a,b,c = sides
    if testTriangle(sides):
        pass
    else:
        return False
    if (a == 0 or b == 0 or c == 0):
        return False
    if a == b and a == c and c == b:
        return True
    if a == b and b != c:
        return True
    if a == c and c != b:
        return True
    if b == c and c != a:
        return True
    else:
        return False


def scalene(sides):
    a,b,c = sides
    if testTriangle(sides):
        pass
    else:
        return False
    if (a == 0 or b == 0 or c == 0):
        return False
    if a == b and a == c and c == b:
        return False
    if a == b and b != c:
        return False
    if a == c and c != b:
        return False
    if b == c and c != a:
        return False
    if a != b and b != c:
        return True
    else:
        return False
    pass

def testTriangle(sides):
    a,b,c = sides
    return (a + b > c) and (b + c > a) and (a + c > b)
