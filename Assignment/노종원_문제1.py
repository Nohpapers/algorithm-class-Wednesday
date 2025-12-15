def climb_stairs(n):
    mem = [0] * (n+1) # 인덱스 오류 방지 
    mem[0] = 1 # 계단 0개 1가지
    mem[1] = 1 # 계단 1개 1가지 

    for i in range(2, n+1):
        mem[i] = mem[i-1] + mem[i-2] # 점화식 적용

    return mem[n] # 최종 결과 반환

# 사용자 입력 처리 
steper = input("계단의 개수를 입력하시오: ")

if steper.isdigit():
    n = int(steper)
    
    if n > 0:
        result = climb_stairs(n)
        print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")
    else:
        print("1 이상의 자연수를 입력하세요.")
else:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")