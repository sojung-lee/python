n, m = map(int, input().split())
array = []
graph = [[0] * 100 for _ in range(100)]
for _ in range(n):
    array.append(list(map(int, input().split())))

for j in array:
    for k in range(j[0], j[2] + 1):
        for z in range(j[1], j[3] + 1):
            graph[k-1][z-1] += 1

result = 0
for x in graph:
    for j in x:
        if j > m:
            result += 1
print(result)