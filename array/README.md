Investigate:
Arrays hold values of the same type at contiguous memory
locations.

In an array, we're usually concerned about two things -
the position/index of an element and the element itself.

In Python, and in also JavaScript, arrays (lists in Python)
have a dynamic size which means that you don't need to have
a size defined beforehand when creating the array.

**Time Complexity for Array Operations**

<ins>Access: O(1)</ins>

No matter how large the size of the array is (n), the time it
takes to access an element at a certain index remains the same.
<br>
<br>
<ins>Search on an unsorted array: O(n)</ins>

Must check each element one by one (linear search).

O(n) in worst case.
<br>
<br>
<ins>Search on a sorted array: O(log n)</ins>

Can use binary search (divide-and-conquer).

Cuts search space in half each step.

O(log n) in worst case.
<br>
<br>
<ins>Insertion at the beginning or middle of the array: O(n)</ins>

Requires shifting all later elements one position right.

Worst case: shifting n elements.
<br>
<br>
<ins>Insertion at the end of the array: O(1)</ins>

If there's empty space at the end of the array
(capacity not full), inserting means:

Place the new element in the next free slot.

Update the array’s size counter.

This takes the same amount of time regardless of the size
of the array (n).
<br>
<br>
<ins>Removal: O(n)</ins>

Removal would require shifting all the subsequent elements
to the left by one and that takes O(n)
<br>
<br>
<ins>Removal at the end of the array: O(1)</ins>

When you remove the last element, there are no elements after
it to shift.

So the operation is simply:

1. Reduce the array’s size counter by 1.

2. Overwrite the last slot with null/None (depending on the language).

This operation is constant time (O(1)), regardless of array size.
