def sort():
    N = input()
    N = int(N)
    V = [int(i) for i in input().split()]
    done = False

    while not done:
        done = True
        theif = -1
        for i in range(N - 2):
            if V[i] > V[i + 2]:
                done = False
                V[i], V[i + 2] = V[i + 2], V[i]
            elif done:
                if theif == -1 and (not V[i] <= V[i + 1]):
                    theif = i
                elif theif == -1 and (not V[i + 1] <= V[i + 2]):
                    theif = i + 1
    # print(V)
    if not theif == -1:
        # Test
        # for i in range(N - 1):
        #     if not V[i] <= V[i + 1]:
        #         return [i, theif]
        return theif
    return "OK"


for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, sort()))
