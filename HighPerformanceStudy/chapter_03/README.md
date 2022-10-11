# Chapter 3: List and Tuple

### Simple Definition
List: dynamic array\
Tuple: immutable static array

### Time complexity for operation

- Search
  - access by index: O(1)
  - access by value: O(log(n))
- Edit
  - addition: O(1)
  - insert: O(n)
  - removal / deletion: O(n)
  - sort: O(n log(n)) ([Timsort](https://en.wikipedia.org/wiki/Timsort))

### Other search approach

Change a list to a dictionary with unique key\
Since dictionary access is O(1)

- Caution!
  - changing a list to a dictionary is O(n)
  - check whether the list is sorted or not

## List vs. Tuple
### List
- can change the value after the list is generated
- add value or connect other list to the list

### Pre-allocation
List pre-(over-)allocate the memory for append operation

memory allocation equation
```python
# N: size of list
# M: new allocation size in the memory for the list
M = (N>>3) + (3 if N < 9 else 6)
# N: 0  1-4  5-8  9-16  17-25  25-35  36-46 ... 
# M: 0  4    8    16    25     35     46    ...
```
Test code
```python
allocated = 0
for new_size in range(100):
    if allocated < new_size:
        new_allocated = (new_size >> 3) + (3 if new_size < 9 else 6)
        allocated = new_size + new_allocated
    print(new_size, allocated)
```

List uses more memory than its length.\
Take care when you handle large list or append in the loop.

### Tuple
- cannot change the value after the tuple is generated
- no additional memory allocation for size N tuple
- lighter than the tuple

### Caching strategy
- save the tuple in cache memory whose length is lt 20
- store 20,000 tuples for each size
- faster access than the list
