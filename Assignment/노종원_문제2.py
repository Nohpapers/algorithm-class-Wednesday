def knapSack_dp(W, wt, val, n):
    # 1. DP 테이블 초기화
    A = []
    for i in range(n + 1):
        row = []
        for w in range(W + 1):
            row.append(0)
        A.append(row)

    # 2. DP 테이블 채우기
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if w < wt[i-1]:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w - wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)

    return A


def backtracking_item(A, W, wt, n):
    selected_items = []
    w = W

    for i in range(n, 0, -1):
        if A[i][w] != A[i-1][w]:
            selected_items.insert(0, i-1)
            w -= wt[i-1]

    return selected_items


item = ["노트북", "카메라", "책", "옷", "휴대용 충전기"]
wt = [3, 1, 2, 2, 1]
val = [12, 10, 6, 7, 4]
n = len(val)

# 사용자 입력 처리
back_weight = input("배낭 용량을 입력 하세요 : ")

if back_weight.isdigit():
    W = int(back_weight)

    if W <= 0:
        print("1 이상의 자연수를 입력하세요.")
        exit()

    # DP 테이블 생성
    A = knapSack_dp(W, wt, val, n)

    # 최대 가치
    max_score = A[n][W]

    # 선택된 물건 인덱스
    selected_idx = backtracking_item(A, W, wt, n)

    # 인덱스를 물건 이름으로 변환
    selected_items = [item[i] for i in selected_idx]

    # 결과 출력
    print(f"최대 만족도: {max_score}")
    print(f"선택된 물건: {selected_items}")

else:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")