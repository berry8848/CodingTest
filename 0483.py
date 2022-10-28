# パスタの茹で具合

def main():
    N = int(input())
    result = [[0]*2]*N
    #print(result)

    for i in range(N):
        result[i] = list(map(int, input().split()))

    # 昇順
    result = sorted(result, key=lambda x: (x[0], x[1])) 

    min0 = 100000000000000
    max0 = -1
    min1 = 100000000000000
    max1 = -1    
    min2 = 100000000000000
    max2 = -1

    for a in result:
        #茹で足りないとき
        if a[1] == 0:
            if int(a[0]) < min0:
                min0 = a[0]
            if int(a[0]) > max0:
                max0 = a[0]

        # ちょうど良いとき
        if a[1] == 1:
            if int(a[0]) < min1:
                min1 = a[0]
            if int(a[0]) > max1:
                max1 = a[0]

        # 茹ですぎのとき
        if a[1] == 2:
            if int(a[0]) < min2:
                min2 = a[0]
            if int(a[0]) > max2:
                max2 = a[0]

    M = int(input())
    for i in range(M):
        exam = int(input())
        if exam<=max0:
            print(0)
        elif min1<=exam and exam<=max1:
            print(1)
        elif min2<=exam:
            print(2)
        else:
            print(-1) 

if __name__ == '__main__':
    main()
