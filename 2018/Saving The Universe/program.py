def find_value(D, P):
    c = 0
    s = 0
    for p in P:
        if p == "C":
            c += 1
        else:
            s += pow(2, c)
            # print("C={}".format(pow(2, c)))
    return [c, s]


def test():
    D, P = input().split()
    D = int(D)
    # print("P={}".format(P))
    # print("D={}".format(D))

    # if D < P.count("C"):
    #     return "IMPOSSIBLE"
    # if 0 == P.count("C"):
    #     return "IMPOSSIBLE"
    # if D > P.count("C"):
    #     return 0
    c, s = find_value(D, P)
    idx = 0
    # print("c={}".format(c))
    # print("s={}".format(s))
    # print("idx={}".format(idx))

    while s > D:
        if "CS" in P:
            P = P.replace("CS", "SC", 1)
            # print("P::={}".format(P))
            idx += 1
            c, s = find_value(D, P)
            # print("c={}".format(c))
            # print("s={}".format(s))
            # print("idx={}".format(idx))
        else:
            return "IMPOSSIBLE"
    return idx


for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, test()))
