
class Graph:

    def __init__(self, size):
        self.edges = {}
        self.cost = {}

    def addNode(self, node):
        self.edges[node] = {}

    def addEdge(self, node1, node2,w):
        self.edges[node1][node2] = w

    def getSub(self, node):
        return self.edges[node]

    def getCost(self,node):
        return self.cost[node]

    def setCost(self, node1, node2, edge):
        if self.getCost(node1) + edge < self.getCost(node2):
            self.cost[node2] = self.getCost(node1) + edge

    def getDistance(self,node1, node2,c):
        return self.getSub(node1)[node2]+c

    # this function travel all graph and update cost of each node
    def DFS(self, start, visited):
        visited +=[start]

        for child in self.getSub(start):
            self.setCost(start, child, self.getSub(start)[child])

        for node in self.getSub(start):
            if node not in visited:
                self.DFS(node,visited)

    # after we set cost for each node/ver we need this fun to find small dis
    def DFS_helper(self, start, end, paths, dis = 0):
        paths += [start]
        if start == end:
            return paths

        for node in self.getSub(start):
            if end in paths:
                break
            if node not in paths:
                new_dis = self.getDistance(start, node, dis)
                """
                    c
                     \3     this just part of graph example if we come from A the distance from A to B is 6 > 3 that's mean we should 
             A--6-->B(3)         come from C if statement prevent as from continue in this path
                      
                """
                if new_dis  <= self.getCost(node) and new_dis <=self.getCost(end):
                    self.DFS_helper(node, end, paths, new_dis)

        return paths

if __name__ == "__main__":
    nodes = ["S","B","C","D",'E']

    g = Graph(len(nodes))

    for node in nodes:
        g.addNode(node)
    g.cost["S"] = 0

    infinity = float('inf')
    for n in nodes[1:]:
        g.cost[n] = infinity

    g.addEdge("S", "D",1)
    g.addEdge('S', "B",6)
    g.addEdge("B", "C",5)
    g.addEdge("D", "E",1)
    g.addEdge("D", "B",2)
    g.addEdge("E", "B",2)
    g.addEdge("E", "C",5)


    g.DFS("S",[])
    print(g.cost)
    print(g.DFS_helper("S","C",[]))
