from binary_heap import BinaryHeap


class MinHeap(BinaryHeap):
    def __init__(self, heap=[]):
        super(self.__class__, self).__init__(heap=heap)

    def _heapify(self, index, size):
        """
        Brief:
            Private method to shiftup the smallest number
        Args:
            heap: Unprocessed Array
            index: Index to start
            size: Size of the array
        """
        l_index = self._left_child_index(index)
        r_index = self._right_child_index(index)
        largest_index = index
        if l_index < size and self.heap[l_index] < self.heap[index]:
            largest_index = l_index
        if r_index < size and self.heap[r_index] < self.heap[largest_index]:
            largest_index = r_index
        if largest_index != index:
            self._swap(largest_index, index)
            self._heapify(largest_index, size)

    def delete_element_at_index(self, index):
        """
        Remove the element at the specified index
        """
        if index >= self.length():
            return

        self.heap[index] = float("-inf")
        self.swim_up(index + 1)
        self.extract_root()

    def _swim_up(self, index):
        """
        Method to swim up if the children are smaller the root
        Args:
            index: Index of the children
            (Here we need to pass 1 based index instead of 0 based index
            so that it will be easy for us to find the parrent)
        Example:
                            1
                       2		3
                   4		5		6
            In the above heap root will be self.heap[0]
            consider elements 2,3 are in respective index 2,3 the parrent node
            will be (children_idex/2) - 1 = (2-1) - 1 => 0
        """
        if index == 1:
            return
        parent = (index // 2)
        if self.heap[parent - 1] < self.heap[index - 1]:
            return
        self._swap(parent - 1, index - 1)
        self._swim_up(index=parent)
