def solution(m, n, puddles):
    # dp 배열을 초기화합니다. (m+1) x (n+1) 크기
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점
    
    # 물웅덩이 위치에 -1을 설정합니다.
    for x, y in puddles:
        dp[y][x] = -1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 물웅덩이가 있는 위치면 건너뜁니다.
            if dp[i][j] == -1:
                continue
            
            # 왼쪽에서 오는 경우
            if dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1]
            
            # 위쪽에서 오는 경우
            if dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j]
            
            dp[i][j] %= 1_000_000_007
    
    return dp[n][m]
