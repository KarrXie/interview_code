"""
并查集算法Union Find:核心思想是用一个root数组，每个点开始初始化为不同的值，如果两个点属于相同的组，
就将其中一个点的root值赋值为另一个点的位置，这样只要是相同组里的两点，通过find函数会得到相同的值。
"""

###问题一：
###夫妻牵手问题：n对夫妻，随机坐成一排，问最小的对调次数，使每对夫妻坐在一起
"""
https://leetcode.com/problems/couples-holding-hands/
思路：此处用到了两次并查集算法。
1. 给定的list中有2*n个元素，相当于2n个顶点，首先，我们需要给他们进行连线（或者放到同一个集合下），此处可以简化成 index//2，
这样，同一对夫妻的标签号变得相同（此时相当于把2n个点转化成了n条线）
2. 贪婪算法思路：每两个元素的获取迭代，如果这两个元素不属于同一条边，则将这两条边合并成一条边，代价是调换次数加1
"""
class Solution(object):
    def parents(self,val,dicts):
        while dicts[val]!=val:
            val = dicts[val]
        return val
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        islands=0
        row = [i//2 for i in row]
        dicts = dict((i,i) for i in row)
        for i in range(0, len(row), 2):
            a = self.parents(row[i],dicts)
            b = self.parents(row[i+1],dicts)
            if a==b:
                continue
            else:
                dicts[a] = b
                islands+=1
        return islands
        
##问题二：一个以列表为元素的列表，表示一个图的边，该图中有一个闭环，找到生成闭环的最后一条边，并输出
"""
https://leetcode.com/problems/redundant-connection/
"""
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find_root(v):
            while dicts[v]!=v:
                v = dicts[v]
            return v
        dicts = {}
        for edge in edges:
            if edge[0] not in dicts:
                if edge[1] not in dicts:
                    dicts[edge[0]] = edge[0]
                    dicts[edge[1]] = edge[0]
                else:
                    dicts[edge[0]] = dicts[edge[1]]
                continue
            else:
                if edge[1] not in dicts:
                    dicts[edge[1]] = dicts[edge[0]]
                    continue
                else:
                    t0 = find_root(edge[0])
                    t1 = find_root(edge[1])
                    if t0!=t1:
                        dicts[t1]=t0
                    else:
                        return edge

"""
摩尔投票算法
https://blog.csdn.net/tinyjian/article/details/79110473
"""      
###出现次数超过一半的数
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0
        val,cnt = None,0
        for num in numbers:
            if cnt==0:
                val,cnt = num,1
            elif val == num:
                cnt+=1
            else:
                cnt-=1
        return val if numbers.count(val)*2>len(numbers) else 0
       
###出现次数超过三分之一的数
class Solution(object):
    def majorityElement(self, nums):
        a, b, ca, cb, ans = None, None, 0, 0, []
        for n in nums:
            if   n  == a: ca += 1
            elif n  == b: cb += 1
            elif ca == 0: a, ca = n, 1
            elif cb == 0: b, cb = n, 1
            else:         ca, cb = ca - 1, cb - 1
        ca, cb = 0, 0
        for n in nums:
            if   n == a: ca += 1
            elif n == b: cb += 1

        if ca > len(nums)/3:
            ans.append(a)
        if cb > len(nums)/3:
            ans.append(b)
        return ans
        
###1到n的数据中出现1的次数：
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n==0:
            return 0
        if n<10:
            return 1
        finalreslt=0
        def count9(k):
            return k*10**(k-1)
        def lst(n):
            temp,rst = n,[]
            while temp:
                rst.append(temp%10)
                temp//=10
            return rst
        lst = lst(n)
        while lst:
            t = lst.pop()
            k = len(lst)
            if t==0:
                continue
            elif t==1:
                temp=0
                k1 = 0
                for i in lst:
                    temp+=i*10**k1
                    k1+=1
                finalreslt+=temp+1
                finalreslt+=count9(k)
            else:
                temp=0
                k1 = k-1
                finalreslt+=count9(k)*t
                finalreslt+=10**k
        return finalreslt