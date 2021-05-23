"""
对于隐形列表的查找问题：
	有一个显性列表，对应一个同大小的递增列表，求符合条件的隐形列表中的点位置对应的显性表的值
"""

"""
题目描述
度度熊和爷爷在玩一个乘法表游戏。乘法表的第i行第j列位置的元素为i*j，并且乘法表下标编号从1开始，比如2 × 3乘法表为
1 2 3
2 4 6
爷爷十分聪明，对于n*m的乘法表，只要度度熊给出一个数k，爷爷就能立刻告诉度度熊乘法表中元素按照不减顺序排列之后，第k个元素是多少。你能重复这个游戏吗？
"""

def factor_seg(x,m,n):
    rst=0
    for k in range(1,m+1):
        if x//k>=n:
            rst+=n
        else:
            rst+=x//k
    return rst

def outputs(m,n,k):
    begin = 1
    lasts = m*n
    while begin<=lasts:
        temp = (begin+lasts)//2   ##思想源自于二分查找
        rst =  factor_seg(temp,m,n)
        if rst<k:
        	begin = temp+1
        else:               #如果rst等于k,此时相当于错过了，但是接下来会一直rst<k，从而导致begin不断接近lasts，而且最佳点在lasts下一个，这样，当跳出while时，begin即为所求点
        	lasts = temp-1
    return begin
                  
print(outputs(4,7,10))