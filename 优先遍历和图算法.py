"""
图的遍历：深度优先遍历，广度优先遍历，
机器人问题
迷宫问题（只有一条出路）
"""
# 图的深度优先遍历
# 1.利用栈实现
# 2.从源节点开始把节点按照深度放入栈，然后弹出
# 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
# 4.直到栈变空
def dfs(node):
    if node is None:
        return
    nodeSet = set()
    stack = []
    print(node.value)
    nodeSet.add(node)
    stack.append(node)
    while len(stack) > 0:
        cur = stack.pop()               # 弹出最近入栈的节点
        for next in cur.nexts:         # 遍历该节点的邻接节点
            if next not in nodeSet:    # 如果邻接节点不重复 
                stack.append(next)      # 把邻接节点压入
                nodeSet.add(next)           # 登记节点
                print(next.value)       # 打印节点值

"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？                
链接：https://www.nowcoder.com/questionTerminal/6e5207314b5241fb83f2329e89fdecc8
"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        self.row, self.col = rows, cols
        self.dict = set()
        self.search(threshold, 0, 0)
        return len(self.dict)
 
    def judge(self, threshold, i, j):
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold
 
    def search(self, threshold, i, j):
        if not self.judge(threshold, i, j) or (i, j) in self.dict:
            return
        self.dict.add((i, j))
        if i != self.row - 1:
            self.search(threshold, i + 1, j)
        if j != self.col - 1:
            self.search(threshold, i, j + 1)

"""采用递推算法解决上述机器人问题"""            
# 图的深度优先遍历
# 1.利用栈实现
# 2.从源节点开始把节点按照深度放入栈，然后弹出
# 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
# 4.直到栈变空
class myself:
    def nextNode(self,node,x,y):
        rst = []
        if node[0]<x-1:
            rst.append((node[0]+1,node[1]))
        if node[1]<y-1:
            rst.append((node[0],node[1]+1))
        return rst
    def judge(self,threshold, i, j):
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold
    def dfs(self,threshold,x,y,node=(0,0)):
        if node is None:
            return
        nodeSet = set()
        stack = []
        nodeSet.add(node)
        stack.append(node)
        while len(stack) > 0:
            cur = stack.pop()               # 弹出最近入栈的节点
            for next in self.nextNode(cur,x,y):         # 遍历该节点的邻接节点
                if self.judge(threshold,next[0],next[1]) and next not in nodeSet:    # 如果邻接节点不重复
                    stack.append(cur)       # 把节点压入
                    stack.append(next)      # 把邻接节点压入
                    nodeSet.add(next)           # 登记节点
                    break                   # 退出，保持深度优先
        print(len(nodeSet))
        
"""广度优先搜索"""
# 图的广度优先遍历
# 1.利用队列实现
# 2.从源节点开始依次按照宽度进队列，然后弹出
# 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
# 4.直到队列变空
from queue import Queue
def bfs(node):
    if node is None:
        return
    queue = Queue()
    nodeSet = set()
    queue.put(node)
    nodeSet.add(node)
    while not queue.empty():
        cur = queue.get()               # 弹出元素
        print(cur.value)                # 打印元素值
        for next in cur.nexts:          # 遍历元素的邻接节点
            if next not in nodeSet:     # 若邻接节点没有入过队，加入队列并登记
                nodeSet.add(next)
                queue.put(next)        
                
"""
迷宫路径的问题
https://www.nowcoder.com/search?query=%E8%BF%B7%E5%AE%AB&type=question 
"""
from collections import deque
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y:(x+1,y),#下
    lambda x,y:(x,y-1),#左
    lambda x,y:(x,y+1),#右
    lambda x,y:(x-1,y),#上

]

def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2]) # 把起点放进去
    realpath.reverse()
    print(len(realpath))
    for i in realpath:
        print(i)

def maze_path_queue(x1,y1,x2,y2):
    maze[x1][y1]=2
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while len(queue)>0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dir in dirs:                         #产生子节点的过程
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]]==0:
                # 后续节点进队，记录哪个节点带他来的
                node = (nextNode[0],nextNode[1],len(path)-1)
                queue.append(node)
                maze[nextNode[0]][nextNode[1]] = 2  # 标记为已经走过
    else:
        print('没有路')
        return False
maze_path_queue(1,1,8,8)

##############################沿用了上面的思路##########################################
"""
https://www.nowcoder.com/questionTerminal/571cfbe764824f03b5c0bfd2eb0a8ddf
处理最短路径问题，此处采用了堆的原理
每个节点用四个坐标：能量消耗，x坐标，y坐标，父节点在path列表中的位置
"""
import heapq
n,m,p = map(int,input().split())                 
maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))    ##当有多行数据输入时，注意此处的list

maps[0][0]=2
beginx,beginy,endx,endy = 0,0,0,m-1
action = [
        lambda t,x,y,index:(t,x+1,y,index),
        lambda t,x,y,index:(t+1,x,y+1,index),
        lambda t,x,y,index:(t+1,x,y-1,index),
        lambda t,x,y,index:(t+3,x-1,y,index)
        ]

def searchPath(beginx,beginy,endx,endy):
    path = []
    NodeList = [(0,beginx,beginy,0)]
    while NodeList:
        curNode = heapq.heappop(NodeList)
        path.append(curNode)
        for lams in action:
            temp = lams(curNode[0],curNode[1],curNode[2],curNode[3])
            if temp[1]>=0 and temp[2]>=0 and temp[1]<n and temp[2]<m and temp[0]<=p and maps[temp[1]][temp[2]]==1:
                maps[temp[1]][temp[2]]=2
                temp = (temp[0],temp[1],temp[2],len(path)-1)
                if temp[1]==endx and temp[2] == endy:
                    path.append(temp)
                    return path
                heapq.heappush(NodeList,temp)
    path = []
    return path

       
def path_shift(path):
    if not path:
        print("Can not escape!")
        return
    rst,index = [[path[-1][1],path[-1][2]]],path[-1][3]
    while True:
        rst.append([path[index][1],path[index][2]])
        index = path[index][3]
        if index==0:
            rst.append([path[index][1],path[index][2]])
            break
    rst.reverse()
    print(','.join(['[{},{}]'.format(x[0], x[1]) for x in rst]))
    return
        
path = searchPath(beginx,beginy,endx,endy)
path_shift(path)

