DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def search_number(engine, y, x, visited):
    if not(y >= 0 and y < len(engine) and x >= 0 and x < len(engine[0])):
        return ""

    if not engine[y][x].isnumeric():
        return ""
    
    if (y, x) in visited:
        return ""
    
    visited.add((y, x))
    
    return search_number(engine, y, x -1, visited) + engine[y][x] + search_number(engine, y, x +1, visited)


def visit_adjacents(engine, visited, i, j):
    founded = []

    for dy, dx in DIRECTIONS:
        ny, nx = i + dy, j + dx
        if ny >= 0 and ny < len(engine) and nx >= 0 and nx < len(engine[0]):
            if (ny, nx) not in visited and engine[ny][nx].isnumeric():
                founded.append(int(search_number(engine, ny, nx, visited)))

    return 0 if len(founded) != 2 else founded[0] * founded[1]

def find_engine_sum(file):
    engine = None

    with open(file, mode="r") as f:
        engine = f.read().split("\n")
    
    res = 0
    visited = set()
    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if engine[i][j] == "*":
                res += visit_adjacents(engine, visited, i, j)

    return res