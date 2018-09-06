#!/usr/bin/env python
import sys

#try:
from topoGeneration import *
from briteGen import *
import os.path
import pygraphviz
from networkx.drawing import nx_agraph
import argparse
from argparse import RawTextHelpFormatter


#except ImportError:
#    print "Error: missing one of the libraries (numpy, pyfits, scipy, matplotlib)"
#    sys.exit()




def main():

    parser = argparse.ArgumentParser(description='Generate a topology with BRITE', formatter_class=RawTextHelpFormatter)
    
    parser.add_argument('nNodes', type=int, help='Number of nodes of the network.')
    
    args = parser.parse_args()

#network topology generation with brite
    nNode, points_list, bandwidth_list, delay_list, coordinate_list = briteGen(args.nNodes)

#graph generation
    topoGen = topoGeneration(nNode, points_list, bandwidth_list, delay_list, coordinate_list)
    graph = topoGen.Graph()
    topoGen.showGraph()

if __name__ == '__main__':
    main()
