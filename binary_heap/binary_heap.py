

class BinaryHeap():
    def __init__(self, heap):
        self.heap = heap

    def elements(self):
        """
        Method to return elements of Binary Heap
        """
        return self.heap

    def length(self):
        """
        Method to return length of Binary Heap
        """
        return len(self.heap)

    def heapify(self):
        """
        Brief:
            Method to convert Array into Binary Heap
        Args:
            heap: Array to be converted
        """
        size = self.length()
        for index in reversed(range(size // 2)):
            self._heapify(index=index, size=size)

    def swim_up(self, index):
        self._swim_up(index=index)

    def get_root_value(self):
        """
        Return root value of the heap
        """
        return self.heap[0]

    def add_element(self, element):
        """
        Brief:
            Method to add element / elements to heap
        Args:
            element: Could be a single number of array of numbers
        """
        if isinstance(element, list):
            for _element in element:
                self.heap.append(_element)
                self.swim_up(self.length())
        else:
            self.heap.append(element)
            self.swim_up(self.length())

    def extract_root(self):
        """
        Remove root element from the heap and return it
        """
        self._swap(0, self.length() - 1)
        result = self.heap.pop()
        self._heapify(index=0, size=self.length())
        return result

    def _swap(self, index1, index2):
        """
        Brief:
            Swap two elements in the given heap
        Args:
            index1: Index of the 1st element to be swapped
            index2: Index of the 2nd element to be swapped
        """
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    def _left_child_index(self, index):
        """
        Method to get the left child index of any given node
        """
        return (2 * index) + 1

    def _right_child_index(self, index):
        """
        Method to get the right child index of any given node
        """
        return (2 * index) + 2
