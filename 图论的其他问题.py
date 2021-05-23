"""
图论中其他问题：
1. 判断是否有闭环的问题。如题1
"""

##############1. 课程表的问题：课程有依赖关系###################
"""https://leetcode.com/problems/course-schedule/"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(start, visited, graph):
            visited[start] = 1
            for nbr in graph[start]:
                if visited[nbr] == 1:    #如果存在环路，则绕一圈回到原点时，出现这种情况
                    return False
                if dfs(nbr, visited, graph) == False:
                    return False
            visited[start] = 2           #如果start这个点以及将它作为根节点的所有节点都没有被访问过，则将这个start点以及以他为根节点的所有点设为2，表示这条线路没有环路
            return True

        graph = [[] for _ in range(0, numCourses)]
        for pre in prerequisites:
            start, end = pre
            graph[start].append(end)      #找出所有顶点的有向边邻点
            
        visited = [0 for _ in range(0, numCourses)]
        
        for pre in prerequisites:
            start, end = pre
            if visited[start] == 0:       #这个顶点还没定为2，也就是说还没判断这条路线是否有环
                if dfs(start, visited, graph) == False:
                    return False
        return True
