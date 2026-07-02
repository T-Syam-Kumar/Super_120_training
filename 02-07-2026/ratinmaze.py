def ratInMaze( maze):
        n = len(maze)
        
        if maze[0][0] == 0:
            return []
        
        directions = [(1,0,'D'),(0,1,'R'),(-1,0,'U'),(0,-1,'L')]
        visited = [[False]*n for _ in range(n)]
        res = []
        
        def solve(i, j, path):
            if i == n-1 and j == n-1:
                res.append(path)
                return

            for dx, dy, d in directions:
                new_i, new_j = i + dx, j + dy
                if new_i < 0 or new_j < 0 or new_i == n or new_j == n:
                    continue
                
                if maze[new_i][new_j] != 1 or visited[new_i][new_j]:
                    continue
                
                visited[new_i][new_j] = True
                solve(new_i, new_j, path+d)
                visited[new_i][new_j] = False
                    
                    
        visited[0][0] = True
        solve(0, 0, '')
        return sorted(res)