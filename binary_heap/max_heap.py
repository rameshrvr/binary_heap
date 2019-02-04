from binary_heap import BinaryHeap


class MaxHeap(BinaryHeap):
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
        left_index = self._left_child_index(index)
        if (size - 1) - left_index == 0:
            if self.heap[left_index] > self.heap[index]:
                self._swap(index, left_index)
        else:
            right_index = left_index + 1
            if self.heap[right_index] > self.heap[left_index] \
                    and self.heap[right_index] > self.heap[index]:
                self._swap(index, right_index)
                if right_index < size // 2:
                    self._heapify(right_index, size)
            elif self.heap[left_index] > self.heap[index]:
                self._swap(index, left_index)
                if left_index < size // 2:
                    self._heapify(left_index, size)

    def delete_element_at_index(self, index):
        """
        Remove the element at the specified index
        """
        if index >= self.length():
            return

        self.heap[index] = float("inf")
        self.swim_up(index + 1)
        self.extract_root()

    def _swim_up(self, index):
        """
        Method to swim up if the children are greater the root
        Args:
            index: Index of the children
            (Here we need to pass 1 based index instead of 0 based index
            so that it will be easy for us to find the parrent)
        Example:
                            6
                       5        4
                   3        2       1
            In the above heap root will be self.heap[0]
            consider elements 5,4 are in respective index 2,3 the parrent node
            will be (children_idex/2) - 1 = (2-1) - 1 => 0
        """
        if index == 1:
            return
        parent = (index // 2)
        if self.heap[parent - 1] > self.heap[index - 1]:
            return
        self._swap(parent - 1, index - 1)
        self._swim_up(index=parent)
