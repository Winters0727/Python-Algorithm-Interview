import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    class Node:
        def __init__(self, x, y, value=None):
            self.value = value
            self.x = x
            self.y = y
            self.children = [None, None]
        
    def preorder(root, result=None):
        if not result:
            result = []
        if root:
            result.append(root.value)
            result = preorder(root.children[0], result)
            result = preorder(root.children[1], result)
        return result
        
    def postorder(root, result=None):
        if not result:
            result = []
        if root:
            result = postorder(root.children[0], result)
            result = postorder(root.children[1], result)
            result.append(root.value)
        return result
        
    new_info = sorted([[*val, idx+1] for idx, val in enumerate(nodeinfo)], key=lambda x : [x[1], x[0]])
    root = Node(*new_info.pop())
    while new_info:
        current = root
        node = Node(*new_info.pop())
        while True:
            if node.x < current.x:
                if current.children[0]:
                    current = current.children[0]
                    continue
                else:
                    current.children[0] = node
                    break
            else:
                if current.children[1]:
                    current = current.children[1]
                    continue
                else:
                    current.children[1] = node
                    break
    
    answer = [preorder(root), postorder(root)]
    return answer