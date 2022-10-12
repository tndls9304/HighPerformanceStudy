# Chapter 4: Dictionary and Set

### Simple Definition

Dictionary: hash table which has key-value pairs \
Set: hash table which has only value

- no duplicated key
- use large memory for saving every element
- time-dependency is depends on hash function

### Time complexity for operation
- Search
  - search with key: O(1)
  - search with value: O(N)

- Edit
  - add / insertion: O(1)
  - removal / deletion: O(1) (Not just change the value as NULL, specific value)

### Size increase
Triple the size whenever 2/3 of hash table is full\
starts with the size 8\
8, 18, 39, 81, 165, 333, 669, 1341, 2685, 5373, ...

## Storing logic
non-sequential data - (save) -> sequential memory

index(of array) = hash(key) & mask

### Elements
- In memory Elements
  - key array (list is not hashable, since value can be changed)
  - value array
  - index hash table (only store index of array)

- Proving 
  - the function that calculates new index

- Load-factor
  - how the data in hash table is distributed in unique
  - related to entropy of hash function
