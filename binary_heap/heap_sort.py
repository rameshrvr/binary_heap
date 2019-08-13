from .max_heap import MaxHeap
from .min_heap import MinHeap


def heap_sort(data, reverse=False):
    """
    Method to sort the list of integers using heap sort Algorithm
    Args:
        data: list of integers to be sorted
    Return:
        list of sorted integers
    """
    # If reverse enabled use Min Heap else use Max Heap
    if reverse:
        heap_obj = MinHeap(data)
    else:
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
