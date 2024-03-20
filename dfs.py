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

###백준 유기농 배추 (1012) 인프런 강의 참고
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

###백준 침투 (13565) <바이러스> 코드 참고

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [[0] * (N+1)]
visited = [[0] * (N+1) for _ in range(M+1)]

for i in range(M):
    temp = list(map(int, input().rstrip()))
    temp.insert(0, 0)
    graph.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global graph, visited

    visited[x][y] = 1
    print(x, y)
    for i in range(4):
        newy = y + dy[i]
        newx = x + dx[i]
        if N >= newy > 0 and M >= newx > 0:
            if not graph[newx][newy] and not visited[newx][newy]:
                dfs(newx, newy)

for i in range(1, N+1):
    if not graph[1][i] and not visited[1][i]:
        dfs(1, i)

if 1 in visited[-1]:
    print("YES")
else:
    print("NO")

###백준 섬의개수 (4963)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

def dfs(x, y):
    global visited, map_, count, M, N
    visited[x][y] = 1
    #print("\t", x, y)
    for i in range(8):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < N and 0 <= newy < M:
            #print("i:",i," ", newx, newy)
            if map_[newx][newy] and not visited[newx][newy]:
                dfs(newx, newy)
    

while True:
    M, N = map(int, input().split())
    if M ==0 and N ==0: break
    visited = [[0] * (M) for _ in range(N)]
    map_ = []
    count = 0
    for _ in range(N):
        list_ = list(map(int, input().split()))
        map_.append(list_)
    
    for i in range(N): #M,N (5,4)로 입력 받지만, 행렬로 따지면 4X5이다. 
        for j in range(M):
            if map_[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)
