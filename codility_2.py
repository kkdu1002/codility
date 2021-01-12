def solution(A, K):
    # write your code in Python 3.6
    x = A
    y = K
    z = 0
    fin = 0
    while z < y:
        for i in range(len(x)-1,0,-1):
            fin = x[i-1]
            x[i-1] = x[i]
            x[i] = fin
        z += 1
    return x
    pass
