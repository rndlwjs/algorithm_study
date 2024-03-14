#개념: 여러 종류 드라마를 드라마 별로 볼것인가, 동시에 한편씩 볼 것인가
#dfs: 재귀 함수
#bfs: 큐 사용, 시간 복잡도적으로 효과적일때가 많음
#종류
  #최단경로 (거리, 시간)
  #네트워크
  #조합

###백준 바이러스 (2606) 인프런 강의 참고
import sys
sys.setrecursionlimit(10**6)
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

###백준 유기농 배추 (1212) 인프런 강의 참고
import sys
sys.setrecursionlimit(10**6)

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]

def dfs(y, x):
    global visited, map_
    visited[y][x] = True
    
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if map_[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)

#입력 초기화
input = sys.stdin.readline
T = int(input())
MAX = 50 + 10

while T > 0:
    T -= 1
    M, N, K = map(int, input().split())
    #map에 연결 정보 채우기
    map_ = [[False] * (MAX) for _ in range(MAX)]
    visited = [[False] * (MAX) for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        map_[y+1][x+1] = True #python order of two lists

    answer = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if map_[i][j] and not visited[i][j]:
                dfs(i, j)
                answer +=1
    #결과 출력 (테스트 케이스 여러 종류이기 때문에 반복문 안에서 수행)
    print(answer)
