from segment_tree import SegmentTree


def test_range_query1():
    array = [1, 1, 3, 1, 2, 2, 3, 2]
    seg_tree = SegmentTree.from_array(array)
    assert seg_tree.query(2,6) == 8


def test_range_query2():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    seg_tree = SegmentTree.from_array(array)
    assert seg_tree.query(0,6) == 21


def test_range_query3():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    seg_tree = SegmentTree.from_array(array)
    assert seg_tree.query(0,6) == 21


def test_range_query_whole_array():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    seg_tree = SegmentTree.from_array(array)
    assert seg_tree.query(0,7) == 28


def test_range_query_solo_array():
    array = [3]
    seg_tree = SegmentTree.from_array(array)
    assert seg_tree.query(0,1) == 3
