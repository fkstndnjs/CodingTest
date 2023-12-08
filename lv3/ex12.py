def solution(n, s, a, b, fares):
    # 플로이드-워셜 알고리즘을 위한 초기화
    inf = float('inf')
    dp = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    for fare in fares:
        dp[fare[0]][fare[1]] = fare[2]
        dp[fare[1]][fare[0]] = fare[2]

    # 모든 지점 쌍에 대해 최단 경로 계산
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # 합승을 고려한 최저 요금 계산
    min_cost = inf
    for i in range(1, n + 1):
        min_cost = min(min_cost, dp[s][i] + dp[i][a] + dp[i][b])

    return min_cost
