"""通过栈求结构树中最短路径"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from pythonds.basic.stack import Stack
import numpy as np
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        """
        考虑没有子树，有左右子树，只有左子树，只有右子树的情况
        """
        if not (root.left or root.right):
            return 1
        st = Stack()
        rst = Stack()
        min_depth=np.inf
        depth=0
        while root or not st.isEmpty():
            while root:
                st.push(root.right)   #可能没有右子树
                depth+=1
                rst.push(depth)
                root = root.left
            min_depth = min(min_depth,depth)
            depth = rst.pop()
            root = st.pop()
            while not root:
                if st.isEmpty():
                    return min_depth
                else:
                    depth = rst.pop()
                    root = st.pop()
        return min_depth
trees = TreeNode(10)
trees.left = TreeNode(3)
#trees.right = TreeNode(9)
trees.left.left = TreeNode(30)
trees.left.left.left = TreeNode(30)
#trees.left.left.right = TreeNode(13)
trees.left.left.left.right = TreeNode(139)
trees.left.left.left.left = TreeNode(13)
#trees.right = TreeNode(5)
t = Solution()

print(t.minDepth(trees))