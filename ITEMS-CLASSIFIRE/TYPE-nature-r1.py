"""
!***************************************************************************!
 Reason for penetration:
    If there is a need to develop any non-numerical processor.
    Neural, optical, live, cellular and analog processors can be examples.
 
 It works based on the graph

!***************************************************************************!
"""

import networkx as nx

class Network:
    def init(self, graph: nx.Graph = None, **attributes):
        self.graph = graph
        self.attributes = attributes

    def set_item(self, node, features: dict = None):
        """Adds a node to the graph with optional features."""
        self.graph.add_node(node, features) if features else self.graph.add_node(node)

    def get_item(self, node):
        """Returns the node's attributes."""
        return self.graph.nodes[node]

    def find_target_node(self, attribute, axis='maximum-attribute'):
        """Finds the node with the maximum or minimum value of a given attribute.

        Args:
            attribute: The attribute to find the maximum or minimum value for.
            axis: The axis to find the extreme value along, either 'maximum-attribute' or 'minimum-attribute'.

        Returns:
            The node with the extreme value, or None if no nodes or attribute found.
        """

        if not self.graph.nodes():
            return None

        if axis == 'maximum-attribute':
            extreme_value = float('-inf')
        elif axis == 'minimum-attribute':
            extreme_value = float('inf')
        else:
            raise ValueError(f"Invalid axis: {axis}")

        target_node = None
        for node, data in self.graph.nodes(data=True):
            if attribute in data:
                value = data[attribute]
                if axis == 'maximum-attribute' and value > extreme_value:
                    extreme_value = value
                    target_node = node
                elif axis == 'minimum-attribute' and value < extreme_value:
                    extreme_value = value
                    target_node = node

        return target_node

    def find_nodes_by_attribute(self, attribute, value):
        """Finds nodes with a specific attribute value.

        Args:
            attribute: The attribute to filter by.
            value: The value of the attribute.

        Returns:
            A list of nodes with the specified attribute value.
        """

        return [node for node, data in self.graph.nodes(data=True) if attribute in data and data[attribute] == value]
    
"""
from GLOBALS import PRINT
import networkx as nx

class Network:
    def __init__(self, grath: nx.Graph | None, iterabel: int=0,  **kwargs) -> None:
        self.grath = grath

        #if args is not None and iterabel != 0: (self.arg = arg for arg in args)
        if kwargs is not None and iterabel == 0: self.attributes = kwargs
        else: self.attributes = None
    
    def __setitem__(self, key: nx.Graph | None, features: dict | None) -> None:
        try:
            self.grath.add_node(key)
            if features is not None:
                for feature in features.keys():
                    self.gerth.set_node_attributes(key, feature = features[feature])
        except:
            if PRINT : print(f"The node {self.grath} in the graph is in the position: ")
    
    def __getitem__(self, key: nx.Graph) -> nx.Graph:
        return self.grath.get_node(key)
    
    def Finde_target_Node(self, attribute: any, axis: str='maximum-attribute') -> nx.Graph:
        if not self.graph.nodes(): raise ValueError("No graph nodes")

        match(axis):
            case 'maximum-attribute':
                max_value = float('-inf')
                max_node = None
                for node, atrributes in self.graph.nodes(data=True):
                    if attribute in atrributes:
                        value = atrributes[attribute]
                        if value > max_value:
                            max_value = value ; max_node = node
                return max_node
            case 'minimum-attribute':
                max_value = float('+inf')
                max_node = None
                for node, atrributes in self.graph.nodes(data=True):
                    if attribute in atrributes:
                        value = atrributes[attribute]
                        if value < max_value:
                            max_value = value ; max_node = node
                return max_node
            case self.attributes[attribute]:
                return [node for node, attributes in self.grath.nodes(data=True): if attributes[attribute] == attribute]


"""