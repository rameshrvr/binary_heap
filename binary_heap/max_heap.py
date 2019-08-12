from binary_heap import BinaryHeap


def heap_sort(data):
    """
    Method to sort the list of integers using heap sort Algorithm
    Args:
        data: list of integers to be sorted
    Return:
        list of sorted integers
    """
    # Create a Max heap object
    heap_obj = MaxHeap(data)
    size = heap_obj.length()
    # Iterate elements from n to 1 (0 based indexing)
    for index in reversed(range(1, (size))):
        # In Max heap largest elemnt will be in root. So swap
        # the root element with last element of heap
        heap_obj._swap(index, 0)
        # Reduce the heap size by 1
        size -= 1
        # Swim down the root element to its heap position (heapify)
        heap_obj._heapify(index=0, size=size)
    # Now the heap has sorted elements
    return heap_obj.elements()


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

        l_index = self._left_child_index(index)
        r_index = self._right_child_index(index)
        largest_index = index
        if l_index < size and self.heap[l_index] > self.heap[index]:
            largest_index = l_index
        if r_index < size and self.heap[r_index] > self.heap[largest_index]:
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
