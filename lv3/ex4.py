def solution(n, stations, w):
    answer = 0  # 증설해야 할 기지국 개수 초기값
    coverage = 2 * w + 1  # 하나의 기지국이 커버하는 아파트 범위
    
    position = 1  # 현재 탐색 중인 아파트 위치 초기화
    station_idx = 0  # stations 배열의 인덱스 초기화
    
    while position <= n:
        # 현재 아파트 위치가 기지국의 영향을 받지 않는 범위인 경우
        if station_idx < len(stations) and position >= stations[station_idx] - w:
            position = stations[station_idx] + w + 1
            station_idx += 1
        else:
            # 기지국의 영향을 받지 않는 범위에 있는 아파트에 새로운 기지국 설치
            position += coverage
            answer += 1
    
    return answer
