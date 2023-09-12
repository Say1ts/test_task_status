import pytest
from src.TreeStore import TreeStore


@pytest.fixture
def tree_store_instance():
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    return TreeStore(items)


def test_get_all(tree_store_instance):
    assert tree_store_instance.getAll() == [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]


def test_get_item(tree_store_instance):
    assert tree_store_instance.getItem(7) == {"id": 7, "parent": 4, "type": None}


def test_get_children(tree_store_instance):
    assert tree_store_instance.getChildren(4) == [
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    assert tree_store_instance.getChildren(5) == []


def test_get_all_parents(tree_store_instance):
    assert tree_store_instance.getAllParents(7) == [
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 1, "parent": "root"}
    ]
