def main():
    N, M = map(int, input().split())
    box_index = list(map(int, input().split()))
    key_index = list(map(int, input().split()))
    count = 0

    for box in box_index:
        if box in key_index:
            count += 1
    
    print(count)
    

if __name__ == '__main__':
    main()