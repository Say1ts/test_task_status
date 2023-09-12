from collections import defaultdict


class TreeStore:
    def __init__(self, items: list[dict]):
        self.items = items
        self.indexed_items = {}
        self.indexed_parent_ids: dict[int, int] = {}
        self.indexed_children: dict[int, list[dict]] = defaultdict(list)
        self.__index_items()

    def __index_items(self):
        for item in self.items:
            if not item['id']:
                raise ValueError(f'No parent for item: {item}')
            if not item['parent']:
                raise ValueError(f'No parent for item_id: {item["id"]}')

            self.indexed_items[item['id']] = item
            self.indexed_parent_ids[item['id']] = item['parent']
            self.indexed_children[item['parent']].append(item)

    def getAll(self) -> list[dict]:
        return self.items

    def getItem(self, id: int) -> dict:
        return self.indexed_items[id]

    def getChildren(self, id: int) -> list[dict]:
        return self.indexed_children[id]

    def getAllParents(self, id: int or str, parents=None):
        if not parents:
            parents = []
        if id != 'root':
            current_parent = self.indexed_items.get(self.indexed_parent_ids.get(id))
            if current_parent:
                parents.append(current_parent)
                self.getAllParents(current_parent['id'], parents)
        return parents

