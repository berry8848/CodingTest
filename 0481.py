def main():
    a = [0]*3
    b = [0]*3
    win = 0
    
    for i in range(3):
        a[i], b[i] = map(int, input().split())

        if a[i] == 0:
            if b[i] == 0:
                pass
            elif b[i] == 1:
                win+=1
            else:
                win-=1
            
        if a[i] == 1:
            if b[i] == 0:
                win-=1
            elif b[i] == 1:
                pass
            else:
                win+=1

        if a[i] == 2:
            if b[i] == 0:
                win+=1
            elif b[i] == 1:
                win-=1
            else:
                pass
    
    if win>0:
        print(0)
    elif win<0:
        print(1)

    else:
        print(-1)


if __name__ == '__main__':
    main()


# 別解
# c = 0
# for i in range(3):
#     x, y = [int(x) for x in input().split()]
#     if (x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0):
#         c += 1
#     elif (x == 1 and y == 0) or (x == 2 and y == 1) or (x == 0 and y == 2):
#         c -= 1
#     else:
#         c += 0
# if c >= 1:
#     print(0)
# elif c == 0:
#     print(-1)
# else:
#     print(1)
