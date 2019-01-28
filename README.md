# Binary Heap

Python library which helps in forming Binary Heaps (Min, Max) using list data structure.
This library provides the below Heap specific functions.

1. heapify - Convert list of elements to Heap data structure
2. add_element - Add single/list of elements to Heap
3. extract_root - Extract root element from Heap and reform the Heap

## Installation

install from pypi using pip
```
 $ pip install binary_heap
```

or easy_install
```
 $ easy_install binary_heap
```

or install from source using
```
 $ git clone https://github.com/rameshrvr/binary_heap.git
 $ cd binary_heap
 $ pip install .
```

### Tutorial

1. Min Heap (Heap where the data in parent node is lesser than the data in child node)
```python
Rameshs-MBP-ead8:binary_heap rameshrv$ python3
Python 3.7.2 (default, Dec 27 2018, 07:35:06) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from binary_heap import MinHeap
>>> min_heap = MinHeap([4, 3, 6, 8, 11])
>>> min_heap.length()
5
>>> min_heap.elements()
[3, 4, 6, 8, 11]
>>> min_heap.add_element(1)
>>> min_heap.elements()
[1, 4, 3, 8, 11, 6]
>>> min_heap.add_element([1, 14, 7, 5])
>>> min_heap.elements()
[1, 4, 1, 7, 5, 6, 3, 14, 8, 11]
>>> min_heap.extract_root()
1
>>> min_heap.elements()
[1, 4, 3, 7, 5, 6, 11, 14, 8]
>>> min_heap.get_root_value()
1
>>> 
```

2. Max Heap (Heap where the data in parent node is greater than the data in child node)
```python
Rameshs-MBP-ead8:binary_heap rameshrv$ python3
Python 3.7.2 (default, Dec 27 2018, 07:35:06) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from binary_heap import MinHeap
>>> max_heap = MaxHeap([4, 3, 6, 8, 11])
>>> max_heap.elements()
[11, 8, 6, 4, 3]
>>> max_heap.add_element(13)
>>> max_heap.elements()
[13, 8, 11, 4, 3, 6]
>>> max_heap.add_element([1, 14, 7, 5])
>>> max_heap.elements()
[14, 13, 11, 8, 5, 6, 1, 4, 7, 3]
>>> max_heap.extract_root()
14
>>> max_heap.elements()
[13, 8, 11, 7, 5, 6, 1, 4, 3]
>>> max_heap.get_root_value()
13
>>> 
```

## Development

After checking out the repo, `cd` to the repository. Then, run `pip install .` to install the package locally. You can also run `python (or) python3` for an interactive prompt that will allow you to experiment.

To install this package onto your local machine, `cd` to the repository then run `pip install .`. To release a new version, update the version number in `setup.py`, and then run `python setup.py register`, which will create a git tag for the version, push git commits and tags, and push the package file to [PyPI](https://pypi.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/rameshrvr/binary_heap. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The package is available as open source under the terms of the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0).

## Code of Conduct

Everyone interacting in the Binary Heap project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/rameshrvr/binary_heap/blob/master/CODE_OF_CONDUCT.md).
