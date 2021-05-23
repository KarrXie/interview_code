"""排序算法:
    简单插入排序
    二分插入排序
    表插入排序
    直接选择排序
    堆选择排序
    冒泡排序
    快速排序
    归并排序
    蒂姆排序
"""

"""在数据量小于20的时候，插入排序具有最好的性能。当大于20时，快速排序具有最好的性能，归并(merge sort)和堆排序(heap sort)也望尘莫及，尽管复杂度都为nlog2(n)。"""

"""冒泡排序"""
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
     return alist
     
alist = [54,26,93,17,77,31,44,55,20]
print(bubbleSort(alist))
"""改进冒泡算法，加入一个校验，如果某次循环发现没有数值交换，直接跳出循环"""
def modiBubbleSort(alist):
    exchange = True
    passnum = len(alist)-1
    while passnum >=1 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                exchange = True
        passnum-=1
    return alist
    
"""插入排序"""
def insertionSort(alist):
    for index,item in enumerate(alist):
        while index>0 and alist[index-1]>item:
            alist[index] = alist[index-1]
            index-=1
        alist[index]=item
    return alist
    
"""归并算法"""
def merge(lfrom,lto,low,mid,high):
    i,j,k = low,mid,low
    while i<mid and j < high:
        if lfrom[i]<=lfrom[j]:
            lto[k]=lfrom[i]
            i+=1
        else:
            lto[k] = lfrom[j]
            j+=1
        k+=1
    while i < mid:     ##复制第一段剩余记录
        lto[k]=lfrom[i]
        i+=1
        k+=1
    while j < high:    ##复制第二段剩余记录
        lto[k]=lfrom[j]
        j+=1
        k+=1
        
def merge_pass(lfrom,lto,llen,slen):
    i=0
    while i+2*slen<llen:       
        merge(lfrom,lto,i,i+slen,i+2*slen)
        i+=2*slen
    if i+slen<llen:      #后面还剩两个seg，可以再进行一次seg排序
        merge(lfrom,lto,i,i+slen,llen)
    else:                #后面只剩一个seg，而且这个seg内部是已经排好序的
        for j in range(i,llen):
            lto[j]=lfrom[j]
            
def merge_sort(lst):
    slen,llen = 1,len(lst)
    templst = [None]*llen
    while slen<llen:
        merge_pass(lst,templst,llen,slen)
        slen*=2
        merge_pass(templst,lst,llen,slen)
        slen*=2
        
lst = [54,26,93,17,77,31,55,44,20,10]
print(merge_sort(lst))

########################################################################
"""选择排序"""
def selectionSort(alist):
    for i in range(len(alist)-1):
        min = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]
    return alist

    ########################################################################
"""堆排序：
            将列表按从上到下，从左到右看成一个树，然后，逐步让最大的数升到根节点
"""
def heapSort(alist):
    if alist == None or len(alist) == 0:
        return
    length = len(alist)
    output = []
    for i in range(length):
        tempLen = len(alist)
        for j in range(tempLen//2-1, -1, -1):  #这些位置的节点都存在子节点
            preIndex = j
            preVal, heap = alist[preIndex], False
            while 2 * preIndex < tempLen - 1 and not heap:
                curIndex = 2 * preIndex + 1
                if curIndex < tempLen - 1:
                    if alist[curIndex] < alist[curIndex+1]:
                        curIndex += 1
                if preVal >= alist[curIndex]:
                    heap = True
                else:
                    alist[preIndex] = alist[curIndex]
                    preIndex = curIndex
            alist[preIndex] = preVal
        output.insert(0, alist.pop(0))
    return output

test = [2, 6, 5, 9, 10, 3, 7]
print(heapSort(test))

########################################################################
"""快速排序"""
"""以list[0]为基准，找出从左向右开始第一个大于这个基准的位置为止，从list尾部向左
找到第一个小于这个基准的位置为止，然后将这两个值进行互换位置，重复上述过程，直至
leftmark > rightmark，然后，将list[0]和list[rightmark]数值对调。此时，在rightmark检索左侧，所以值都小于等于基准，其右侧，所有值都大于等于基准"""
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
##检索位置小于splitPoint的值都小于list[0],检索位置大于splitPoint的值都大于list[0],,所以接下来分别对左边部分和右边部分进行递归
        quickSortHelper(alist, first, splitPoint-1)   
        quickSortHelper(alist, splitPoint+1, last)

def partition(alist, first, last):
    pivotvlue = alist[first]

    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvlue: # bugfix: 先比较index, 不然数组会越界
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvlue:
            rightmark -= 1

        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
alist2 = [1]
quickSort(alist)
print(alist)


########################################################################
"""希尔排序"""
理解：https://www.cnblogs.com/chengxiao/p/6104371.html
def shellSort(alist):
    sublistcount= len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        sublistcount = sublistcount//2
    return alist

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentValue

alist = [54,26,93,17,77,31,44,55,20]
print(shellSort(alist))


"""蒂姆排序：结合使用了归并排序和插入排序"""
def binary_search(arr, left, right, value):
    """
    二分查找
    :param arr: 列表
    :param left: 左索引
    :param right: 右索引
    :param value: 需要插入的值
    :return: 插入值所在的列表位置
    """
    if left >= right:
        if arr[left] <= value:
            return left + 1
        else:
            return left
    elif left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            return binary_search(arr, mid + 1, right, value)
        else:
            return binary_search(arr, left, mid - 1, value)


def insertion_sort(arr):
    """
    针对run使用二分折半插入排序
    :param arr: 列表
    :return: 结果列表
    """
    length = len(arr)
    for index in range(1, length):
        value = arr[index]
        pos = binary_search(arr, 0, index - 1, value)
        arr = arr[:pos] + [value] + arr[pos:index] + arr[index + 1:]
    return arr


def merge(l1, l2):
    """
    合并
    :param l1: 列表1
    :param l2: 列表2
    :return: 结果列表
    """
    if not l1:
        return l2
    if not l2:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])


def timsort(arr):
    """
    timsort
    :param arr: 待排序数组
    :return:
    """
    if not arr:  # 空列表
        return
    runs = []
    new_run = [arr[0]]
    length = len(arr)
    # 划分run区，并存储到runs里，这里简单的按照升序划分，没有考虑降序的run
    for index in range(1, length):
        if arr[index] < arr[index - 1]:
            runs.append(new_run)
            new_run = [arr[index]]
        else:
            new_run.append(arr[index])
        if length - 1 == index:
            runs.append(new_run)
            break
#############################重点######################################
    # 由于仅仅是升序的run，没有涉及到run的扩充和降序的run
    # 因此，其实这里没有必要使用insertion_sort来进行run自身的排序
    for run in runs:   #这部分是对每个子列表进行插值排序，现阶段没用上
        insertion_sort(run)

    # 合并runs
    sorted_arr = runs.pop()
    for run in runs:
        sorted_arr = merge(sorted_arr, run)
    print(sorted_arr)
timsort([3,5,4,3,2,1,4,32,76])









