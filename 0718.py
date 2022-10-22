def main():
    N, M = map(int, input().split())
    balls = [i + 1 for i in range(N)]
    print(balls)

    for _ in range(M):
        X, Y = map(int, input().split())
        balls[X-1] = Y

    for i in range(N):
        print(balls[i]) 

if __name__ == '__main__':
    main()