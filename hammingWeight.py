def hammingWeight(n):
    
    weight = 0
    print format(n,'b')
    for i in format(n, 'b'):
        print i
        if i == '1': weight += 1
    return weight
    
print hammingWeight(11111111111111111111111111111101)