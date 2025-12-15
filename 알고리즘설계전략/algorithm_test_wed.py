#============================
# 예제: 리스트에서 최대값 찾는 문제의 알고리즘 작성
# 성능 분석 비교연산과 이동연산 기준
#=============================
def find_max(A):
    n = len(A) # 입력 크기
    move = 0 # 이동 연산 횟수
    cmp = 0 # 비교 연산 횟수

    max_val = A[0] # 최대값 초기화
    move += 1 # 이동 연산 횟수 

    for i in range(n): # 1~ n-1까지 반복
        cmp += 1 # 비교연산 횟수
        if A[i] > max_val:
            max_val = A[i] 
            move += 1 # 이동 연산 회수
    return max_val, cmp, move
#==========================================
# 정렬 알고리즘
#===========================================
def selection_sort(arr): # 선택 정렬
    a = arr[:] # 원본 복사 
    n = len(arr) # 입력 크기
    for i in range(n-1): # i 번째 위치에 최소값 선택 배치
        min_idx = i # 최소값 인덱스
        for j in range (i+1, n): # 미정렬 구간 탐색
            if a[j] < a[min_idx]: # 더 작은값을 발견
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i] # i번째 위치와 최소값 위치 교환
    return a

def insertion_sort(arr): # 삽입정렬
    a = arr[:] # 원본 복사 
    n = len(arr) # 입력 크기
    for i in range(1,n):# 두 번째 요소부터 시작
        key = a[i] # 삽입할 요소 
        # 삽입할 요소의 삽입 위치 찾기
        j = i-1 # 정렬된 구간의 마지막 요소의 위치
        while j >= 0 and a[j] > key : 
            a[j + 1] = a[j] # 뒤쪽으로 한칸 이동
            j -= 1 # 왼쪽으로 한칸 이동
        a[j + 1] = key # 삽입할 위치 j + 1
    return a

#=====================
# 데스트 실행
#======================
if __name__ == "__main__":
    data = [3, 9, 2, 7, 5, 10, 4]
    #result, comp_count, move_count = find_max(data)
    #print(f"최대값 : {result}, 비교연산횟수 : {comp_count}, 이동연산횟수 : {move_count}") 
    # sorted_array = selection_sort(data) 
    sorted_array = insertion_sort(data)       
    print(f"최대값 : {sorted_array},")    

   
    
            
    
