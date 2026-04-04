import math
import heapq


def manhattan(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def euclidean(pos, goal):
    return math.sqrt((pos[0] - goal[0])**2 + (pos[1] - goal[1])**2)


def a_star(grid, start, goal, heuristic):
    rows, cols = len(grid), len(grid[0])
    
    open_list = []
    heapq.heappush(open_list, (0, 0, start))  
    
    g_cost = {start: 0}   
    parent = {start: None}  
    closed_set = set()
    expanded = 0

    
    moves = [(0,1), (1,0), (0,-1), (-1,0)]

    while open_list:
        f, h, current = heapq.heappop(open_list)
        if current in closed_set:
            continue
        closed_set.add(current)
        expanded += 1

        
        if current == goal:
            path = []
            node = current
            while node:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, expanded

        r, c = current
        
        neighbors = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                neighbors.append((nr, nc))
        
        
        neighbors.sort()
        
        for neighbor in neighbors:
            new_g = g_cost[current] + 1
            h_value = heuristic(neighbor, goal)
            f_value = new_g + h_value
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                heapq.heappush(open_list, (f_value, h_value, neighbor))

    return None, expanded


def mark_path(grid, path):
    new_grid = [list(row) for row in grid]
    for r, c in path[1:-1]: 
        new_grid[r][c] = '*'
    return ["".join(row) for row in new_grid]

# 
def main():
    N, M = map(int, input("Enter rows and columns: ").split())
    print("Enter the grid rows (S=start, G=goal, .=walkable, #=obstacle):")
    grid = [input().strip() for _ in range(N)]
    
    start = goal = None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i,j)
            elif grid[i][j] == 'G':
                goal = (i,j)

    
    path_ma, exp_ma = a_star(grid, start, goal, manhattan)
    path_eu, exp_eu = a_star(grid, start, goal, euclidean)

    if path_ma:  
        print(f"\nShortest Path Length: {len(path_ma)}")
        print("Path:")
        print("->".join(f"({r},{c})" for r,c in path_ma))
        
        grid_marked = mark_path(grid, path_ma)
        print("\nGrid with Path:")
        for row in grid_marked:
            print(row)
        
        print(f"\nNodes Expanded: Manhattan Distance: {exp_ma}")
        print(f"Nodes Expanded: Euclidean Distance: {exp_eu}")
    else:
        print("No path found.")


if __name__ == "__main__":
    main()