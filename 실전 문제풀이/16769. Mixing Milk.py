C, M = list(), list()

for i in range(3):
    a, b = map(int, input().split())
    C.append(a)
    M.append(b)
print(M)
for i in range(100):
    idx = i % 3
    next = (idx + 1) % 3

    M[idx], M[next] = max(M[idx] - (C[next] - M[next]), 0), min(C[next], M[next] + M[idx])

for i in M:
    print(i)
