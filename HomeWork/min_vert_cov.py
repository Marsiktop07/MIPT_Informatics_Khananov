def bipartite(graph):
    n = len(graph.keys())
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = [start]
            colors[start] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    # Если сосед уже окрашен в тот же цвет, граф не двудольный
                    elif colors[v] == colors[u]:
                        return False, []

    set1 = [i for i in range(n) if colors[i] == 0]
    set2 = [i for i in range(n) if colors[i] == 1]

    return True, (set1, set2)


def min_vert_cov(graph):
    n = len(graph.keys())
    match = [-1] * n
    visited = [False] * n
    _, parts = bipartite(graph)
    L = parts[0]
    R = parts[1]
    def dfs(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or dfs(match[u]):
                    match[u] = v
                    return True
        return False
    def dfsn(v):
        visited[v] = True
        visitedans[v] = True
        for u in graph2[v]:
            if not visited[u]:
                visited[u] = True
                visitedans[u] = True
                dfsn(u)

    for v in L:
        visited = [False] * n
        dfs(v)
    graph2 = {}
    for i in graph.keys():
        graph2[i] = []
    for i in graph.keys():
        for j in graph[i]:
                if match[j] == i or match[i] == j:
                    if i in L:
                        graph2[j].append(i)
                    else:
                        graph2[i].append(j)
                else:
                    if i in L:
                        graph2[i].append(j)
                    else:
                        graph2[j].append(i)
    for i in graph2.keys():
        graph2[i] = sorted(list(set(graph2[i])))

    visitedans = [False] * n
    for i in graph.keys():
        if (i not in match and match[i] == -1) and i in L:
            visited = [False] * n
            dfsn(i)
    ans = []
    for i in range(len(visitedans)):
        if (i in L and visitedans[i] == False) or (i in R and visitedans[i] == True):
            ans.append(i)
    return ans






G = {}
# G[0] = [1,3,5]
# G[1] = [0,2,6]
# G[2] = [1]
# G[3] = [0,4]
# G[4] = [3,5,7]
# G[5] = [0,4]
# G[6] = [1]
# G[7] = [4]

G[0] = [1]
G[1] = [0, 2, 4]
G[2] = [1, 3]
G[3] = [2, 4]
G[4] = [1, 3]

print(min_vert_cov(G))
#алгоритм будет работать только для неориентрированных двудольных графов.
