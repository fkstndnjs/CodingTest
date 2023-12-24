def solution(k, room_number):
    answer = []
    room_dict = {}  # 방 번호와 배정된 방 번호를 저장할 딕셔너리

    def find_empty_room(request):
        if request not in room_dict:
            room_dict[request] = request
            return request
        else:
            next_request = find_empty_room(room_dict[request] + 1)
            room_dict[request] = next_request
            return next_request

    for request in room_number:
        next_empty_room = find_empty_room(request)
        answer.append(next_empty_room)

    return answer
