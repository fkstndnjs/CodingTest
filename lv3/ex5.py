def solution(n, t, m, timetable):
    # 시간을 분 단위로 변환하는 함수
    def time_to_minutes(time):
        hh, mm = map(int, time.split(':'))
        return hh * 60 + mm
    
    # 대기 크루의 도착 시간을 분 단위로 정렬
    timetable.sort(key=lambda x: time_to_minutes(x))
    
    last_time = 9 * 60  # 셔틀의 첫 도착 시간
    for i in range(n):
        # 셔틀에 탈 수 있는 크루 수
        available_seats = m
        
        while timetable and time_to_minutes(timetable[0]) <= last_time:
            # 현재 대기 크루가 셔틀에 탑승 가능한 경우
            if available_seats > 0:
                available_seats -= 1
                last_crew_time = timetable.pop(0)
            else:
                break
        
        if i == n - 1:  # 마지막 셔틀인 경우
            if available_seats == 0:
                # 셔틀이 꽉 찼으면 마지막 크루보다 1분 일찍 나가야 함
                last_time = time_to_minutes(last_crew_time) - 1
            else:
                # 셔틀에 자리가 남아있으면 셔틀 도착 시간에 나가면 됨
                last_time = 9 * 60 + (n - 1) * t
        else:
            last_time += t  # 다음 셔틀 도착 시간 설정
    
    # 결과를 HH:MM 형식으로 변환하여 반환
    return f'{last_time // 60:02}:{last_time % 60:02}'
