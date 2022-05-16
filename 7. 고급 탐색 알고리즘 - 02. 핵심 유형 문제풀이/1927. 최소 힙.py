import heapq

n = int(input())
heap = []
result = []
for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            heapq.heappush(heap, data)

for data in result:
    print(data)