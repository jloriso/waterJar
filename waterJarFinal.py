class Graph:
    class GraphNode:
        def __init__(self, jar1 = 0, jar2 = 0, jar3 = 0, visit = False, pre = None):
            self.jar1 = jar1
            self.jar2 = jar2
            self.jar3 = jar3
            self.visit = visit
            self.pre = pre
        
        def __str__(self):
            return "(" + str(self.jar1) + "," + str(self.jar2) + "," + str(self.jar3) + ")"

        def __repr__(self):
            return str(self)
        
    ###
    def __init__(self, j1 = 0, j2 = 0, j3 = 0, target = 0):
        self.j1 = j1
        self.j2 = j2
        self.j3 = j3
        self.target = target
        self.vertices = {}
        for x in range(j1 + 1):
            for y in range(j2 + 1):
                for z in range(j3 + 1):
                    node = Graph.GraphNode(x, y, z, False, None)
                    self.vertices[node] = None

    def isFound(self, a: GraphNode) -> bool:
        if a.jar1 == self.target:
            return True
        elif a.jar2 == self.target:
            return True
        elif a.jar3 == self.target:
            return True
        else:
            return False

    def isAdjacent(self, n1: GraphNode, n2: GraphNode) -> bool:
        #sum of the jars in each node
        s1 = n1.jar1 + n1.jar2 + n1.jar3
        s2 = n2.jar1 + n2.jar2 + n2.jar3
        
        #fill 1
        if n1.jar2 == n2.jar2 and n1.jar3 == n2.jar3 and n2.jar1 == self.j1:
            return True
        #fill 2
        elif n1.jar1 == n2.jar1 and n1.jar3 == n2.jar3 and n2.jar2 == self.j2:
            return True
        #fill 3
        elif n1.jar1 == n2.jar1 and n1.jar2 == n2.jar2 and n2.jar3 == self.j3:
            return True
        
        #empty1 to 3
        elif s1 == s2 and n1.jar2 == n2.jar2 and n2.jar1 == 0:
            return True
        #empty1 to 2
        elif s1 == s2 and n1.jar3 == n2.jar3 and n2.jar1 == 0:
            return True
        #empty2 to 3
        elif s1 == s2 and n1.jar1 == n2.jar1 and n2.jar2 == 0:
            return True
        #empty2 to 1
        elif s1 == s2 and n1.jar3 == n2.jar3 and n2.jar2 == 0:
            return True
        #empty3 to 1
        elif s1 == s2 and n1.jar2 == n2.jar2 and n2.jar3 == 0:
            return True
        #empty3 to 2
        elif s1 == s2 and n1.jar1 == n2.jar1 and n2.jar3 == 0:
            return True
        
        #split3 to 1
        elif s1 == s2 and n1.jar2 == n2.jar2 and n2.jar1 == self.j1:
            return True
        #split 3 to 2
        elif s1 == s2 and n1.jar1 == n2.jar1 and n2.jar2 == self.j2:
            return True
        #split2 to 1
        elif s1 == s2 and n1.jar3 == n2.jar3 and n2.jar1 == self.j1:
            return True
        #split2 to 3
        elif s1 == s2 and n1.jar1 == n2.jar1 and n2.jar3 == self.j3:
            return True
        #split1 to 3
        elif s1 == s2 and n1.jar2 == n2.jar2 and n2.jar3 == self.j3:
            return True
        #split1 to 2
        elif s1 == s2 and n1.jar3 == n2.jar3 and n2.jar2 == self.j2:
            return True      
        
        else:
            return False



    def BFS(self):
        start = Graph.GraphNode(0,0,0, False)
        queue = []
        output = []

        queue.append(start)
        while len(queue) > 0:
            u = queue.pop(0)
            for v in self.vertices:
                if self.isAdjacent(u,v) and v not in queue:
                    if v.visit == False:
                        v.visit = True
                        v.pre = u
                        if self.isFound(v):
                            while v.pre is not None:
                                output.append(v)
                                v = v.pre
                            output.append(start)
                            return output
                        else:
                            queue.append(v)
            u.visit = True
        return output

def reverse(arr):
    output = arr[:: -1]
    return output

def main():
    #take the user input
    jar1, jar2, jar3, target = 0,0,0,0

    #verify that the input is within the size of the jars
    while jar1 < 1 or jar1 > 10:
        jar1 = int(input("Size of the first jar: "))
    while jar2 < 1 or jar2 > 10:
        jar2 = int(input("Size of the second jar: "))
    while jar3 < 1 or jar3 > 10:
        jar3 = int(input("Size of the third jar: "))
    while target < 1 or target > 10:
        target = int(input("What is the target: "))
    
    print()
    
    #initialize the graph
    g = Graph(jar1, jar2, jar3, target)
    
    #print the BFS
    output = g.BFS()

    #verse output
    output = reverse(output)

    #check if output is an empty string
    if len(output) == 0:
        print("Unable to find a path.")
    else:
        print(output)
#run
main()