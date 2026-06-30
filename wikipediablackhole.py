from collections import defaultdict, deque

def bfs(graph, start):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        article, clicks = queue.popleft()

        for next_article in graph[article]:
            if next_article == start:
                return clicks + 1

            if next_article not in visited:
                visited.add(next_article)
                queue.append((next_article, clicks + 1))

    return 'NO BLACK HOLE'


n = int(input())
start = input()
graph = defaultdict(list)
for _ in range(n):
    source, destination = input().split()
    graph[source].append(destination)
print(bfs(graph, start))