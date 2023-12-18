def solution(board, skill):
    N, M = len(board), len(board[0])
    
    # 누적합 배열 초기화
    acc_sum = [[0] * (M + 1) for _ in range(N + 1)]
    
    # 스킬 적용 (누적합 기법 사용)
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:  # 적의 공격 스킬
            degree = -degree
        # 시작 지점과 끝 지점에 마킹
        acc_sum[r1][c1] += degree
        acc_sum[r1][min(c2 + 1, M)] -= degree
        acc_sum[min(r2 + 1, N)][c1] -= degree
        acc_sum[min(r2 + 1, N)][min(c2 + 1, M)] += degree
    
    # 누적합 계산
    for i in range(N):
        for j in range(M):
            acc_sum[i][j + 1] += acc_sum[i][j]
    for j in range(M):
        for i in range(N):
            acc_sum[i + 1][j] += acc_sum[i][j]

    # 파괴되지 않은 건물의 개수 세기
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + acc_sum[i][j] > 0:
                count += 1
    
    return count
