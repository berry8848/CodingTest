import sys
import math

def main():
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    lines = [[0]*3]*5
    lines = [input().split() for i in range(5)]
    lines = [[float(s) for s in x] for x in lines]
    print(lines)
    # for i in range(5):
    #     lines[i] = map(float, input().split())
    ans = 0
    next_num = lines.pop(0)

    while lines:
        min_distance = 10000
        for i, line in enumerate(lines): 
            distance_sq = kyori(next_num, line)
            if min_distance > distance_sq:
                min_distance = distance_sq
                next_num2 = i
        ans += math.sqrt(min_distance)
        next_num = lines.pop(next_num2)
    
    print(ans)

def kyori(x, y):
    kyori = (x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2
    return kyori

if __name__ == '__main__':
    # for l in sys.stdin:
    #     l.rstrip('\r\n')
    #     l1 = map(float, l)
    #     print(l1[0])
    #     lines.append(l1)
    # lines = [item.replace("'", "") for item in lines]
    # lines = list(map(float, lines))
    #lines = [[float(s) for s in lines.replace('"', '')]]
    main()
