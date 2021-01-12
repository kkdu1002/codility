def solution(N):
    # write your code in Python 3.6
    ten = N
    binary = 0
    a = 0
    binary_fin = []
    count = 0
    count_fin = []
    big = 0
    #진법변환
    while(1):
        if ten == 1:
            binary_fin.append(ten)
            break
        else:
            a = int(ten / 2)
            binary = ten % 2
            binary_fin.append(binary)
            ten = a

    binary_fin = binary_fin[::-1]
    
    for i in range(len(binary_fin)):
        if binary_fin[i] == 0:
            count += 1
        else:
            count_fin.append(count)
            count = 0

    for i in range(1,len(count_fin)):
        if count_fin[i-1] > count_fin[i]:
            count_fin[i] = count_fin[i-1]
            big = count_fin[i]
        elif count_fin[i-1] < count_fin[i]:
            big = count_fin[i]
    return big
    pass