def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # 진출 지점을 기준으로 정렬
    
    print(routes)
    
    camera = -30001  # 카메라 초기 위치 (가능한 가장 작은 값)
    
    for route in routes:
        print(camera, route[0])
        if camera < route[0]:  # 현재 카메라의 위치가 차량의 진입 지점보다 작으면
            answer += 1  # 카메라를 설치하고
            camera = route[1]  # 카메라 위치를 차량의 진출 지점으로 업데이트
    
    return answer