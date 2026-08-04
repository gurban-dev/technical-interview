For a sorted array, searching can be carried out
with the binary search algorithm.

The binary search algorithm has a time complexity of O(log n).

First step: you check n items but throw away half → n/2.

Next step: you check n/2 and throw away half → n/4.

Then n/8, n/16, … until only 1 item is left.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

n = 16

16 / 2 -> 8
8 / 2 -> 4
4 / 2 -> 2
2 / 2 -> 1

log₂(16) = 4

2^4 = 16

It took 4 times to divide 16 by 2 repeatedly until reaching
1, which is why log₂(16) = 4.

So the question is:
How many times can you divide n by 2 before you reach 1?

The answer is log₂(n).
That's why the time complexity is O(log n).
'''

'''
Suppose you had an array of four billion elements.

log₂(n) means to what power must I raise 2 to get n?
log₂(8) = 3 because 2³ = 8.

log₂(16) = 4 because 2⁴ = 16.

2^31 = 2 147 483 648

2^32 = 4 294 967 296

Think of log₂(n) as "how many times can I cut the
array in half before I get down to 1 element?"

For 2^32, exactly 32 cuts.

log₂(4,000,000,000) ≈ 31.89735285

For 4 000 000 000, it's just a tiny bit fewer cuts (≈ 31.9),
but we round up to 32 because in practice you still need up
to 32 steps.

log₂(4 000 000 000) = 32

2 ^ 32 = 4 294 967 296