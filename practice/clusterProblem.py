import random
from collections import deque

dr, dc = [1,-1,0,0], [0,0,1,-1]

def simulation(a, b): # 서버 감염 시뮬레이션 함수
    A, B = a, b

    def calculate_percentile(server_map, total): # 정상 서버의 비율을 구하는 함수
        return round(sum([server.count('O') for server in server_map])*100/total)

    def change_map(server_map, server_checker): # 서버 맵을 변경하는 함수
        server_map = [server[:] for server in server_map]
        for server in server_checker.keys():
            if not server_checker[server]:
                server_map[server[0]][server[1]] = 'X'
        return server_map

    def infesting(server_checker, infected_servers, server_map): # 서버 감염 및 클러스터 감염
        today_server_map = [server[:] for server in server_map]
        
        for infected_server in infected_servers:
            server_checker[infected_server] = False
            today_server_map[infected_server[0]][infected_server[1]] = '@'

        normal_servers = [key for key in server_checker.keys() if server_checker[key]]
        clusters = []
        visited_servers = []

        for server in normal_servers:
            if server in visited_servers:
                continue
            else:
                cluster = [server]
                queue = deque([server])
                visited_servers.append(server)
                while queue:
                    cluster_server = queue.popleft()
                    row, col = cluster_server
                    for k in range(4):
                        n_row, n_col = row + dr[k], col + dc[k]
                        next_server = (n_row, n_col)
                        if (0 <= n_row < A and 0 <= n_col < A) and server_checker[next_server] and (next_server not in visited_servers):
                            visited_servers.append(next_server)
                            cluster.append(next_server)
                            queue.append(next_server)
                clusters.append(cluster)
        
        sorted_clusters = sorted(clusters, key=lambda x : len(x)) # 클러스터를 크기 순으로 정렬
        sorted_clusters.pop() # 제일 규모가 큰 클러스터 제거

        for cluster in sorted_clusters: # 나머지 클러스터들에 대해
            for server in cluster: # 클러스터 내에 있는 서버를 순회하여
                server_checker[server] = False # 모두 감염시킨다.
        return server_checker, today_server_map

    total, servers = pow(A,2), [(i,j) for i in range(A) for j in range(A)]

    total = pow(A,2)
    server_map = [['O' for _ in range(A)] for _ in range(A)]
    server_checker = {server:True for server in servers}

    percentile = calculate_percentile(server_map, total)
    day = 0

    while percentile > 40: # 정상적인 서버의 비율이 40%를 넘어선다면 = 감염된 서버의 비율이 60% 이하라면
        day += 1
        normal_servers = [key for key in server_checker.keys() if server_checker[key]] # 정상적인 서버 리스트
        infected_servers = random.sample(normal_servers, B) # 정상적인 서버 리스트 중에서 B개 감염
        server_checker, today_server_map = infesting(server_checker, infected_servers, server_map) # 서버를 감염시키고
        server_map = change_map(server_map, server_checker) # 서버 맵을 변경
        percentile = calculate_percentile(server_map, total) # 정상적인 서버의 비율을 구한다.
        # print(f'{day}일 째, 정상 서버 비율 : {percentile}%')

        # for server in today_server_map:
        #     print(server)
        # print('')

    print(f'{day}일 째, 정상 서버 비율 : {percentile}%')

    for server in today_server_map:
        print(server)
    
    return day

def recur_simulation(case, n): # 시뮬레이션 n회 반복 함수
    a, b = case
    result = []
    for _ in range(n):
        result.append(simulation(a, b))
    avg = round(sum(result)/n,1)
    print(f'(A:{a}, B:{b})로 {n}회 반복시 평균 일수 : {avg}일')
    return avg

simulation(5,1)
simulation(10,5)
simulation(100,100)
simulation(200,400)

# recur_simulation((5,1),10)
# recur_simulation((10,5),10)
# recur_simulation((100,100),10)
# recur_simulation((200,400),10)