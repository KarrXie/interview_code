"""序列类型的动态规划"""

"""
问题一：Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
https://leetcode.com/problems/longest-substring-without-repeating-characters/ 
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0   ##动态起始位
        max_len = 0
        d = {}
        for i, c in enumerate(s):    ##相当于同时获取检索信息
            if c in d and d[c] >= start:
                max_len = max(max_len, i - start)
                start = d[c] + 1
            d[c] = i
        return max(max_len, len(s) - start)
        
"""
问题二：栈处理
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
https://leetcode.com/problems/longest-valid-parentheses/
"""
class Solution:
    def longestValidParentheses(self, s):
        retn = 0
        start = -1
        stack=[]
        for i,j in enumerate(s):
            if j==")" and not stack:
                start=i
            if j=="(":
                stack.append(i)
            elif j==")" and stack:
                stack.pop()
                if stack:
                    retn = max(retn,i-stack[-1])
                else:
                    retn = max(retn,i-start)
        return retn
        
"""间隔拿取硬币，使总价值最大"""
# 解决动态规划中的币值最大化问题---在满足所选硬币不相邻的条件下,从一堆硬币中选择最大金额的硬币
# 输入数组C[1..n]保存n个硬币的面值
# 输出可选硬币的最大金额
"""递归问题时，不仅要上一步状态，还要上上一步状态"""
def coinRow(coinrow):
    alist = [0]*(len(coinrow)+1)
    alist[1] = coinrow[0]
    for i in range(2, len(coinrow)+1):
        alist[i] = max(coinrow[i-1]+alist[i-2], alist[i-1])   #此处有加号，是个可延伸的动态规划问题
    return alist.pop()


    
"""
股票买进卖出的问题（1）
重要点：每一次递推代表一次状态转移，分析每个状态下可能的状态，这些可能的状态在下一阶段会转移到什么状态，每一个可能的状态转移是否会需要阈值
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""
"""状态量一定要和所求相关，买进时，视为手里钱减少，为负，卖出时视为手里钱增加，为正"""
The key is 3 states and 5 edges for state transition. 3 states are notHold (stock), hold (stock), and notHold_cooldown. 
The initial values of the latter two are negative infinity since they are meaningless, i.e. you won't hold stocks at first and there's no 
cooldown at first. The 5 edges（状态转移过程）:

hold -----do nothing----->hold
hold -----sell----->notHold_cooldown
notHold -----do nothing -----> notHold
notHold -----buy-----> hold
notHold_cooldown -----do nothing----->notHold

def maxProfit(self, prices):
    notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
    for p in prices:
        hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
    return max(notHold, notHold_cooldown)   
######################方案二############################################
class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell

        
######################股票买进卖出问题二########################################
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
class Solution(object):
    def maxProfit(self,prices):
        min_price=float('inf')  #状态一
        rst = 0           #状态二
        for i in prices:
            rst = max(rst,i-min_price)
            min_price = min(min_price,i)
        return rst