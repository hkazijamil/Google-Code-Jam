import sys


def solve():
    sys.stdout.flush()
    print(10, 10)
    sys.stdout.flush()

    i1 = i2 = 10 - 1
    j1 = j2 = 10 + 2
    b = []
    c = [po[:] for po in [[None] * 225] * 225]

    for x1 in range(i1, j1):
        for y1 in range(i2, j2):
            b.append([x1, y1])

    x, y = map(int, input().split())
    if x == -1 or y == -1:
        return True
    elif x == 0 or y == 0:
        return True
    c[x][y] = [10, 10]
    pl = 0

    while pl <= 1000:
        for pk in b:
            x1, y1 = pk
            while c[x1][y1] == None or (x1 != x or y1 != y):
                sys.stdout.flush()
                print(x1, y1)
                sys.stdout.flush()
                x, y = map(int, input().split())
                pl += 1
                if x == -1 or y == -1:
                    return True
                elif x == 0 or y == 0:
                    return True
                c[x][y] = [x1, y1]

    return True


T = int(input())
for _ in range(T):
    A = input()
    solve()
