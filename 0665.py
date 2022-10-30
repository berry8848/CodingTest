#Merge

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []

    while True:
        if not A and not B:
            break
        elif not A:
            C.append(B.pop(0))

        elif not B:
            C.append(A.pop(0))

        else:
            if A[0] <= B[0]:
                C.append(A.pop(0))

            else:
                C.append(B.pop(0))
    
    for x in C:
        print(x)

if __name__ == '__main__':
    main()

# 別解
# input()
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# a.extend(b)
# for i in sorted(a):
#     print(i)