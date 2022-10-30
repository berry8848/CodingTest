#最頻値 (Mode)

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]*M
    print(A)

    for i in range(M):
        B[i] = A.count(i+1)
        print(B[i])
    
    print(max(B))
    

if __name__ == '__main__':
    main()
