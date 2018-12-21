idict = {'#': 1, '.': 0}  # 입력시 사용할 사전


def boardinput(H, W):
    res = []
    for i in range(0, H):
        res.append([])
        row = list(input())
        for j in range(0, W):
            res[-1].append(idict[row[j]])
    return res

W, H = 0 ,0  # 보드의 폭, 높이
coverType = (((0, 0), (1, 0), (0, 1)), ((0, 0), (0, 1), (1, 1)), ((0, 0), (1, 0), (1, 1)), ((0, 0), (1, 0), (1, -1)))  # 기준 칸에 대해 오른쪽/아래로 향하는 조각의 배치
board = []  # 보드


def set(y, x, type, delta):  # 좌표 y, x를 기준으로, type의 위치에 조각을 배치하거나(delta == 1), 없앤다(delta == -1)
    global W, H, coverType, board
    ok = True  # 이 배치는 유효한가?
    for i in range(0, 3):  # 트리노미노의 세 칸에 대해 iterate
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        if ny < 0 or ny >= H or nx < 0 or nx >= W:  # 보드 이탈
            ok = False
            continue
        board[ny][nx] += delta
        if board[ny][nx] > 1:  # 검은 칸/덮인 칸에 덮으려는 시도
            ok = False
    return ok


def cover():  # 재귀적으로 보드를 왼쪽 위부터 차례대로 덮어 나간다
    global W, H, board
    y, x = -1, -1
    for i in range(0, H):  # 덮이지 않은 흰 칸을 찾는다
        for j in range(0, W):
            if not board[i][j]:  # 흰 칸 발견
                y = i
                x = j
                break
        if y >= 0:  # 흰 칸 발견
            break

    if y == -1:  # 모든 칸이 덮였다면 1을 반환
        return 1
    ret = 0
    for type in range(0, 4):  # 새로운 조각을 배치 시도한다
        if set(y, x, type, 1):  # 배치 가능하다면 그 상태에서 재귀한다
            ret += cover()  # 재귀적으로 경우의 수를 더한다
        set(y, x, type, -1)  # 배치했던 조각을 제거 후 iterate한다

    return ret


def main():
    global W, H, board, idict
    C = int(input())
    for tc in range(0, C):
        H, W = map(int, input().split())  # 폭, 높이 입력을 받는다.
        board = boardinput(H, W)
        count = cover()
        print(count)


if __name__ == "__main__":
    main()
