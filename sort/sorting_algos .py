import random
import time
import matplotlib.pyplot as plt # type: ignore
from collections import deque


#=======================================================
# 1. 정렬 알고리즘 
#=======================================================

def selection_sort(arr): # 선택 정렬    
    a= arr[:] # 원본 복사 
    n = len(arr) # 입력 크기 
    for i in range(n-1): # i번째 위치에 최소값 선택 
        min_idx = i # 최소 값 인덱스 
        for j in range(i+1, n):
            if a[j] < a[min_idx]: # 더 작은 값을 발견하게 된다면
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i] # i 번째 위치와 최소값 위치를 교환 
    return a

def insertion_sort(arr): # 삽입 정렬
    a= arr[:] # 원본 복사 
    n = len(arr) # 입력 크기 
    for i in range(1,n): # 두번째 요소부터 시작 
        key = a[i] #삽입할 요소 
        j = i-1
        # 삽입할 요소의 삽입 위치 찾기
        while j>=0 and a[j]>key:
            a[j+1] = a[j] # 뒤 쪽으로 한칸 이동 
            j -= 1 # 왼쪽으로 한칸 이동 
        a[j+1] = key # 삽입할 위치 j+1
    return a

def quick_sort(arr, left, right):  # 퀵 정렬
    def partition(A, left, right):
        pivot = A[left]
        low = left + 1
        high = right

        while low <= high:
            # low는 high를 넘지 않는 한에서 피벗보다 큰 값을 찾을 때까지 이동
            while low <= high and A[low] <= pivot:
                low += 1
            # high는 low를 넘지 않는 한에서 피벗보다 큰(또는 >일 경우) 값을 찾을 때까지 이동
            while low <= high and A[high] > pivot:
                high -= 1

            if low <= high:   # 교차되지 않았을 때만 교환
                A[low], A[high] = A[high], A[low]
                low += 1
                high -= 1
            else:
                break

        # pivot을 최종 위치인 high와 교환 (high는 pivot 이하의 마지막 인덱스)
        A[left], A[high] = A[high], A[left]
        return high

    if left < right:
        q = partition(arr, left, right)
        quick_sort(arr, left, q - 1)
        quick_sort(arr, q + 1, right)
    return arr


    if left < right: # 정렬할 원소가 2개 이상인 경우
        q = partition(arr, left, right) # 분할할 위치 - 피벗 기준 왼쪽은 작겉나 같은값, 오른쪽은 큰 값
        quick_sort(arr,left, q-1)
        quick_sort(arr, q+1, right)
    return arr 

def radix_sort(arr, bucket_size = 10): # 기수 정렬 
    # 버킷 리스트 생성 
    queues = []
    for _ in range(bucket_size):
        queues.append(deque()) # 덱 추가 
    
    n = len(arr)
    factor = 1 #자리수 기준 (1의자리, 10의 자리, 100의 자리 ..)
    max_val = max(arr) # 최대값 찾기
    while max_val // factor > 0: # 최대값의 모든 자리수에 대한 반복
        for i in range(n): 
            digit = (arr[i] // factor) % bucket_size # 현재 자리수의 값 추출
            queues[digit].append(arr[i]) # 배분
        
        idx = 0 # 배열 인덱스 초기화
        for b in range(bucket_size): 
            while queues[b]: # 버킷이 빌 때까지 수행함 
                arr[idx] = queues[b].popleft() # 원소 꺼내서 배열에 저장
                idx += 1
        
        factor *= bucket_size # 다음 자리수로 이동
    return arr 

def list_sorted(arr): # 리스트의 arr의 sort 메서드 사용
    return arr.sort(reverse=False)

def python_sorted(arr): # 내장 정렬 함수
    return sorted(arr)

def lambda_sorted(arr): # 람다 함수 사용한 정렬
    return sorted(arr, key=lambda x: x, reverse=False) # 복잡한 객체 (튜플, 딕셔너리)를 정렬


# ======================================================
# 2. 실행 시간 측정 함수
# ======================================================
def measure_time(sort_func, data):
    arr = data[:]  
    start = time.time()
    if sort_func == quick_sort:
        sort_func(arr, 0, len(arr) - 1)
    else:
        sort_func(arr)
    return time.time() - start

# ======================================================
# 3. 알고리즘 목록
# ======================================================
algorithms = {
    "선택정렬": selection_sort,
    "삽입정렬": insertion_sort,
    "퀵정렬": quick_sort,
    "기수정렬": radix_sort,
    "lambda": lambda_sorted,
    "sorted()": python_sorted,
    "sort()": list_sorted,    
}

# ======================================================
# 4. 입력 크기별 실행 시간 측정
# ======================================================
sizes = [100, 1000, 10000, 100000, 1000000, 10000000]  # 테스트할 입력 크기
# results = {name: [] for name in algorithms.keys()} # 결과 저장용 딕셔너리
results = {}
for name in algorithms.keys():
    results[name] = []
repeat = 3  # 평균 반복 횟수

for n in sizes:
    print(f"\n데이터 크기 n={n}")
    data = [random.randint(1, 99999) for _ in range(n)] # 무작위 데이터 생성
    for name, func in algorithms.items(): # 각 알고리즘에 대해
        # 느린 정렬은 대규모 입력 생략
        if name in ["삽입정렬", "선택정렬"] and n > 1000: # 1천 초과 시 생략
            results[name].append(None) # 결과에 None 추가
            print(f"  {name:}: (생략)") # 출력
            continue # 생략
        times = [measure_time(func, data) for _ in range(repeat)] # 실행 시간 측정
        avg_time = sum(times) / len(times) # 평균 시간 계산
        results[name].append(avg_time) # 결과 저장
        print(f"  {name:}: {avg_time:.6f}초 (평균 {repeat}회)") # 출력

# ======================================================
# 5. 선 그래프 (로그 스케일)
# ======================================================
plt.rcParams['font.family'] = 'Malgun Gothic' # 한글 폰트 설정 (Windows)
plt.figure(figsize=(10, 6)) # 그래프 크기 설정
for name, times in results.items(): # 각 알고리즘에 대해
    valid_sizes = [s for s, t in zip(sizes, times) if t is not None] # None이 아닌 크기만 선택
    valid_times = [t for t in times if t is not None] # None이 아닌 시간만 선택
    plt.plot(valid_sizes, valid_times, marker='o', label=name) # 선 그래프 그리기

plt.title("정렬 알고리즘별 실행 시간 비교 (입력 1백~1천만)", fontsize=14)
plt.xlabel("입력 크기 (n)")
plt.ylabel("평균 실행 시간 (초, log scale)")
plt.yscale("log") # 
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()