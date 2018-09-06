#import networkx as nx
#import matplotlib.pyplot as plt
import subprocess
import os
import sys



def briteGen(numVertex):
    #generation of the topology
    path="path_directory"
    os.system("sh {}/bin/javagen.sh {}".format(path,numVertex))

    points_list = []
    bandwidth_list = {}
    delay_list = {}
    coordinate_list = {}
        


    with open(path+'/file_topo/edges_'+ str(numVertex) + '.txt', 'r') as f:
        for line in f:
            line_data = line.split()
            a = int(line_data[0])
            b = int(line_data[1])
            if (a > b):
                c = b
                b = a
                a = c
            points_list.append((a, b))
            delay_list[a, b] = float(line_data[2])
            bandwidth_list[a, b] = float(line_data[3])

    with open(path+'/file_topo/coordinate_'+ str(numVertex) + '.txt', 'r') as f:
        for line in f:
            line_data = line.split()
            a = int(line_data[0])
#            b = int(line_data[1])
#            if (a > b):
#                c = b
#                b = a
#                a = c
            coordinate_list[a] = float(line_data[1]), float(line_data[2])

#    print('point list', points_list)
    max_value = points_list[0][0]
#    print('max_value iniziale', max_value)
#    print('len(points_list)', len(points_list))

    for row1 in range(len(points_list)):
        for col1 in range(2):
            if points_list[row1][col1] > max_value:
                max_value = points_list[row1][col1]
    nNode = max_value + 1
#    print('nNode', nNode)

    return nNode, points_list, bandwidth_list, delay_list, coordinate_list

