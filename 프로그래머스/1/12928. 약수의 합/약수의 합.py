def solution(n):
    # 문제 이해 -> 입력받은 n 의 약수를 모두 더한다
    # - 입력 : n
    # - 출력 : n의 약수의 총합
    # - 약수 : n 을 나눴을 때 나머지가 0 이 아닌 수
    
    # 제한 사항 -> n은 3000 이하의 정수
    # - O(n) : 3K
    # - O(n^2) : 3K * 3K
    
    # 아이디어 
    # - answer 초기화
    answer = 0
    # - n만큼 반복
    for i in range (1, n+1):
    # - - n을 나눈 나머지가 0 이라면 answer에 더함
        if n % i == 0:
            answer += i
    return answer