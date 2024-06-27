nv, ne = list(map(int, input().split()))
edges = []
for i in range(ne):
    edge = list(map(int, input().split()))
    edges.append(edge)
adj_list = {v:[] for v in range(nv)}
for v1, v2 in edges:
    adj_list[v1].append(v2)
start = int(input())
s = [start]
bfs = []
while(len(s)>0):
    ele = s.pop(0)
    if ele not in bfs:
        bfs.append(ele)
    for j in adj_list[ele]:
        if j not in bfs:
            s.append(j)
print(*bfs)