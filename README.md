# Spiral Traversal of a Matrix

A Python implementation that reads a matrix in spiral order, moving across its boundaries layer by layer until every element has been visited.

## Overview

Spiral traversal starts at the top-left corner and follows four directions:

1. Left to right across the top row
2. Top to bottom along the right column
3. Right to left across the bottom row
4. Bottom to top along the left column

After each direction, the corresponding boundary moves inward. The process continues until there are no rows or columns left to process.

## How It Works

The program maintains four boundaries:

```python
top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1
```

These values define the current unvisited region of the matrix.

### 1. Traverse the Top Row

The elements between `left` and `right` are added from left to right.

```python
for col in range(left, right + 1):
    order.append(matrix[top][col])

top += 1
```

Once the row has been processed, `top` moves downward.

### 2. Traverse the Right Column

The next boundary is the right column:

```python
for row in range(top, bottom + 1):
    order.append(matrix[row][right])

right -= 1
```

Afterward, the `right` boundary moves one position inward.

### 3. Traverse the Bottom Row

If rows remain, the bottom row is processed from right to left:

```python
if top <= bottom:
    for col in range(right, left - 1, -1):
        order.append(matrix[bottom][col])

    bottom -= 1
```

The bottom boundary then moves upward.

### 4. Traverse the Left Column

Finally, if columns remain, the left column is processed from bottom to top:

```python
if left <= right:
    for row in range(bottom, top - 1, -1):
        order.append(matrix[row][left])

    left += 1
```

The left boundary moves inward, completing one spiral layer.

## Example

The program uses the following matrix:

```text
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
```

Its spiral traversal is:

```text
1, 2, 3, 4, 5,
10, 15, 20,
19, 18, 17, 16,
11, 6,
7, 8, 9,
14,
13, 12
```

The matrix and traversal call are defined in the program's `main()` function.

## Boundary Movement

The four boundaries gradually close in:

```text
top    → moves downward
bottom → moves upward
left   → moves right
right  → moves left
```

This prevents already-visited rows and columns from being processed again.

## Algorithm

1. Initialize the four matrix boundaries.
2. Traverse the top row from left to right.
3. Move the top boundary inward.
4. Traverse the right column from top to bottom.
5. Move the right boundary inward.
6. Traverse the bottom row from right to left when valid.
7. Move the bottom boundary inward.
8. Traverse the left column from bottom to top when valid.
9. Move the left boundary inward.
10. Repeat until the boundaries cross.

## Complexity

Let the matrix contain `M × N` elements.

| Metric          | Complexity |
| --------------- | ---------- |
| Time            | O(M × N)   |
| Auxiliary Space | O(M × N)   |

Every matrix element is visited once, while the `order` list stores the complete traversal result.

## Edge Case

An empty matrix or a matrix whose first row is empty returns an empty list immediately:

```python
if not matrix or not matrix[0]:
    return []
```

## Running the Program

Run:

```bash
python "Spiral Traversal of a Matrix.py"
```

The resulting spiral order is printed as a Python list.
