# Longest Consecutive Sequence

**Difficulty:** Medium

**Pattern:** Hash Set

## Problem

Given an unsorted array of integers `nums`, return the length of the longest sequence of consecutive integers.

A consecutive sequence consists of numbers that differ by exactly **1**.

The algorithm must run in **O(n)** time.

---

## Examples

### Example 1

```text
Input:
nums = [100, 4, 200, 1, 3, 2]

Output:
4

Explanation:
The longest consecutive sequence is:
[1, 2, 3, 4]
```

---

### Example 2

```text
Input:
nums = [0,3,7,2,5,8,4,6,0,1]

Output:
9
```

---

### Example 3

```text
Input:
nums = []

Output:
0
```

---

## Constraints

```text
0 <= nums.length <= 100000
-10^9 <= nums[i] <= 10^9
```

---

# Algorithm

The solution uses a **Hash Set** to achieve constant-time lookups.

Instead of expanding from every number, we only start building a sequence when the current number is the **first element** of that sequence.

A number is considered the start of a sequence if:

```text
num - 1 is not in the set
```

For every starting number:

1. Count consecutive numbers (`num + 1`, `num + 2`, ...).
2. Track the sequence length.
3. Update the maximum length found.

Since every number is visited at most once during sequence expansion, the overall complexity remains linear.

---

# Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | **O(n)**   |
| Space  | **O(n)**   |

---

# Why Hash Set?

A Hash Set provides **O(1)** average-time membership checks.

Without it, searching for the next consecutive number would require scanning the array, resulting in **O(n²)** complexity.

---

# Key Insight

Instead of expanding from every number:

```text
100
4
200
1
3
2
```

we only expand from numbers that **do not have a predecessor**.

Example:

```text
1 → start
2 → skip (1 exists)
3 → skip (2 exists)
4 → skip (3 exists)
```

This prevents counting the same sequence multiple times.

---

# Implementations

This problem has been implemented in multiple backend languages:

* ✅ Python
* ✅ TypeScript
* ✅ C#
* ✅ Go

Each implementation follows the same algorithm while using language-specific idioms and standard libraries.

---

## Language Comparison

Although the algorithm is identical in every implementation, each language offers different syntax, standard libraries, and idioms.

| Concept          | Python                | TypeScript                   | C#                             | Go                         |
| ---------------- | --------------------- | ---------------------------- | ------------------------------ | -------------------------- |
| Hash Set         | `set[int]`            | `Set<number>`                | `HashSet<int>`                 | `map[int]struct{}`         |
| Loop             | `for num in nums_set` | `for (const num of numsSet)` | `foreach (var num in numsSet)` | `for num := range numsSet` |
| Membership Test  | `num in nums_set`     | `numsSet.has(num)`           | `numsSet.Contains(num)`        | `_, ok := numsSet[num]`    |
| Maximum          | `max(a, b)`           | `Math.max(a, b)`             | `Math.Max(a, b)`               | `if current > max { ... }` |
| Dictionary / Map | `dict`                | `Map<K, V>`                  | `Dictionary<TKey,TValue>`      | `map[K]V`                  |
| Time Complexity  | O(n)                  | O(n)                         | O(n)                           | O(n)                       |
| Space Complexity | O(n)                  | O(n)                         | O(n)                           | O(n)                       |

---

## Language Notes

### Python

* Built-in `set` provides concise and expressive syntax.
* Membership checks are clean with `in`.
* Ideal for interview speed and readability.

### TypeScript

* Uses the ES6 `Set` collection.
* Membership checks use `.has()`.
* Common choice for Node.js backend development and NestJS.

### C#

* Uses `HashSet<T>` from `System.Collections.Generic`.
* Strong typing and excellent performance.
* Common in enterprise backend applications with ASP.NET Core.

### Go

* Go has no built-in set type.
* A set is commonly implemented using:

```go
map[int]struct{}
```

where `struct{}` occupies zero bytes, making it the idiomatic and memory-efficient choice.

---

## Common Algorithm

Every implementation follows the same four steps:

1. Store all numbers in a Hash Set.
2. Iterate through each unique number.
3. Start a sequence only if the previous number (`num - 1`) does not exist.
4. Count consecutive numbers while updating the maximum sequence length.

The only differences between implementations are the language-specific collection types and syntax. The algorithm, complexity, and reasoning remain identical across all four languages.


---

# Interview Topics

This problem tests knowledge of:

* Hash Set
* Hash Table lookup
* Time complexity optimization
* Linear-time algorithms
* Problem-solving with unordered data

---

# Related Problems

* Top K Frequent Elements
* Contains Duplicate
* Happy Number
* Longest Substring Without Repeating Characters

All of these rely heavily on efficient use of hash-based data structures.
