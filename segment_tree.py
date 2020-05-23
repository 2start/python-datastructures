class SegmentTree:
    class Node:
        def __init__(self, value, start, end):
            self.left = None
            self.right = None
            self.value = value
            self.start = start
            self.end = end

    @staticmethod
    def from_array(array):
        assert len(array) > 0
        tree = SegmentTree()
        tree.init_tree(array)
        return tree

    def ___init__(self, array):
        self.root = None

    def init_tree(self, array):
        self.root = self.build_tree(array, 0, len(array))

    def build_tree(self, array, start, end):
        if start == end:
            return None
        if end - start == 1:
            return self.Node(array[start], start , end)

        mid = start + (end - start) // 2

        left_child = self.build_tree(array, start, mid)
        right_child = self.build_tree(array, mid, end)
        node = self.Node(left_child.value + right_child.value, start, end)
        node.left = left_child
        node.right = right_child
        return node

    def query(self, start, end):
        def rec_sum(node):
            if start <= node.start < node.end <= end:
                return node.value
            if start >= node.end or end <= node.start:
                return 0
            if node.left and node.right:
                return rec_sum(node.left) + rec_sum(node.right)
            return 0

        return rec_sum(self.root)