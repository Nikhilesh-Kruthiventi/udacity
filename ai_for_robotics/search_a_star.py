# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid2 = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
heuristic2 = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
             
grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0,]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]             

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    import heapq
    
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    count = 0;
    q = []
    visited = []
    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[x][y]
    node = (f, g, x, y)
    heapq.heappush(q, node)
    visited.append((x, y))
    
    found = False
    while q:
        node = heapq.heappop(q)
        g = node[1]
        x = node[2] 
        y = node[3]
        expand[x][y] = count
        count += 1
        if x == goal[0] and y == goal[1]:
            found = True
            break
        
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 > -1 and x2 < len(grid) and y2 > -1 and y2 < len(grid[0]) and (x2, y2) not in visited and grid[x2][y2] == 0:
                g2 = cost + g
                f2 = g2 + heuristic[x2][y2]
                node = (f2, g2, x2, y2)
                heapq.heappush(q, node)
                visited.append((x2, y2))
                
    if found:            
        return expand
    else:
        return 'fail'
    
expand = search(grid,init,goal,cost,heuristic)
if expand == 'fail':
    print 'fail'
else:    
    for i in range(len(expand)):
        print expand[i]

