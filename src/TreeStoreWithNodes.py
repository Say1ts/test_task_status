from typing import List, Dict, Union, Optional


class Node:
    def __init__(self, id: Union[int, str], parent: Union[int, str], **kwargs):
        self.id = id
        self.parent_id = parent
        self.children = []
        self.attributes = kwargs

    def add_child(self, child):
        self.children.append(child)


class TreeStore:
    """
    A class-based solution for storing and querying a tree structure.
    This approach uses object-oriented programming to represent each node as an object.
    """
    def __init__(self, items: List[Dict]):
        self.nodes = {}
        self.root_nodes = []
        self._build_tree(items)

    def _build_tree(self, items: List[Dict]):
        """
        Builds the tree by creating Node objects and linking them together.
        """
        temp_nodes = {}

        for item in items:
            if 'id' not in item:
                raise ValueError(f'Item missing id: {item}')
            if 'parent' not in item:
                raise ValueError(f'Item missing parent: {item}')

            node = Node(**item)
            temp_nodes[item['id']] = node

        for node_id, node in temp_nodes.items():
            if node.parent_id == 'root':
                self.root_nodes.append(node)
            else:
                parent_node = temp_nodes.get(node.parent_id)
                if parent_node:
                    parent_node.add_child(node)

        self.nodes = temp_nodes

    def getAll(self) -> List[Dict]:
        """
        Retrieve all items in their original form.

        :return: List of all items.
        """
        return [{**node.attributes, 'id': node.id, 'parent': node.parent_id} for node in self.nodes.values()]

    def getItem(self, id: int) -> Optional[Dict]:
        """
        Retrieve an item by its ID.

        :param id: The ID of the item to retrieve.
        :return: The item as a dictionary, or None if not found.
        """
        node = self.nodes.get(id)
        return {**node.attributes, 'id': node.id, 'parent': node.parent_id} if node else None

    def getChildren(self, id: int) -> List[Dict]:
        """
        Retrieve the children of an item by its ID.

        :param id: The ID of the item whose children are to be retrieved.
        :return: List of children as dictionaries, or an empty list if none found.
        """
        node = self.nodes.get(id)
        return [{**child.attributes, 'id': child.id, 'parent': child.parent_id} for child in
                node.children] if node else []

    def getAllParents(self, id: int) -> List[Dict]:
        """
        Retrieve all parents of an item by its ID, up to the root.

        :param id: The ID of the item whose parent chain is to be retrieved.
        :return: List of parents as dictionaries, in order from the immediate parent to the root.
        """
        parents = []
        node = self.nodes.get(id)
        while node and node.parent_id != 'root':
            node = self.nodes.get(node.parent_id)
            if node:
                parents.append({**node.attributes, 'id': node.id, 'parent': node.parent_id})
        return parents
