# Notes

My own notes for the problems in this repo. I write them after
solving each one so I can come back and remember the idea.

---

## Warmup

**solveMeFirst** — return `a + b`. Just a syntax check.

**simpleArraySum** — `sum(ar)` does the loop for us in O(n).

**compareTriplets** — walk both lists position by position. If
`a[i] > b[i]` Alice scores; if `b[i] > a[i]` Bob does; ties give
nobody a point.

**aVeryBigSum** — same as `simpleArraySum`. Python integers grow
without overflow, so `sum()` works for huge values too.

**miniMaxSum** — total minus the max is the smallest sum of 4 of 5
numbers; total minus the min is the biggest. One pass for total.

**plusMinus** — count positives, negatives, and zeros in one pass,
then divide by `n`. `round(x, 6)` keeps 6 decimal places.

**staircase** — row `i` (1..n) has `n-i` spaces and `i` hashes.
String multiplication keeps it short.

**birthdayCakeCandles** — only the tallest candles can be blown
out, so find `max(candles)` and count how many match.

**timeConversion** — check the AM/PM suffix:
- AM and hour 12 → 00
- AM otherwise → drop the suffix
- PM and hour 12 → keep 12, drop the suffix
- PM otherwise → add 12 to the hour

---

## Arrays

**reverseArray** — `a[::-1]` is a reversed slice. O(n) time and space.

**rotateLeft** — `arr[d:] + arr[:d]` cuts at index `d` and swaps
the two halves. Cleaner than rotating one element at a time.

**matchingStrings** — for each query, count its occurrences with
`list.count`. O(q · n). A `Counter` from `collections` would make
it O(n + q), worth coming back to once I learn dictionaries.

**countingSort** — make a frequency table of size 100 (the problem
constraint). Use the value itself as the index. This is the first
half of full counting sort. O(n + k).

---

## Linked Lists

A linked list is a chain of nodes; each node has `data` and a
`next` pointer (or `None` at the end). Two patterns I keep using:

1. *Walk to the end* — `while current.next: current = current.next`
2. *Walk to one before a position* — `for i in range(position - 1)`,
   because to insert or delete at `p` I need the node at `p - 1`
   so I can rewire `.next`.

**printLinkedList** — start at head, print, follow `.next` until None.

**insertNodeAtTail** — walk to the last node, attach the new node.
If the list is empty, the new node is the head.

**insertNodeAtHead** — point the new node at the old head, return
the new node. O(1) — the cheapest insert.

**insertNodeAtPosition** — walk to `position - 1`, then splice:
```
new_node.next = current.next
current.next  = new_node
```

**deleteNode** — find the node before the one to remove, then skip
over it: `current.next = current.next.next`. Position 0 is special
— just return `head.next`.

---

## Sorting

Insertion sort is how I sort cards in my hand: pick the next card
and slide it left until it sits in the right spot. Worst case is
O(n²) but it's fast on small or already-sorted arrays and uses
O(1) extra memory.

Counting sort skips comparisons entirely. It uses the value itself
as an index into a frequency array, so it runs in O(n + k). Good
when the value range `k` is small.

**introTutorial** — `arr.index(V)` does a linear scan. Binary
search would be O(log n), but `index` is fine for small inputs.

**insertionSort1** — only the last element is out of place. Slide
it left while everything to its left is bigger, shifting those
elements right by one. Print after every shift to show the slide.

**insertionSort2** — same idea but applied to every position from
1 to n-1. Treat `arr[0..i-1]` as already sorted, then insert `arr[i]`.

**countingSort** — same bucket idea as in the arrays file. Index
into a length-100 list and increment.

**findMedian** — sort then take the middle element. O(n log n).
For odd-length arrays `len(arr) // 2` lands exactly in the middle.
