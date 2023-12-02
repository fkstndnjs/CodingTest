def rotate_key(key):
    m = len(key)
    rotated_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated_key[j][m - 1 - i] = key[i][j]
    return rotated_key

def check(key, lock, x, y, m, n):
    # key를 lock에 적용
    extended_lock = [[0] * (n + 2 * m) for _ in range(n + 2 * m)]
    for i in range(n):
        for j in range(n):
            extended_lock[m + i][m + j] = lock[i][j]

    for i in range(m):
        for j in range(m):
            extended_lock[x + i][y + j] += key[i][j]

    # 자물쇠 영역 검사
    for i in range(n):
        for j in range(n):
            if extended_lock[m + i][m + j] != 1:
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    for _ in range(4):  # 4 방향으로 회전
        key = rotate_key(key)
        for x in range(1, m + n):
            for y in range(1, m + n):
                if check(key, lock, x, y, m, n):
                    return True
    return False