def solution(n, k, cmd):
    class Node:
        def __init__(self, idx):
            self.idx = idx
            self.prev = None
            self.next = None

    # 행들을 연결 리스트로 구현
    rows = [Node(i) for i in range(n)]
    for i in range(n - 1):
        rows[i].next = rows[i + 1]
        rows[i + 1].prev = rows[i]

    current = rows[k]  # 현재 선택된 행을 나타내는 포인터
    deleted = []  # 삭제된 행을 저장하는 스택

    for command in cmd:
        if command[0] == 'U':
            _, x = command.split()
            x = int(x)
            for _ in range(x):
                current = current.prev
        elif command[0] == 'D':
            _, x = command.split()
            x = int(x)
            for _ in range(x):
                current = current.next
        elif command[0] == 'C':
            deleted.append(current)
            prev_node = current.prev
            next_node = current.next
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
            if next_node:
                current = next_node
            else:
                current = prev_node
        elif command[0] == 'Z':
            row_to_restore = deleted.pop()
            prev_node = row_to_restore.prev
            next_node = row_to_restore.next
            if prev_node:
                prev_node.next = row_to_restore
            if next_node:
                next_node.prev = row_to_restore

    result = ['O'] * n
    for row in deleted:
        result[row.idx] = 'X'

    return ''.join(result)
