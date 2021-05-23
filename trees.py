# �����ӡ���������ݹ飩
def preOrderTraverse(node):
    if node is None:
        return None
    print(node.val)
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)
    
# �����ӡ���������ǵݹ飩
def preOrderTravese(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()
#�ڶ��ַ���
def __iter__(self):
    stack = []
    node = self.root
    while node or stack:
        while node:
            yield node.val
            stack.append(node)
            node = node.left
        node = stack.pop().right
        
########### �����ӡ���������ݹ飩
def inOrderTraverse(node):
    if node is None:
        return None
    inOrderTraverse(node.left)
    print(node.val)
    inOrderTraverse(node.right)
        
# �����ӡ���������ǵݹ飩
def inOrderTraverse(node):
    stack = []
    node = node
    while node or stack:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)
            node = node.right        
###�ڶ��ַ���        
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
        
#### �����ӡ���������ݹ飩
def postOrderTraverse(node):
    if node is None:
        return None
    postOrderTraverse(node.left)
    postOrderTraverse(node.right)
    print(node.val)        
        
# �����ӡ���������ǵݹ飩
def postOrderTraverse(node):
    stack = [node]
    stack2 = []  ##ʹ������ջ
    while stack:
        node = stack.pop()
        stack2.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    while stack2:
        print(stack2.pop().val)    

###������ȱ���
def __iter__(self):
    stack = []
    node = self.root
    while 1:
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        yield node.val
        if stack:
            node = stack.pop(0)
        else:
            break        
        
#### ��������ڵ����
def treeNodenums(node):
    if node is None:
        return 0
    nums = treeNodenums(node.left)
    nums += treeNodenums(node.right)
    return nums + 1        
        
#### ��������������
def bTreeDepth(node):
    if node is None:
        return 0
    ldepth = bTreeDepth(node.left)
    rdepth = bTreeDepth(node.right)
    return (max(ldepth, rdepth) + 1)       
        
        
        
        
        
        
        
        
        
        
        