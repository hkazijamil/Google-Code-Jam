def test():
    A = float(input())
    if A == 1 or A == 0:
        print(0.5, 0.0, 0.0)
        print(0.0, 0.5, 0.0)
        print(0.0, 0.0, 0.5)
    else:
        print((0.5 * A) / 2, 0.0, 0.0)
        print(0.0, (0.5 * A) / 2, 0.0)
        print(0.0, 0.0, 0.0)

    return True


for i in range(1, int(input()) + 1):
    print("Case #{}:".format(i))
    test()
