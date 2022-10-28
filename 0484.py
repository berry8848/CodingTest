# トラックの周回記録

def main():
    N, T = map(int, input().split())
    time = list(map(int, input().split()))
    b = 0
    overtime = 0
    count = 0 # 記録用
    over = 0 #時間を連続で超えた回数

    for i in range(N):
        time[i] = time[i] - b
        b += time[i]

        if T + overtime > time[i]: #制限時間に間に合わなかった場合
            over +=1
            overtime = T + overtime - time[i]
            #print(overtime)
        else: # 制限時間に間に合った場合
            count +=1
            over = 0
            overtime = 0
        
        if over >=2:
            break
        
    

    print(count)



if __name__ == '__main__':
    main()