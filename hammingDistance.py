def hammingDistance(x, y):
    binX = format(x, 'b').zfill(32)
    binY = format(y, 'b').zfill(32)
    print binX, binY
    
    dis = 0
    for (i, j) in zip(binX, binY):
        if i != j: dis += 1
    
    return dis
    
print hammingDistance(1, 4)