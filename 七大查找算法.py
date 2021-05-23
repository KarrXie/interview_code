"""
查找算法
七大查找算法（Python） - ls秦 - 博客园
https://www.cnblogs.com/lsqin/p/9342929.html
"""
#二分查找
#插值查找
#斐波那契查找
##二叉树查找算法
# 二叉树查找 Python实现

#二分查找 |||插值查找
def binary_search(lst,key):
    low,high=0,len(lst)-1
    while low<=high:   ##注意此处的“=”
        mid = (low+high)//2  ##如果是插值查找，此处为mid = low+int((high-low)*(key-lst[low])/(lst[high]-lst[low]))
        if lst[mid]<key:
            low=mid+1
        elif lst[mid]>key:
            high=mid-1
        else:
            return True
    return False  

#############二叉查找树################
"""二叉查找树（BinarySearch Tree）或者是一棵空树，或者是具有下列性质的二叉树：
　　    1）若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
　　    2）若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
　　    3）任意节点的左、右子树也分别为二叉查找树。"""
##############################
class BSTNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinarySortTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return not self.root
    def insert(self,val):
        if self.isEmpty():
            self.root=BSTNode(val)
            return
        temp = self.root
        while temp:
            if val < temp.val:
                if temp.left is None:
                    temp.left = BSTNode(val)
                    return
                temp = temp.left
            elif val > temp.val:
                if temp.right is None:
                    temp.right = BSTNode(val)
                    return
                temp = temp.right
            else:
                return  ##########此处是将重复了的元素取消了
    ###最难理解的部分。删除一个节点，立马会想到与父节点有关，可是我们采用的节点类中没有父节点的指针
    ###思路：（1）对待删节点，想到十字交叉，即它是否为父节点的左节点还是右节点？它是否存在左子树或者右子树（2）该节点是否为根节点
    def delete(self,key):   
        p,q = None,self.root
        if not q:
            print('tree is empty')
            return
        while q and q.val!=key:
            if key < q.val:
                p = q
                q = q.left
            if key > q.val:
                p = q
                q = q.right
            if not q:
                return
        if not q.left:
            if not p:
                self.root = q.right
            elif p.left == q:
                p.left = q.right
            else:
                p.right = q.right
            return
        t = q.left
        while t.right:
            t = t.right
        t.right = q.right
        if p is None:
            self.root = q.left
        elif p.left == q:
            p.left = q.left
        else:
            p.right = q.left
            
    def search(self,val):
        t = self.root
        while t:
            if val < t.val:
                t = t.left
            elif val > t.val:
                t = t.right
            else:
                return True
        return False
    ###在类中采用 __iter__生成迭代器，也就是其对象可以作为迭代器使用
    ###中序遍历算法
    def __iter__(self):
        stack = []
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.val
            node = node.right
    ###先序遍历算法  迭代  
    def __iter__(self):
        stack = []
        node = self.root
        while node or stack:
            while node:
                yield node.val
                stack.append(node)
                node = node.left
            node = stack.pop().right
        
    ###后序遍历算法 迭代
    def __iter__(self):
        stack = [self.root]
        stack2 = []
        while len(stack)>0:
            node = stack.pop()
            stack2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while stack2:
            yield stack2.pop().val
            
            
if __name__ == '__main__':
    lis = [62,58,88,48,73,99,35,51,93,29,51,37,49,56,36,50]
    bs_tree = BinarySortTree()
    for i in lis:
        bs_tree.insert(i)
    bs_tree.delete(58)
    for i in bs_tree:   ##将bs_tree对象作为迭代器使用
        print(i,end=" ")
        
###哈希查找###
###哈希函数，将需要查找的值代入哈希函数，得到哈希值。按哈希值作为检索进行查找
"""
算法流程

　　1）用给定的哈希函数构造哈希表；
　　2）根据选择的冲突处理方法解决地址冲突；
　　　　 常见的解决冲突的方法：拉链法和线性探测法。
　　3）在哈希表的基础上执行哈希查找。
"""
class HashTable:
  def __init__(self, size):
    self.elem = [None for i in range(size)] # 使用list数据结构作为哈希表元素保存方法
    self.count = size # 最大表长
 
  def hash(self, key):
    return key % self.count # 散列函数采用除留余数法
 
  def insert_hash(self, key):
    """插入关键字到哈希表内"""
    address = self.hash(key) # 求散列地址
    while self.elem[address]: # 当前位置已经有数据了，发生冲突。
      address = (address+1) % self.count # 线性探测下一地址是否可用
    self.elem[address] = key # 没有冲突则直接保存。
 
  def search_hash(self, key):
    """查找关键字，返回布尔值"""
    star = address = self.hash(key)
    while self.elem[address] != key:
      address = (address + 1) % self.count
      if not self.elem[address] or address == star: # 说明没找到或者循环到了开始的位置
        return False
    return True
 
 
if __name__ == '__main__':
  list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
  hash_table = HashTable(12)
  for i in list_a:
    hash_table.insert_hash(i)
 
  for i in hash_table.elem:
    if i:
      print((i, hash_table.elem.index(i)), end=" ")
  print("\n")
 
  print(hash_table.search_hash(15))
  print(hash_table.search_hash(33))
  
  
"""补码等相关计算"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        ans = 0
        if n<0:
            n = n & 0xffffffff
        while n:
            ans += n & 1
            n >>= 1
        return ans

class Solution:
    def NumberOf1(self, n):
        def fun(t):
            temp = []
            while t>0:
                temp.append(t%2)
                t = t//2
            return temp
        if n == 0:
            return 0
        elif n >0:
            return sum(fun(n))
        else:
            lst = fun(abs(n))
            if len(lst)>31:
                lst = lst[:31]
            if len(lst)<31:
                lst=lst+[0]*(31-len(lst))
            lst = [1 if i==0 else 0 for i in lst]
            temp = 1
            for i in range(len(lst)):
                lst[i] = temp+lst[i]
                temp = lst[i]//2
                lst[i]%=2
            return sum(lst)+1
