from queue import PriorityQueue
Result = []

ans=[]
graph = []
vis =[]
wieghts={}
'''def dfs(u, v):
    if vis[v]==0 :
        if v != 0:
            ans.append((u,v))
        vis[v]=1

        for i in graph[v]:
            dfs(v,i)'''
def dfs(s,s1):
    q=PriorityQueue()
    q.put((s,0,0))
    while not q.empty():
        w,v,u=q.get()
        if vis[v]==1:
            continue
        vis[v]=1
        if(v!=u):
            ans.append((u,v))
        for i in graph[v]:
                q.put((w+wieghts[v,i],i,v,))
                
    






def addEdge(e):
    #print('addedge ', e)
    '''for i in Result:
        if(i[4] == e[4]):
            #print("remove",i[0], i[1], i[3], i[4])
            Result.remove(i)'''

    Result.append(e)


def dmst(vertices, test, root=0):
    oo = int(1e9)
    #print(test)
    cost = {}
    global graph
    global vis
    global wieghts
    #bigmap={}
    back = {}
    label = []
    bio = []
    edge = {}
    ret = 0
    nodes = vertices
    #for e in test:
        #bigmap[(e[3],e[4])]=[]
    #wieghts=[[100000000000 for i in range(vertices)] for j in range(vertices)]

    for j in test:
        #wieghts[j[0]][j[1]]=j[2]
        wieghts[j[0],j[1]]=j[2]
    while(True):
        for i in range(vertices):
            cost[i] = oo

        for e in test:
            if(e[0] == e[1]):
                continue
            if(e[2] < cost[e[1]]):
                #print("found", e[1])
                cost[e[1]] = e[2]
                back[e[1]] = e[0]
                edge[e[1]] = e

        cost[root] = 0

        for i in range(vertices):
            if(cost[i] == oo):
                print('problem at ', i)
                return -1


        for i in range(vertices):
            ret += cost[i]
            if(i!=root):
                #print("add   ",edge[i][0], edge[i][1],edge[i][3], edge[i][4])
                addEdge(edge[i])

        K = 0
        label=[-1 for i in range(vertices)]
        bio = [-1 for i in range(vertices)]
        '''for i in range(vertices):
            label[i] = -1
            bio[i] = -1'''

        for i in range(vertices):
            x = i
            while(True):
                if(x != root and bio[x] == -1):
                    bio[x] = i
                    x = back[x]
                else:
                    break

            if(x != root and bio[x] == i):
                while(True):
                    if(label[x] == -1):
                        label[x] = K
                        x = back[x]
                    else:
                        break
                K = K + 1

        if(K==0):
            break

        for i in range(vertices):
            if(label[i] == -1):
                label[i] = K
                K = K + 1


        for e in range(len(test)):
            xx = label[test[e][0]]
            yy = label[test[e][1]]
            if(xx != yy):
                zz = test[e][2] - cost[test[e][1]]
                #m=edge[test[e][1]]
                #bigmap[(test[e][3],test[e][4])].append((m[3],m[4]))
            else:
                zz = test[e][2]
                #test[e] = (test[e][0],test[e][1], zz, test[e][3],test[e][4])

            test[e] = (xx, yy,zz,test[e][3],test[e][4])
            #test[e] = (test[e][0], yy, test[e][2],test[e][3],test[e][4])

        root = label[root]
        vertices = K
    
    
    result= [(i[3], i[4]) for i in Result]
    Result.clear()
    answer=[]
    
    graph = [set() for i in range(nodes)]
    vis = [ 0 for i in range(nodes)]
    print( len(result))
    for i in result:
        #print(i[0],i[1])
        graph[i[0]].add(i[1])
    dfs(0,0)
    answer = ans[:]
    ans.clear()
    print( "answe length ", len(answer))

    return ret, answer

'''
node, edge  = map( int , input().split())
e=[]
for i in range(edge):
    u,v,w = map( int , input().split())
    e.append((u,v,w,u,v,u,v))

c,ed = dmst(node, e, 0)

for i in ed:
    print( i[5], i[6])



to input to this code, first enter number of edges and vertices
in terminal and write the values of u, v, w in a file(just to make
the input process faster)


sample input
4 6
0 1 6
0 3 4
1 3 3
2 1 2
2 0 1
3 2 5

another input
6 9
0 1 1
1 2 1
2 0 1
5 3 1
3 4 1
4 5 1
1 5 3
2 5 4
0 4 5


'''







































