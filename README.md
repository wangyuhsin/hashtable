# HashTable

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A `HashTable` is a Python class that implements a basic hash table data structure. A hash table, also known as a hash map, is a data structure that provides efficient storage and retrieval of key-value pairs. It is commonly used when there is a need for fast lookup of values based on a given key.

## Introduction to Hash Tables

A hash table consists of an array of fixed-size buckets or slots and a hash function. The hash function takes a key as input and computes an index within the array where the corresponding value will be stored. The index is determined in such a way that it minimizes collisions, which occur when two different keys map to the same index.

The key advantage of a hash table lies in its ability to provide fast access to data. Instead of searching through all the elements, the hash function narrows down the search to a specific bucket or index, significantly reducing the time complexity. This makes hash tables ideal for scenarios that require frequent data access, such as caching, symbol tables, and database indexing.

Hash tables have an average time complexity of O(1) for insertion, deletion, and retrieval operations, making them highly efficient for large datasets.

## Example

Here's an example that demonstrates the usage of the `HashTable` class:

```python
from oohtable import HashTable

# Create a new hash table with 10 buckets
htable = HashTable(10)

# Add items to the hash table
htable['name'] = 'Amy'
htable['age'] = 27
htable['city'] = 'San Francisco'

# Retrieve an item from the hash table
name = htable['name']
print(name)  # Output: Amy

# Check if a key exists in the hash table
if 'city' in htable:
    print("City:", htable['city'])  # Output: City: San Francisco

# Iterate over the keys in the hash table
for key in htable:
    print(key)  # Output: name, age, city

# Retrieve all keys and items from the hash table
keys = htable.keys()
items = htable.items()
print(keys)  # Output: ['name', 'age', 'city']
print(items)  # Output: [('name', 'Amy'), ('age', 27), ('city', 'San Francisco')]
```

## Implementation Details

The `HashTable` class internally uses a dictionary (`dict`) to store the items. It utilizes the built-in `hash` function to calculate the hash value of a key and maps it to a specific bucket.

 Each bucket contains a list of key-value pairs.

The class overrides several special methods to provide convenient functionality, such as `__len__`, `__setitem__`, `__getitem__`, `__contains__`, `__iter__`, `keys`, `items`, `__repr__`, and `__str__`. These methods allow for easy manipulation and representation of the hash table.

Please note that this implementation does not handle collisions or resizing of the hash table. It serves as a basic demonstration of a hash table data structure in Python.

## License

This project is licensed under the [MIT License](link-to-license).

## Acknowledgments

The project structure is adapted from the MSDS 689 course materials provided by the University of San Francisco (USFCA-MSDS). Special thanks to the course instructors for the inspiration.
