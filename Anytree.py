'''
Creating an ASCII style phylogenic tree pased on the lineage data that was stroed in the pkl files
'''

import json
from anytree import Node, RenderTree
import pickle


with open('Host tree.pkl', 'rb') as fp:
    nested_json = pickle.load(fp)

def build_tree(node_data, parent_node=None):
    '''
    Recursive function to build tree nodes
    '''
    for key, value in node_data.items():
        node = Node(key, parent=parent_node)
        if value:
            build_tree(value, parent_node=node)

# Create the root node
root = Node("Root")

# Build the tree structure
build_tree(nested_json, parent_node=root)

# Render and visualize the tree
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

# Alternatively, you can visualize the tree with graphical representation
from anytree.render import AsciiStyle

# Create a unique dot file and render the tree as ASCII art
print(RenderTree(root, style=AsciiStyle()).by_attr())
