#文字列の反転

def main():
    N, A, B = map(int, input().split())
    S = list(input())
    S_reverse = S[A-1:B]
    print(S_reverse)
    S_reverse.reverse()
    a = ''.join(S[0:A-1]+S_reverse[:]+S[B:])
    print(a) 

if __name__ == '__main__':
    main()
