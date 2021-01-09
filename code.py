import random
import turtle


n = 40
x = -300
y = 200
mycolor = ("red", "green", "blue", "pink", "orange")

class Solution:
    def numIslands(self, grid):
        if grid is None:
            return None
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = 0
        k = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
                    k += 1
                    self.dfs(grid, i, j, k)
        return res


    def dfs(self, grid, i, j, k):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == 1:
            grid[i][j] = k
            self.dfs(grid, i + 1, j, k)
            self.dfs(grid, i - 1, j, k)
            self.dfs(grid, i, j - 1, k)
            self.dfs(grid, i, j + 1, k)


def draw_square(length: float, fill_color: str):
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    for index in range(4):
        turtle.forward(length)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def draw(grid, r, c):
    for i in range(r):
        for j in range(c):
            turtle.goto(x + j * n, y - i * n)
            if grid[i][j] == 0:
                draw_square(n, "white")
            elif grid[i][j] % 5 == 0:
                draw_square(n, mycolor[0])
            elif grid[i][j] % 5 == 1:
                draw_square(n, mycolor[1])
            elif grid[i][j] % 5 == 2:
                draw_square(n, mycolor[2])
            elif grid[i][j] % 5 == 3:
                draw_square(n, mycolor[3])
            else:
                draw_square(n, mycolor[4])


def show(grid, r, c):
    draw(grid, r, c)
    turtle.done()

if __name__ == '__main__':
    r = 5
    c = 5
    grid = [[random.randint(0, 1) for _ in range(r)] for _ in range(c)]
    s = Solution()
    result = s.numIslands(grid)
    turtle.speed(300)
    turtle.pensize(2)
    turtle.setup(width=0.5, height=0.75, startx=30, starty=100)
    turtle.penup()
    print(result)
    show(grid, r, c)
