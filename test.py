from collections import defaultdict

store_size_list = defaultdict(list)

B, Q = map(int, input().split(","))

# 브랜드 사이즈 정보 입력
for _ in range(B):
    b_name, s_num = input().split(",")
    s_num = int(s_num)

    for _ in range(s_num):
        size_name, H_min, H_max, C_min, C_max, W_min, W_max = input().split(",")
        store_size_list[b_name].append((
            size_name,
            int(H_min), int(H_max),
            int(C_min), int(C_max),
            int(W_min), int(W_max)
        ))

# 고객 질의 처리
for _ in range(Q):
    q_b, qH, qC, qW = input().split(",")
    qH, qC, qW = int(qH), int(qC), int(qW)

    # 1) 브랜드 없음
    if q_b not in store_size_list:
        print(f"{q_b},UNKNOWN")
        continue

    sizes = store_size_list[q_b]

    # 2) 작은 사이즈부터 매칭 탐색
    picked = None
    for (name, h1, h2, c1, c2, w1, w2) in sizes:
        if h1 <= qH <= h2 and c1 <= qC <= c2 and w1 <= qW <= w2:
            picked = name
            break

    if picked is not None:
        print(f"{q_b},{picked}")
        continue

    # 3) UP / DOWN / MISMATCH 판단을 위한 전체 범위 계산
    min_h = min(h1 for (_, h1, _, _, _, _, _) in sizes)
    min_c = min(c1 for (_, _, _, c1, _, _, _) in sizes)
    min_w = min(w1 for (_, _, _, _, _, w1, _) in sizes)

    max_h = max(h2 for (_, _, h2, _, _, _, _) in sizes)
    max_c = max(c2 for (_, _, _, _, c2, _, _) in sizes)
    max_w = max(w2 for (_, _, _, _, _, _, w2) in sizes)

    if qH > max_h and qC > max_c and qW > max_w:
        print(f"{q_b},UP")
    elif qH < min_h and qC < min_c and qW < min_w:
        print(f"{q_b},DOWN")
    else:
        print(f"{q_b},MISHMATCH")
