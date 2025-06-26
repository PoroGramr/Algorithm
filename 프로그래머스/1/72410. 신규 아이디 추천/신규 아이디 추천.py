def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    allowed = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
    filtered = [ch for ch in new_id if ch in allowed]
    new_id = ''.join(filtered)

    # 3단계
    collapsed = []
    prev_dot = False
    for ch in new_id:
        if ch == '.':
            if not prev_dot:
                collapsed.append(ch)
            prev_dot = True
        else:
            collapsed.append(ch)
            prev_dot = False
    new_id = ''.join(collapsed)

    # 4단계
    while new_id.startswith('.'):
        new_id = new_id[1:]
    while new_id.endswith('.'):
        new_id = new_id[:-1]

    # 5단계
    if new_id == '':
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]

    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
