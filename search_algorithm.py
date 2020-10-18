import pygame
import graphUI
from node_color import white, yellow, black, red, blue, purple, orange, green

"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""


def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search

    """
    # TODO: your code

    #Init visited & path
    visitted=[]
    path=[]
    for i in range(0,len(graph),1):
        visitted.append(False)
        path.append(-1)

    #Diem Start

    graph[start][3]=orange
    graphUI.updateUI()
    #Hang doi luu cac node chuan bi xet

    queue=[]
    queue.append(start)
    check = 0
    while((queue.__len__()!=0)&(check==0)):

        #Dinh hien tai
        graph[queue[0]][3] = yellow
        graphUI.updateUI()
        visitted[queue[0]] = True

        for count in range(0 ,len(graph[queue[0]][1]) , 1):
            # Neu la Dinh dich
            if (graph[queue[0]][1][count]==goal):
                temp=graph[queue[0]][1][count]
                graph[temp][3]=purple
                #graph[queue[0]][3] = purple
                graphUI.updateUI()
                check=1
                break
            #Neu khong phai
            elif((graph[queue[0]][1][count] not in queue) and (visitted[graph[queue[0]][1][count]]==False)):
                queue.append(graph[queue[0]][1][count])
                graph[queue[len(queue)-1]][3]=red
        if(check==0):
            graph[queue[0]][3] = blue
            queue.pop(0)
            graphUI.updateUI()

    graph[start][3] = orange
    graphUI.updateUI()
    print("Implement BFS algorithm.")
    pass


def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    # TODO: your code
    print("Implement DFS algorithm.")
    pass


def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    # TODO: your code
    print("Implement Uniform Cost Search algorithm.")
    pass


def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    # TODO: your code
    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()

