from collections import defaultdict
from typing import Dict, Union, List


class TreeStore:
    """
    A class-based solution for storing and querying a tree structure.
    This approach minimizes the number of operations and uses less memory
    compared to an object-oriented approach.
    """
    def __init__(self, items: list[dict]):
        self._items = items
        self._indexed_items: Dict[int, Dict] = {}
        self._indexed_parent_ids: Dict[int, Union[int, str]] = {}
        self._indexed_children: Dict[Union[int, str], List[Dict]] = defaultdict(list)
        self._index_items()

    def _index_items(self):
        """
        Indexes the items for quick lookup. Populates the _indexed_items,
        _indexed_parent_ids, and _indexed_children dictionaries.
        """
        for item in self._items:
            if 'id' not in item:
                raise ValueError(f'Item missing id: {item}')
            if 'parent' not in item:
                raise ValueError(f'Item missing parent: {item}')

            self._indexed_items[item['id']] = item
            self._indexed_parent_ids[item['id']] = item['parent']
            self._indexed_children[item['parent']].append(item)

    def getAll(self) -> List[Dict]:
        """
        Retrieve all items in their original form.

        :return: List of all items.
        """
        return self._items

    def getItem(self, id: int) -> Dict:
        """
        Retrieve an item by its ID.

        :param id: The ID of the item to retrieve.
        :return: The item as a dictionary, or an empty dictionary if not found.
        """
        return self._indexed_items.get(id, {})

    def getChildren(self, id: int) -> List[Dict]:
        """
        Retrieve the children of an item by its ID.

        :param id: The ID of the item whose children are to be retrieved.
        :return: List of children as dictionaries, or an empty list if none found.
        """
        return self._indexed_children.get(id, [])

    def getAllParents(self, id: Union[int, str]) -> List[Dict]:
        """
        Retrieve all parents of an item by its ID, up to the root.

        :param id: The ID of the item whose parent chain is to be retrieved.
        :return: List of parents as dictionaries, in order from the immediate parent to the root.
        """
        parents = []
        while id != 'root':
            id = self._indexed_parent_ids.get(id)
            if id is None:
                break
            parent = self._indexed_items.get(id)
            if parent:
                parents.append(parent)
        return parents

