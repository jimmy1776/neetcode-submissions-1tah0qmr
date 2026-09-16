class Solution: 
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: 
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False 
            if rank[p1] > rank[p2]:
                par[p2] = p1 
                rank [p1] += rank[p2]
            else:
                par[p1] = p2 
                rank[p2] += rank[p1]
            return True 
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]


            
            
            











#The booleans answers the question:
# did this edge actually connect two separate groups ?  That is the whole cycle detector. 

# False: same root already -> already connected -> this edge is redudant.

#Those two nodes are already reachable from each other through edges you processed earlier. Adding a direct edge between them give you a second path between the same pair of nodes, and a second path is exactly what a cycle is. 



# True: the roots were different, they really were two separate groups andyou just fused them. A useful edge

        





    

        

    