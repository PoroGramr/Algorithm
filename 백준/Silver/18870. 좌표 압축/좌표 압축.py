import sys

# 입력 받기
n = int(sys.stdin.readline().strip())
coords = list(map(int, sys.stdin.readline().split()))

# 좌표 압축을 위한 정렬 및 인덱스 매핑
sorted_unique = sorted(set(coords))  # 중복 제거 후 정렬
index_map = {num: i for i, num in enumerate(sorted_unique)}  # 압축된 좌표 매핑

# 결과 출력
print(' '.join(str(index_map[num]) for num in coords))
