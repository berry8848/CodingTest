import numpy as np
from numpy.linalg import norm

def main():
    A = list(map(float, input().split())) # A点の座標入力
    B = list(map(float, input().split())) # B点の座標入力
    n = int(input()) # 各チームが提出する個数を入力

    # 候補点をlistに格納
    candidate_points = [input().split() for _ in range(3*n)]
    candidate_points = [[float(s) for s in x] for x in candidate_points]

    #list → numpy変換
    A = np.array(A) 
    B = np.array(B)
    candidate_points = np.array(candidate_points)

    # 最短距離格納用
    min_distance_R = 100000
    min_distance_G = 100000
    min_distance_B = 100000

    # Rチームの記録
    for i in range(0, 3*n, 3):
        # 各候補点の最短距離を計算
        distance = calc_distance(A, B, candidate_points[i])
        # 最短距離が更新されたかを確認
        if distance < min_distance_R:
            min_distance_R = distance
    
    # Gチームの記録
    for i in range(1, 3*n, 3):
        # 各候補点の最短距離を計算
        distance = calc_distance(A, B, candidate_points[i])
        # 最短距離が更新されたかを確認
        if distance < min_distance_G:
            min_distance_G = distance

    # Bチームの記録
    for i in range(2, 3*n, 3):
        # 各候補点の最短距離を計算
        distance = calc_distance(A, B, candidate_points[i])
        # 最短距離が更新されたかを確認
        if distance < min_distance_B:
            min_distance_B = distance
    
    # 各チームの記録を比較して優勝を決定
    d = {'R':min_distance_R, 'G':min_distance_G, 'B':min_distance_B}
    print(min(d, key=d.get))
    print(min(d.values()))


# 線分と候補点の最短距離を計算
def calc_distance(a, b, p):
    #APベクトル、ABベクトル、BAベクトル、BPベクトルを生成
    ap = p - a
    ab = b - a
    ba = a - b
    bp = p - b

    #線分上で一番近い点が点Aであったとき
    if np.dot(ap, ab) < 0:
        distance = norm(ap)

    #線分上で一番近い点が点Bであったとき
    elif np.dot(bp, ba) < 0:
        distance = norm(bp)
    
    #線分上で一番近い点が点Aでも点Bでもなかったとき
    else:
        ai_norm = np.dot(ap, ab)/norm(ab)
        neighbor_point = a + (ab)/norm(ab)*ai_norm
        distance = norm(p - neighbor_point)
    return (distance)


if __name__ == '__main__':
    main()