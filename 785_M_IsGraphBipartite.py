## Solution: DFS with stack instead of recursion for memory optimization

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        label = [0] * len(graph)
        stack = []
        
        def traverse(node):
            nonlocal label, stack
            label[node] = 1
            stack.append(node)
            
            while len(stack) > 0:
                node = stack.pop()
                lab = label[node]
                for v in graph[node]:
                    if label[v] != 0:
                        if label[v] != -lab:
                            return False
                    else:
                        label[v] = -lab
                        stack.append(v)
                        
            return True
        
        for node in range(len(graph)):
            if label[node] == 0 and not traverse(node):
                return False

        return True
                       
        
            
            
                
