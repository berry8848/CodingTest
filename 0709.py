#Python 
def main():
    N = int(input())
    S = input().strip()
    list = ['A', 'B', 'C', 'D', 'E']
    count = 0

    for char in list:
        if char in S:
            count += 1
    if count >= 3:
        print('Yes')
    else:
        print('No')
    

if __name__ == '__main__':
    main()