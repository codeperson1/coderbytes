def ParseNodes(strArr):
    nodes = []
    for i in range(0, len(strArr)):
        node = strArr[i][1:len(strArr[i])-1].split(',')
        for j in range(0, len(node)):
            node[j] = int(node[j])
        nodes.append(node)
    return nodes

def CopyNodes(nodes):
    _nodes = []
    for i in range(0, len(nodes)):
        node = []
        for j in range(0, len(nodes[i])):
            node.append(nodes[i][j])
        _nodes.append(node)
    return _nodes

def RequiredConnections(nodes):
    connections = []
    node_size = 2
    # nodes = nodes.copy()
    nodes = CopyNodes(nodes)
    while(node_size <= len(nodes)):
        #print(node_size)
        for i in range(0, node_size):
            for j in range(0, node_size):
                if(i!=j and nodes[i][j]==1):
                    for k in range(0, node_size):
                        if(k!=i):
                            if(nodes[j][k]==1):
                                if(nodes[i][k]!=1):
                                    if(0):
                                        print("i = %d" % (i))
                                        print("j = %d" % (j))
                                        print("k = %d" % (k))
                                    connections.append([i, k])
                                    nodes[i][k] = 1
        node_size += 1

    # sort the connections
    _connections = []
    for i in range(0, len(nodes)):
        _connections.append([i,[]])
    for j in range(0, len(connections)):
        _connections[connections[j][0]][1].append(connections[j][1])
    def key_fn(a):
        return a[0]
    _connections.sort(key=key_fn)
    for i in range(0, len(_connections)):
        _connections[i][1].sort()
    #print(_connections)
    connections = []
    for i in range(0, len(_connections)):
        for j in range(0, len(_connections[i][1])):
            connections.append([_connections[i][0],_connections[i][1][j]])

    return connections

def SerializeConnections(connections):
    connections_str = ''
    for i in range(0, len(connections)):
        if(i > 0):
            connections_str += '-'
        connections_str += '(%d,%d)' % (connections[i][0], connections[i][1])
    return connections_str

def TransitivityRelations(strArr):
    nodes = ParseNodes(strArr)
    connections = RequiredConnections(nodes)
    is_transitive = (len(connections)==0)
    if(is_transitive):
        result = 'transitive'
    else:
        result = SerializeConnections(connections)
    return result

#print TransitivityRelations(raw_input())
print(TransitivityRelations(("(1,1,0,0)","(0,0,1,0)","(0,1,0,1)","(1,0,0,1)")))
