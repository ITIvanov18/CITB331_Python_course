import sys

# '#' - стена,
# ' ' - неизследван път,
# 'g' - цел
maze = [
    list("############"),
    list("#          #"),
    list("# ##########"),
    list("# #      #g#"),
    list("# ## ##### #"),
    list("#          #"),
    list("############")
]

# горе, дясно, долу, ляво
posoki = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def printMaze():
    for red in maze:
        print("".join(red))
    print()


def inBounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def solveMaze(start_r, start_c):
    rows, cols = len(maze), len(maze[0])

    if not inBounds(start_r, start_c, rows, cols):
        print("Грешка: Началната позиция е извън лабиринта!")
        return False
    if maze[start_r][start_c] == '#':
        print("Грешка: Началната позиция е в стена!")
        return False
    if maze[start_r][start_c] == 'g':
        print("Вече сте на целта!")
        printMaze()
        return True

    stack = [(start_r, start_c)]
    visited = set()
    parent = {}
    goal = None

    # DFS обход
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue

        # Граници и стени
        if not inBounds(r, c, rows, cols) or maze[r][c] == '#':
            continue

        visited.add((r, c))
        if maze[r][c] == 'g':
            goal = (r, c)
            break

        # Съседи за обхождане
        for dr, dc in posoki:
            new_row = r + dr
            new_col = c + dc

            # 1) Прескачаме вече обходените клетки
            if (new_row, new_col) in visited:
                continue

            # 2) Прескачаме, ако сме извън лабиринта
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            # 3) Прескачаме, ако е стена
            if maze[new_row][new_col] == '#':
                continue

            # Ако стигнем дотук, ходът е валиден:
            parent[(new_row, new_col)] = (r, c)
            stack.append((new_row, new_col))

    if goal is None:
        print("Няма път до целта.")
        return False

    # Реконструиране на пътя
    path = set()
    current = goal
    while current != (start_r, start_c):
        path.add(current)
        current = parent[current]
    path.add((start_r, start_c))

    # Маркиране
    for row, col in visited:
        if maze[row][col] == '#' or maze[row][col] == 'g':
            continue
        if (row, col) in path:
            maze[row][col] = '.'
        else:
            maze[row][col] = 'x'

    printMaze()
    print(f"Целта е намерена на позиция {goal}!")
    return True


if len(sys.argv) != 3:
    print("Грешка: Трябва да подадете точно 2 координати (ред и колона)!")
    sys.exit(1)

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("Грешка: Координатите трябва да са цели числа!")
    sys.exit(1)

start_r = int(sys.argv[1])
start_c = int(sys.argv[2])

solveMaze(start_r, start_c)
