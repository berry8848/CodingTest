#惑星探査(Planetary Exploration)

def main():
    h, w = map(int, input().split())
    k = int(input())
    mp = [list(input()) for _ in range(h)]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        J = 0
        O = 0
        I = 0
        for i in range(a-1, c, 1):
            for j in range(b-1, d, 1):
                if mp[i][j] == 'J':
                    J += 1
                elif mp[i][j] == 'O':
                    O += 1
                elif mp[i][j] == 'I':
                    I += 1
        print(str(J) + ' '+ str(O) +' '+ str(I))


if __name__ == '__main__':
    main()
