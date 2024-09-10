n = int(input())

for i in range(n):
  data = list(input())
  answer = []
  # 문자열을 순회하며 answer에 없다면 삽입, 있다면 삭제
  # 짝이 없는 문자만 남게됨
  for k in range(len(data)):
    if not data[k] in answer:
      answer.append(data[k])
    else:
      answer.remove(data[k])
  # 정렬
  answer.sort()
  
  if len(answer) == 0:
    print(f"#{i+1} Good")
  else:
    print(f"#{i+1} ", end="")
    for a in answer:
      print(a, end="")
    print()