import copy
import turtle
import random

rows = 5
cols = 5
# 行和列
num_rows = rows * 2 + 1
num_cols = cols * 2 + 1


# 初始化迷宫（0是路，1是墙）
def init():
    i, j = 0, 0

    status = [[[False for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    stack = [(i, j)]
    while stack:
        visited[i][j] = True
        choosable = []
        if j > 0 and not visited[i][j - 1]:
            choosable.append('L')
        if i > 0 and not visited[i - 1][j]:
            choosable.append('U')
        if j < cols - 1 and not visited[i][j + 1]:
            choosable.append('R')
        if i < rows - 1 and not visited[i + 1][j]:
            choosable.append('D')
        if choosable:
            direct = random.choice(choosable)
            if direct == 'L':
                status[i][j][0] = True
                j -= 1
                status[i][j][2] = True
            elif direct == 'U':
                status[i][j][1] = True
                i -= 1
                status[i][j][3] = True
            elif direct == 'R':
                status[i][j][2] = True
                j += 1
                status[i][j][0] = True
            elif direct == 'D':
                status[i][j][3] = True
                i += 1
                status[i][j][1] = True
            stack.append((i, j))
        else:
            i, j = stack.pop()

    maze = [[1 for _ in range(cols * 2 + 1)] for _ in range(rows * 2 + 1)]
    for r in range(rows):
        for c in range(cols):
            cell = status[r][c]
            maze[r * 2 + 1][c * 2 + 1] = 0
            if cell[0]:
                maze[r * 2 + 1][c * 2] = 0
            if cell[1]:
                maze[r * 2][c * 2 + 1] = 0
            if cell[2]:
                maze[r * 2 + 1][c * 2 + 2] = 0
            if cell[3]:
                maze[r * 2 + 2][c * 2 + 1] = 0
    return maze


# 画图时每行间隔，小格子边长
n = 40
x = -300
y = 200
# 迷宫入口
maze_entry = (1, 1)
# 迷宫出口
maze_exit = (num_rows - 2, num_cols - 2)
# 一个解路径
path = [maze_entry]
# 存储多个解
paths = []

# 移动的方向 上下, 左右
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 检测冲突
def conflict(now_x, now_y):
    # 如果当前坐标在maze范围内，且可通行 返回不冲突
    if 0 <= now_x < num_rows and 0 <= now_y < num_cols and maze[now_x][now_y] == 0:
        return False
    return True


def maze_out(now_x, now_y):
    global maze, path, paths, dirs, maze_entry, num_rows, num_cols
    if (now_x, now_y) == maze_exit:
        paths.append(path[:])
    else:
        # 遍历四个方向
        for d in dirs:
            new_x, new_y = now_x + d[0], now_y + d[1]
            path.append((new_x, new_y))
            if not conflict(new_x, new_y):
                # 通路标记为2
                maze[new_x][new_y] = 2
                # 回溯
                maze_out(new_x, new_y)
                # 未能走通，回溯恢复
                maze[new_x][new_y] = 0
            # 回溯 出栈
            path.pop()


# 迷宫解的可视化
def showsuc(path):
    global maze
    # 深拷贝
    maze_2 = copy.deepcopy(maze)
    for p in path:
        # 通路标记为2
        maze_2[p[0]][p[1]] = 2
    draw(maze_2)
    turtle.done()


# 画正方形
def draw_square(length: float, fill_color: str):
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    for index in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def draw(maze_0):
    for i in range(num_rows):
        for j in range(num_cols):
            turtle.goto(x + j * n, y - i * n)
            if maze_0[i][j] == 1:
                draw_square(n, "black")
            elif maze_0[i][j] == 0:
                draw_square(n, "white")
            else:
                draw_square(n - 10, "blue")


if __name__ == '__main__':
    maze = init()
    turtle.speed(300)
    turtle.pensize(2)
    turtle.setup(width=0.5, height=0.75, startx=30, starty=100)
    turtle.penup()
    (origin_x, origin_y) = maze_entry
    maze_out(origin_x, origin_y)
    if len(paths) != 0:
        showsuc(paths[-1])
