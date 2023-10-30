def move_zeros(lst):
    count = 0
    mst = []
    
    for num in lst:
        if num == 0:
            count += 1
        else:
            mst.append(num)
    mst.extend([0] * count)
    return mst
