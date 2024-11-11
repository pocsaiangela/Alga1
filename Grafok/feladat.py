def count_rooms(n, m, building_map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    room_count = 0
    
    def is_valid(x, y):
        if 0 > x or x >= n:
            return False
        if 0 > y or y >= m:
            return False
        
        return building_map[x][y] == '.' and not visited[x][y]
    
    def DFS(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        while stack:
            curr_x, curr_y = stack.pop()
            for dx, dy in directions:
                new_x, new_y = curr_x + dx, curr_y + dy
                if is_valid(new_x, new_y):
                    visited[new_x][new_y] = True
                    stack.append((new_x, new_y))
    
    for i in range(n):
        for j in range(m):
            if building_map[i][j] == '.' and not visited[i][j]:
                DFS(i, j)
                room_count += 1
    
    return room_count
