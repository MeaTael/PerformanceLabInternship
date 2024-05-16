import sys


def check(x1, y1, x2, y2, r2):
    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if distance < r2 ** 2:
        return 1
    elif distance == r2 ** 2:
        return 0
    else:
        return 2


if __name__ == '__main__':
    _, circlePath, pointsPath = sys.argv

    with open(circlePath, 'r') as circleFile:
        xc, yc = list(map(int, circleFile.readline().split(' ')))
        r = int(circleFile.readline())

    with open(pointsPath, 'r') as pointsFile:
        line = pointsFile.readline()
        while line:
            x, y = list(map(int, line.split(' ')))
            print(check(x, y, xc, yc, r))
            line = pointsFile.readline()
