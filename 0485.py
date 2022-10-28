# 徴収官

def main():
    N, M = map(int, input().split())
    ths = [[0]*2]*M
    for i in range(M):
        ths[i] = list(map(int, input().split()))
    house = [0]*N
    money = 0
    flg=False
    index1 = ths[0][1]-1
    index2 = ths[1][1]-1

    house[index1] = 1
    money += ths[0][0]
    house[index2] = 1
    money += ths[1][0]    

    while True:
        if index2 > index1:
            while house[index1]==1:
                index1+=1
                if index1 >= N:
                    flg = True
                    break
            if flg:
                break 
            house[index1] = 1
            money += ths[0][0]
        else:
            while house[index2]==1:
                index2+=1
                if index2 >= N:
                    flg = True
                    break
            if flg:
                break    
            house[index2] = 1
            money += ths[1][0] 
        print('Index1 ', index1)
        print('Index2 ', index2)   
        print(money)



    print(money)



if __name__ == '__main__':
    main()