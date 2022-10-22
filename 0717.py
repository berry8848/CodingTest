def main():
    N = int(input())
    K = int(input())
    hear = list(input())
    print(hear)
    red = 0
    white = 0
    for a in hear:
        print(a)
        if a=='R':
            red += 1
        else:
            white += 1
    
    if K == red:
        print('W')
    else:
        print('R')
    

if __name__ == '__main__':
    main()