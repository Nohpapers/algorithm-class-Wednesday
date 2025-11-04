# 하노이 탑 문제 : 재귀적으로 문제 해결

def tower_hanoi(n, start, tmp, target):
    if n == 1:
        print(f"원판{n} {start} -> {target}")
    else:
        tower_hanoi(n-1, start, target, tmp)
        print(f"원판{n} {start} -> {target}")
        tower_hanoi(n-1, tmp, start, target )



if __name__ == "__main__":
    n = int(input("원판의 개수를 입력해주세요: "))
    tower_hanoi(n,'A','B','C')

    total = ( 1 << n ) -1
    print(f"\n 총 이동 횟수: {total} (2^{n} - 1)")


    
