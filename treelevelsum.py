def sumr(tree):
    if tree[0] == "null":
        return 0
    level = 1
    sum = 0
    for i in range (len(tree)):
        if tree[i] == "null":
            continue
        if int(tree[i])<0:
            continue
        sum = sum + int(tree[i])
        if i == (2**level):
            level +=1
            print(sum)
            sum = 0
            

tree = input()
sumr(tree)