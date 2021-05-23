"""题目1：给定数组arr，arr中所有的值都是正数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求组成aim的最少货币数。
举例： arr[5,2,3]，aim=20。  4张5元可以组成20元，其他的找钱方案都要使用更多张的货币，所以返回4。"""
def ChangeMaking(coinVal, change):
    alist = [0]*(change+1)
    for i in range(1, change+1):
        temp = change; j = 0
        while j <= len(coinVal)-1 and i >= coinVal[j]:
  """temp为需要用到的硬币个数。alist[i]表示将i找零需要的硬币个数，对于从小到大需要找零的钱数i，
  依次找出对应最合理的硬币，然后出现一个新的大小i时，尝试不同的硬币，从而将新的i通过先换算一次硬币，
  转换成更小且已知最合理换算硬币的i"""       
            temp = min(alist[i-coinVal[j]], temp) 
            j += 1
        alist[i] = temp + 1
    return alist.pop()
######################################################################
import numpy as np
def ChangeMaking(coinVal,change):
    len_val = len(coinVal)
    rst = np.zeros([len_val,change+1])
    rst[0,1:]=np.inf
    multi=1
    while multi*coinVal[0]<=change:
        rst[0,multi*coinVal[0]]=multi
        multi+=1
    for i in range(1,len_val):
        for j in range(1,change+1):
            leftup = np.inf
            multi = 0
            while multi*coinVal[i]<=j:
                if rst[i-1,j-multi*coinVal[i]]!=np.inf:
                    leftup = min(rst[i-1,j-multi*coinVal[i]]+multi,leftup)
                multi+=1
            rst[i,j] = leftup
    return rst[len_val-1,change]
print(ChangeMaking([1, 5, 10, 25], 63))
################################################################
def ChangeMaking1(coinVal,change):
    len_val = len(coinVal)
    rst = np.zeros([len_val,change+1])
    rst[0,1:]=np.inf
    multi=1
    while multi*coinVal[0]<=change:
        rst[0,multi*coinVal[0]]=multi
        multi+=1
    for i in range(1,len_val):
        for j in range(1,change+1):
            if coinVal[i]>j:
                rst[i,j]=rst[i-1,j]
            else:
                rst[i,j]=min(rst[i-1,j],rst[i,j-coinVal[i]]+1)
    return rst[len_val-1,change]
#################################################################    

"""题目2： 给定数组arr，arr中所有的值都为正数，每个值仅代表一张钱的面值，
再给定一个整数aim代表要找的钱数，求组成aim的最小货币数。
题解: 相对于上一题，这道题的arr中的钱只有一张，而不是任意多张，
构造dp数组的含义也同上，但是此时略有不同，"""
import numpy as np
def ChangeMaking(coinVal,change):
    len_val = len(coinVal)
    rst = np.zeros([len_val,change+1])
    rst[0,1:]=np.inf
    if coinVal[0]<=change:
        rst[0,coinVal[0]]=1
    for i in range(1,len_val):
        for j in range(1,change+1):
            leftup = np.inf
            if j>=coinVal[i] and rst[i-1,j-coinVal[i]]!=np.inf:
                leftup = rst[i-1,j-coinVal[i]]+1
            rst[i,j] = min(rst[i-1,j],leftup)
    return rst[len_val-1,change]
    
print(ChangeMaking([1,2,1,6,8,20],19))

"""题目3：给定数组arr,arr中所有的值都为正数且重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求换钱有多少种方法。 """
import numpy as np
def ChangeMaking(coinVal,change):
    len_val = len(coinVal)
    rst = np.zeros([len_val,change+1])  
    rst[:,0]=1
    multi=1
    while multi*coinVal[0]<=change:
        rst[0,multi*coinVal[0]]=1
        multi+=1
    for i in range(1,len_val):
        for j in range(1,change+1):
            if j-coinVal[i]>=0:
                rst[i,j]=rst[i-1,j]+rst[i,j-coinVal[i]]
            else:
                rst[i,j]=rst[i-1,j]
    print(rst)
    return rst[-1,-1]
print(ChangeMaking([4, 5, 10, 25], 39))

"""问题4：和3类似，只是每个货币不能任意使用，仅代表一张"""
import numpy as np
def ChangeMaking(coinVal,change):
    len_val = len(coinVal)
    rst = np.zeros([len_val,change+1])  
    rst[:,0]=1
    if coinVal[0]<=change:
        rst[0,coinVal[0]]=1
    for i in range(1,len_val):
        for j in range(1,change+1):
            rst[i,j]=rst[i-1,j]+rst[i-1,j-coinVal[i]]
    return rst[-1,-1]
print(ChangeMaking([4, 5,10,5, 10, 25], 39))

"""间隔拿取硬币，使总价值最大"""
# 解决动态规划中的币值最大化问题---在满足所选硬币不相邻的条件下,从一堆硬币中选择最大金额的硬币
# 输入数组C[1..n]保存n个硬币的面值
# 输出可选硬币的最大金额
"""递归问题时，不仅要上一步状态，还要上上一步状态"""
def coinRow(coinrow):
    alist = [0]*(len(coinrow)+1)
    alist[1] = coinrow[0]
    for i in range(2, len(coinrow)+1):
        alist[i] = max(coinrow[i-1]+alist[i-2], alist[i-1])
    return alist.pop()

##################################################################################    
"""台阶问题"""

"""递推"""
def fun(num_step):
    if num_step==1:
        return 1
    if num_step==2:
        return 2
    a,b = 1,2
    for i in range(3,num_step):
        temp = a+b
        a=b
        b=temp
"""递归，当数字大时，时间复杂度成指数增长"""    
def fun(num_step):
    if num_step==1:
        return 1
    if num_step==2:
        return 2
    else:
        return fun(num_step-1)+fun(num_step-2)
print(fun(300))

##################################################################################    
"""0-1背包问题"""
import numpy as np

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1,-1]

if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    result = solve(v,w,weight,n)
    print(result)

###############################################################################
def solve(dicts,aims):
    rst = np.zeros([len(dicts)+1,aims+1])
    rst[0,:]=np.inf
    rst[:,0]=0
    i=1
    for val,num in dicts.items():
        for j in range(1,aims+1):
            if val>j:
                rst[i,j]=rst[i-1,j]
            else:
                multi=0
                temp = np.inf
                while multi*val<=j and multi<=num:
                    temp = min(temp,rst[i-1,j-val*multi]+multi)
                    multi+=1
                rst[i,j]=temp
        i+=1
    return rst[-1,-1]
dcts={1:3,5:2,10:1,6:1}
print(solve(dcts,17))