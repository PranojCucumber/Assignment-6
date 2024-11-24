# Data Structures and Algorithms Implementation

This project implements and analyzes various data structures and algorithms in Python, divided into two main parts:
1. Selection algorithms comparison (Deterministic vs Randomized)
2. Basic data structures implementation

## Part 1: Selection Algorithms

### Overview
Implements and compares two selection algorithms:
- Deterministic Algorithm (Median of Medians)
- Randomized Algorithm (Randomized Quickselect)

### Requirements
- Python 3.x
- NumPy
- Pandas
- Time (built-in)
- Random (built-in)

### How to Run
1. Ensure all required packages are installed:
```bash
pip install numpy pandas
```

2. Run the script:
```bash
python assignment6_part1.py
```

### Key Findings
#### Time Complexity Analysis
- **Deterministic Algorithm (Median of Medians)**: O(n)
- **Randomized Algorithm (Quickselect)**: O(n) expected, O(n²) worst case
- **Space Complexity**: O(log n) for both algorithms

#### Performance Comparison
1. **General Trends**:
   - Deterministic algorithm shows consistent linear growth
   - Randomized algorithm performs faster in practice
   - Both algorithms scale well with input size

2. **Input Distribution Impact**:
   - Both algorithms handle sorted, reverse sorted, and random inputs effectively
   - Minimal performance variation across different distributions

3. **Scaling Behavior**:
   - Small inputs (n=10): Performance difference negligible
   - Large inputs (n=10,000): Randomized algorithm ~2x faster

## Part 2: Data Structures Implementation

### Overview
Implements fundamental data structures:
- Dynamic Array
- Matrix
- Stack
- Queue
- Singly Linked List
- Tree

### How to Run
```bash
python assignment6_part2.py
```

### Data Structures Performance Analysis

#### Time Complexity Summary
| Operation  | Array     | Stack | Queue | Linked List |
|------------|-----------|--------|--------|-------------|
| Insert     | O(n)*     | O(1)   | O(1)   | O(1)        |
| Delete     | O(n)*     | O(1)   | O(1)   | O(n)**      |
| Access     | O(1)      | O(1)   | O(1)   | O(n)        |
| Traverse   | O(n)      | O(n)   | O(n)   | O(n)        |

\* For insertion/deletion in middle  
\** For deletion by value

### Implementation Details

#### Array Class
```python
# Usage example:
array = Array()
array.insert(0, 5)  # Insert value 5 at index 0
array.access(0)     # Access value at index 0
array.delete(0)     # Delete value at index 0
```

#### Stack Class
```python
# Usage example:
stack = Stack()
stack.push(5)       # Add element
value = stack.pop() # Remove and return top element
top = stack.peek()  # View top element without removing
```

#### Queue Class
```python
# Usage example:
queue = Queue()
queue.enqueue(5)    # Add element to queue
value = queue.dequeue() # Remove and return first element
front = queue.peek()    # View first element without removing
```

#### Linked List Class
```python
# Usage example:
linked_list = SinglyLinkedList()
linked_list.insert(5)   # Insert value
linked_list.delete(5)   # Delete value
elements = linked_list.traverse() # Get all elements
```

### Trade-offs and Recommendations

1. **Memory Usage**:
   - Arrays: Continuous memory allocation, efficient for fixed-size data
   - Linked Lists: Dynamic memory allocation, better for frequent size changes

2. **Use Case Recommendations**:
   - Use Arrays when:
     - Random access is frequent
     - Size is relatively stable
     - Memory is not constrained
   
   - Use Linked Lists when:
     - Frequent insertions/deletions at the beginning
     - Dynamic size requirements
     - Memory fragmentation is a concern

   - Use Stacks/Queues when:
     - LIFO/FIFO operations are needed
     - Simple push/pop operations are primary

## Conclusions
- Randomized selection algorithm generally outperforms deterministic approach
- Choice of data structure should be based on specific use case requirements
- Consider time complexity trade-offs when selecting appropriate data structure

## Contributing
This project is part of an academic assignment. Please refer to your institution's academic integrity guidelines before using or modifying this code.
