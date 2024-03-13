#개념: 여러 종류 드라마를 드라마 별로 볼것인가, 동시에 한편씩 볼 것인가
#dfs: 재귀 함수
#bfs: 큐 사용, 시간 복잡도적으로 효과적일때가 많음
#종류
  #최단경로 (거리, 시간)
  #네트워크
  #조합

###백준 바이러스 (2606) 인프런 강의 참고
import sys

def dfs(idx):
    global graph, visited, cnt    
    visited[idx] = True
    cnt += 1
    for i in range(n+1):
        if visited[i]==False and graph[idx][i]==True:
            dfs(i)
    return cnt
#입력, 초기화
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)  #방문한 위치

cnt = 0
#그래프 채우기
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
#결과 출력
print(dfs(1)-1)
