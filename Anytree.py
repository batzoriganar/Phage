import json
from anytree import Node, RenderTree
import pickle
# Sample nested JSON data
nested_json = {
    "10239": {
        "2732410": {
            "2732411": {
                "2732094": {
                    "10860": {
                        "31596": {}
                    }
                }
            }
        }
    },
    "2731618": {
        "2731619": {
            "35242": {}
        }
    },
    # Add more data here...
}
# with open('name_hierarchy_host.json' , 'r') as datafile:
#     nested_json=json.load(datafile)
with open('Host tree.pkl', 'rb') as fp:
    nested_json = pickle.load(fp)
# Recursive function to build tree nodes
def build_tree(node_data, parent_node=None):
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
from anytree.exporter import UniqueDotExporter

# Create a unique dot file and render the tree as ASCII art
# UniqueDotExporter(root).to_picture("tree.png")
print(RenderTree(root, style=AsciiStyle()).by_attr())
