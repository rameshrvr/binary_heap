Binary Heap
###########

.. image:: https://img.shields.io/badge/binary_heap-1.0.4-green.svg
  :target: https://pypi.org/project/binary-heap/
.. image:: https://travis-ci.org/rameshrvr/binary_heap.svg?branch=master
    :target: https://travis-ci.org/rameshrvr/binary_heap


Python library which helps in forming Binary Heaps (Min, Max) using list data structure.
This library provides the below Heap specific functions.

*heap_sort*
	Sort the given list of elements using Heap Sort Algorithm

*heapify*
	Convert list of elements to Heap data structure (MinHeap/MaxHeap)

*add_element*
	Add single/list of elements to Heap

*get_root_value*
	Returns root value of the Heap without removing the element
	Minimum value for Min Heap, Maximum value for Max Heap

*extract_root*
	Extract root element from Heap and reform the Heap

*search_value*
	Searches the value in heap and returns index.
	if same element is present multiple times, first occurring index is returned

*delete_element_at_index*
	Remove the element at the specified index and reform the Heap


For example function invocations, plesae see the tutorial.

.. contents::


Installation
============

install from pypi using pip::

	$ pip install binary_heap

or easy_install::

	$ easy_install binary_heap

or install from source using::

	$ git clone https://github.com/rameshrvr/binary_heap.git
	$ cd binary_heap
	$ pip install .


Tutorial
========

1. Heap Sort (Sort the list using heap sort algorithm)

.. code-block:: python

	Rameshs-MBP:binary_heap ramesh_rv$ python3
	Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
	[Clang 6.0 (clang-600.0.57)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>>
	>>> from binary_heap import heap_sort
	>>>
	>>> data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	>>>
	>>> heap_sort(data)  # Returns sorted list in ascending order
	[1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
	>>> 
	>>> heap_sort(data, reverse=True)  # Returns sorted list in decsnding order
	[16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
	>>> 



2. Min Heap (Heap where the data in parent node is lesser than the data in child node)

.. code-block:: python
	
	Rameshs-MBP:binary_heap rameshrv$ python3
	Python 3.7.2 (default, Dec 27 2018, 07:35:06) 
	[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 
	>>> from binary_heap import MinHeap
	>>>
	>>> min_heap = MinHeap([4, 3, 6, 8, 11])  # Create an object for Min Heap
	>>>
	>>> min_heap.length()  # Returns size of the heap
	5
	>>> min_heap.elements()
	[3, 4, 6, 8, 11]
	>>>
	>>> min_heap.add_element(1)  # Add a single element to Heap
	>>>
	>>> min_heap.elements()
	[1, 4, 3, 8, 11, 6]
	>>>
	>>> min_heap.add_element([1, 14, 7, 5])  # Add list of elements to Heap
	>>>
	>>> min_heap.elements()
	[1, 4, 1, 7, 5, 6, 3, 14, 8, 11]
	>>>
	>>> min_heap.extract_root()  # Extract root element from Heap and retrun it. In this case its the minimum element
	1
	>>>
	>>> min_heap.elements()
	[1, 4, 3, 7, 5, 6, 11, 14, 8]
	>>>
	>>> min_heap.get_root_value()  # Returns the root value (minimum value) without removing it from Heap
	1
	>>>
	>>> min_heap.search_value(value=5)  # Returns index of the searched value. -1 if there is no such value in Heap
	4
	>>> min_heap.search_value(value=7)
	3
	>>> min_heap.search_value(value=16)
	-1
	>>>
	>>> min_heap.delete_element_at_index(3)  # Remove the element at the specified index
	>>>
	>>> min_heap.elements()
	[1, 4, 3, 8, 5, 6, 11, 14]
	>>> 



3. Max Heap (Heap where the data in parent node is greater than the data in child node)

.. code-block:: python

	Rameshs-MBP:binary_heap rameshrv$ python3
	Python 3.7.2 (default, Dec 27 2018, 07:35:06) 
	[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 
	>>> from binary_heap import MaxHeap
	>>>
	>>> max_heap = MaxHeap([4, 3, 6, 8, 11])  # Create an object for Max Heap
	>>>
	>>> max_heap.elements()  # Returns size of the heap
	[11, 8, 6, 4, 3]
	>>>
	>>> max_heap.add_element(13)  # Add a single element to Heap
	>>>
	>>> max_heap.elements()
	[13, 8, 11, 4, 3, 6]
	>>>
	>>> max_heap.add_element([1, 14, 7, 5])  # Add list of elements to Heap
	>>>
	>>> max_heap.elements()
	[14, 13, 11, 8, 5, 6, 1, 4, 7, 3]
	>>>
	>>> max_heap.extract_root()  # Extract root element from Heap and retrun it. In this case its the maximum element
	14
	>>>
	>>> max_heap.elements()
	[13, 8, 11, 7, 5, 6, 1, 4, 3]
	>>>
	>>> max_heap.get_root_value()  # Returns the root value (maximum value) without removing it from Heap
	13
	>>> 
	>>> max_heap.search_value(value=11)  # Returns index of the searched value. -1 if there is no such value in Heap
	2
	>>> max_heap.search_value(value=1)
	6
	>>> max_heap.search_value(value=14)
	-1
	>>>
	>>> max_heap.delete_element_at_index(3)  # Remove the element at the specified index
	>>>
	>>> max_heap.elements()
	[13, 8, 11, 4, 5, 6, 1, 3]


Development
===========

After checking out the repo, `cd` to the repository. Then, run `pip install .` to install the package locally. You can also run `python (or) python3` for an interactive prompt that will allow you to experiment.

To install this package onto your local machine, `cd` to the repository then run `pip install .`. To release a new version, update the version number in `setup.py`, and then run `python setup.py register`, which will create a git tag for the version, push git commits and tags, and push the package file to [PyPI](https://pypi.org).


Contributing
============

Bug reports and pull requests are welcome on GitHub at https://github.com/rameshrvr/binary_heap. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


License
========

The package is available as open source under the terms of the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0).


Code of Conduct
===============

Everyone interacting in the Binary Heap project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/rameshrvr/binary_heap/blob/master/CODE_OF_CONDUCT.md).


misc
========

:license:
  * GPL-3.0

:authors:
  * Ramesh RV
  * Adithya KS
