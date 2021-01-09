# Algorithm_Homework
# maze.py 是迷宫构建和迷宫破解
# code.py 是岛屿问题
# 环境: python 3.6
# 依赖：copy turtle random 库
# 运行：  1. 打开命令行进入目录
#        2. 输入 python maze.py, 运行第一个程序
#        3. 输入 python code.py, 运行第二个程序
# 
# 解释：maze.py
# 目的是先随机构建一个入口为（1，1），出口为（num_rows - 2, num_cols - 2）的迷宫，然后再进行破解，最后将路径可视化，
# 蓝色为路径，黑色为墙，白色为通路
# 生成迷宫 init() 运用的是深度优先（递归回溯）算法，算法思想：
#   初始cell入栈stack
#   当前cell置为初始cell
#   循环，终止条件：栈stack为空
#	    将当前cell的访问状态置为已访问
#	    如果，当前cell有相邻的未访问cell
#		    随机选择相邻的未访问cell中的一个cell
#		    当前cell与随机选择的cell之间的相邻的两个状态置为可通行
#		    随机选择的cell入栈stack
#		    当前cell置为随机选择的cell
#	    否则
#		    从stack中出栈一个cell作为当前cell
#   最后生成的迷宫0为通路， 1为墙壁
# 破解迷宫 maze_out() 运用的是递归回溯算法，算法思想：
#   由该点开始遍历4个方向
#   选择一个方向，判断是否能走
#   若能前进，标记为2
#       进入maze_out()再次循环
#       若未能走通，回溯恢复为0
#   若达到终点，加入路径集
# 解释：code.py
# 目的：岛屿问题，给定一个包含了一些 0 和 1的非空二维数组 grid , 一个岛屿是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。
# 假设二维矩阵的四个边缘都被水包围着。分出有多少岛屿。每次运行代码会随机生成一次地图，最后将分类出的岛屿进行可视化，一种颜色代表一
# 个岛屿，若数量超过5，则颜色会循环一次
# 解释class Solution
# numIslands算法思想
# 遍历每一个位置，若为土地，对其进行深度优先遍历，然后对土地进行标记，直至超出边界退出
# dfs算法思想
# 对该位置进行上下左右深度优先遍历，对土地进行标记，直至超出边界退出

