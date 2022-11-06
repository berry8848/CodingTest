#勇者ビ太郎(Bitaro the Brave)

def main():
    h, w = map(int, input().split())
    mp = [list(input()) for _ in range(h)]
    ans = 0
    ci = [0 for _ in range(w)]

    for i in range(h-1, -1, -1):
        co = 0
        for j in range(w-1, -1, -1):
            if mp[i][j] == 'J': #i,j
                ans += co * ci[j]
            elif mp[i][j] == 'O': #i,l
                co += 1
                
                
            elif mp[i][j] == 'I': #k,j
                ci[j] += 1
            
    print(ans)

if __name__ == '__main__':
    main()
