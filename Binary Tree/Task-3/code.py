class TreeNode:
    def __init__(self,val,lc,rc):
        self.value = val 
        self.lchild = lc
        self.rchild = rc 

class Node:
    def __init__(self,ref,next):
        self.ref = ref 
         
        self.next = next 

class Queue:
    def __init__(self):
        self.front = None 
        self.back = None 

    def enqueue(self,ref):
        if self.front == None:
            self.front = Node(ref,None)
            self.back = self.front 
        else:
            newNode = Node(ref,None)
            self.back.next = newNode
            self.back = newNode

    def dequeue(self):
        if self.front == None:
            return 'Empty Queue'
        else:
            x = self.front 
            self.front = self.front.next 
            return x.ref 
        
    def peek(self):
        if self.front == None:
            return 'Queue is Empty'
        return self.front.elem 
    
    def display(self):
        p = self.front
        while p!=None:
            print(p.elem,end=' ')
            p = p.next 
    def isEmpty(self):
        if self.front == None:
            return True
        return False


def Tree_creation():
    q = Queue()
    v = int(input('Enter Root value:'))
    root = TreeNode(v,None,None)
    r =root
    q.enqueue(root)

    while not q.isEmpty():
        p = q.dequeue()
        x = int(input(f"Enter Left child of {p.value}: "))
        if x!=-1:
            temp = TreeNode(x,None,None)
            p.lchild = temp 
            q.enqueue(temp)

        x = int(input(f"Enter Right child of {p.value}: "))
        if x!=-1:
            temp = TreeNode(x,None,None)
            p.rchild = temp 
            q.enqueue(temp)
    return r

def height(root):
    if root is None:
        return -1 
    left = height(root.lchild)
    right = height(root.rchild)
    if left < right:
        return right+1 
    return left+1 

def heightBalance(root):
    if root is None:
        return 1 
    elif abs(height(root.lchild) - height(root.rchild)) > 1:
        return 0 
    return heightBalance(root.lchild) and heightBalance(root.rchild)



root = Tree_creation()

print(heightBalance(root))