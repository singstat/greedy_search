class Map:
    def __init__(self):
        self.dot_dic = {}
        self.dot_dic['s'] = [ 3, 6]
        self.dot_dic['e'] = [10, 2]
        self.dot_dic['a1'] = [ 4,13]
        self.dot_dic['a2'] = [ 9, 7]
        self.dot_dic['a3'] = [ 1, 1]
        self.dot_dic['a4'] = [ 6, 2]
        self.dot_dic['a5'] = [ 5,10]
        self.dot_dic['a6'] = [ 8, 1]
    
    def print_corr(self, a):
        print self.dot_dic[a]
    
    def printmap(self):
        import matplotlib.pyplot as plt
        
        x = []
        y = []
        color = []
        
        for i in self.dot_dic.keys():
            #print self.dot_dic[i][0]
            x.append(self.dot_dic[i][0])
            y.append(self.dot_dic[i][1])
            if i == 's':
                color.append('red')
            elif i == 'e':
                color.append('green')
            else:
                color.append('blue')

        plt.scatter(x, y, c = color)
        plt.show()
    
    def cal_distance(self, a, b):
        return (self.dot_dic[a][0] - self.dot_dic[b][0])* (self.dot_dic[a][0] - self.dot_dic[b][0]) + (self.dot_dic[a][1] - self.dot_dic[b][1])* (self.dot_dic[a][1] - self.dot_dic[b][1])


class node():
    def __init__(self):
        self.name=None
        self.node=[]
        self.otherInfo = None
        self.prev=None
    def nex(self,child):
        "Gets a node by number"
        return self.node[child]
    def goto(self,data):
        "Gets the node by name"
        for child in range(0,len(self.node)):
            if(self.node[child].name==data):
                return self.node[child]
    def add(self):
        node1=node()
        self.node.append(node1)
        node1.prev=self
        return node1