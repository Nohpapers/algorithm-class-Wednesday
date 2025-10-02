import time

def factorial_iter(n):
    # 반복문 기반 n!
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    #  재귀적으로 문제 해결 n! -> 재귀함수 정의

    # 1. base case (재귀호출 종료 조건)
    if n == 1 or n ==0 :
        return 1
    
    # 2. 재귀 분할 호출
    return n * factorial_rec(n-1)

def run_with_time(func, n ):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    result_time = end_time - start_time
    return result_time


if __name__ == "__main__":
    print("=============== Factorial Tester ===============\n")
    print("1) 반복문으로 n! 계산\n")
    print("2) 재귀로 n! 계산\n")
    print("3) 두 방식 모두 계산 후 결과/시간비교\n")
    print("4) 준비된 테스트 데이터 일괄 실행\n")
    print("q) 종료\n")
    print("=================================================\n")
    k = int(input("선택: ").strip())
    if(k == 1):
        n = int(input("n 값(정수, 0이상)을 입력하세요: ").strip())
        if(n < 0):
            raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
        print(f"[반복]: {n}! = {factorial_iter(n)}")
    elif(k ==2):
        n = int(input("n 값(정수, 0이상)을 입력하세요: ").strip())
        if(n < 0):
            raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
        print(f"[재귀]: {n}! = {factorial_rec(n)}")
    elif(k ==3):
        n = int(input("n 값(정수, 0이상)을 입력하세요: ").strip())
        if(n < 0):
            raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
        iter_time = run_with_time(factorial_iter, n)
        rec_time = run_with_time(factorial_rec, n)
        print(f"[반복]: {n}! = {factorial_iter(n)}")
        print(f"[재귀]: {n}! = {factorial_rec(n)}")
        if(factorial_iter(n) == factorial_rec(n)):
            print("결과 일치 여부: 일치.\n")
        try:    
            print(f"[반복] 시간: {iter_time:.7f}s  |  [재귀] 시간: {rec_time:.7f}s")
        except RecursionError:  
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")
    elif(k ==4):
        test_data = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]
        print("[테스트 데이터 실행]\n")
        for n in test_data:
            iter_time = run_with_time(factorial_iter, n)
            rec_time = run_with_time(factorial_rec, n)
            Same = (factorial_iter(n) == factorial_rec(n))
            print(f"n = {n} | same = {Same} | iter_time = {iter_time:.7f}s,  rec_time = {rec_time:.7f}s")
            print(f" {n}! = {factorial_iter(n)}")
    elif(k == 'q'):
        print("종료합니다.")