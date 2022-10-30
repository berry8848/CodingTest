# 母音を数える

def main():
    N = int(input())
    S = list(input())
    boin = ['a', 'i', 'u', 'e', 'o']
    count = 0
    for x in S:
        if x in boin:
            count+=1
    print(count)





if __name__ == '__main__':
    main()