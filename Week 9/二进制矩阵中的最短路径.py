class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0] !=0: return -1
        dx = [0,0,1,1,-1,-1,1,-1]
        dy = [1,-1,1,-1,1,-1,0,0]
        q =[(0,0)]
        visited = set()
        visited.add((0,0))
        level = 1
        def isLegal(x,y):
            return x>=0 and x<n and y>=0 and y < n
        while q:
            # print(q)
            tmp = []
            for ele in q:
                if ele == (n-1,n-1):
                    return level
                i,j = ele
                for k in range(8):
                    x = i+ dx[k]
                    y = j+ dy[k]
                    if isLegal(x,y) and grid[x][y] == 0 and (x,y) not in visited:
                        tmp.append((x,y))
                        visited.add((x,y))
            q = tmp
            level += 1

                

        return -1