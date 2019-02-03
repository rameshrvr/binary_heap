from unittest import TestCase

from binary_heap import MinHeap, MaxHeap


class TestMinHeap(TestCase):
    def setUp(self):
        self.array = [4, 3, 6, 8, 11]

    def test_min_heap_property(self):
        min_heap = MinHeap(self.array)
        length = min_heap.length()
        elements = min_heap.elements()
        for i in range(0, length):
            current_value = elements[i]
            left_index = (2 * i) + 1
            right_index = (2 * i) + 2
            if left_index <= length - 1:
                self.assertLessEqual(current_value, elements[left_index])
            if right_index <= length - 1:
                self.assertLessEqual(current_value, elements[right_index])

    def test_min_heap_count_and_elements(self):
        min_heap = MinHeap(self.array)
        self.assertEqual(5, min_heap.length())
        self.assertEqual([3, 4, 6, 8, 11], min_heap.elements())

    def test_add_element_to_minheap(self):
        min_heap = MinHeap(self.array)
        min_heap.add_element(1)
        self.assertEqual(6, min_heap.length())
        self.assertEqual([1, 4, 3, 8, 11, 6], min_heap.elements())
        self.assertEqual(1, min_heap.get_root_value())

    def test_add_array_of_elements_to_minheap(self):
        min_heap = MinHeap(self.array)
        min_heap.add_element([1, 14, 7, 5])
        self.assertEqual(9, min_heap.length())
        self.assertEqual([1, 4, 3, 5, 11, 6, 14, 8, 7], min_heap.elements())
        self.assertEqual(1, min_heap.get_root_value())

    def test_delete_element_at_index_minheap(self):
        min_heap = MinHeap(self.array)
        min_heap.delete_element_at_index(3)
        self.assertEqual(4, min_heap.length())
        self.assertEqual([3, 4, 6, 11], min_heap.elements())

    def test_search_value_minheap(self):
        min_heap = MinHeap(self.array)
        index = min_heap.search_value(8)
        self.assertEqual(index, 3)
        index = min_heap.search_value(12)
        self.assertEqual(index, -1)

    def test_extract_root_value_minheap(self):
        min_heap = MinHeap(self.array)
        self.assertEqual(3, min_heap.extract_root())
        self.assertEqual([4, 8, 6, 11], min_heap.elements())

    def test_multiple_operations_minheap(self):
        min_heap = MinHeap(self.array)
        min_heap.add_element(5)
        self.assertEqual([3, 4, 5, 8, 11, 6], min_heap.elements())
        self.assertEqual(3, min_heap.extract_root())
        self.assertEqual([4, 6, 5, 8, 11], min_heap.elements())
        min_heap.add_element([1, 3, 5, 6])
        self.assertEqual([1, 5, 3, 6, 11, 5, 4, 8, 6], min_heap.elements())
        self.assertEqual(1, min_heap.extract_root())
        self.assertEqual(3, min_heap.extract_root())
        self.assertEqual([4, 5, 5, 6, 11, 8, 6], min_heap.elements())
        self.assertEqual([4, 5, 5, 6, 6, 8, 11], sorted(min_heap.elements()))


class TestMaxHeap(TestCase):
    def setUp(self):
        self.array = [4, 3, 6, 8, 11]

    def test_max_heap_property(self):
        max_heap = MaxHeap(self.array)
        length = max_heap.length()
        elements = max_heap.elements()
        for i in range(0, length):
            current_value = elements[i]
            left_index = (2 * i) + 1
            right_index = (2 * i) + 2
            if left_index <= length - 1:
                self.assertGreaterEqual(current_value, elements[left_index])
            if right_index <= length - 1:
                self.assertGreaterEqual(current_value, elements[right_index])

    def test_max_heap_count_and_elements(self):
        max_heap = MaxHeap(self.array)
        self.assertEqual(5, max_heap.length())
        self.assertEqual([11, 8, 6, 4, 3], max_heap.elements())

    def test_add_element_to_maxheap(self):
        max_heap = MaxHeap(self.array)
        max_heap.add_element(13)
        self.assertEqual(6, max_heap.length())
        self.assertEqual([13, 8, 11, 4, 3, 6], max_heap.elements())
        self.assertEqual(13, max_heap.get_root_value())
        self.assertEqual([13, 8, 11, 4, 3, 6], max_heap.elements())

    def test_add_array_of_elements_to_maxheap(self):
        max_heap = MaxHeap(self.array)
        max_heap.add_element([1, 14, 7, 5])
        self.assertEqual(9, max_heap.length())
        self.assertEqual([14, 8, 11, 7, 3, 1, 6, 4, 5], max_heap.elements())
        self.assertEqual(14, max_heap.get_root_value())

    def test_delete_element_at_index_maxheap(self):
        max_heap = MaxHeap(self.array)
        max_heap.delete_element_at_index(2)
        self.assertEqual(4, max_heap.length())
        self.assertEqual([11, 8, 3, 4], max_heap.elements())

    def test_search_value_maxheap(self):
        max_heap = MaxHeap(self.array)
        index = max_heap.search_value(8)
        self.assertEqual(index, 1)
        index = max_heap.search_value(44)
        self.assertEqual(index, -1)

    def test_extract_root_value_maxheap(self):
        max_heap = MaxHeap(self.array)
        self.assertEqual(11, max_heap.extract_root())
        self.assertEqual([8, 4, 6, 3], max_heap.elements())

    def test_multiple_operations_maxheap(self):
        max_heap = MaxHeap(self.array)
        max_heap.add_element(5)
        self.assertEqual([11, 8, 6, 4, 3, 5], max_heap.elements())
        self.assertEqual(11, max_heap.extract_root())
        self.assertEqual([8, 5, 6, 4, 3], max_heap.elements())
        max_heap.add_element([11, 13, 5, 6])
        self.assertEqual([13, 6, 11, 5, 3, 6, 8, 4, 5], max_heap.elements())
        self.assertEqual(13, max_heap.extract_root())
        self.assertEqual(11, max_heap.extract_root())
        self.assertEqual([8, 6, 6, 5, 3, 4, 5], max_heap.elements())
        self.assertEqual([3, 4, 5, 5, 6, 6, 8], sorted(max_heap.elements()))
