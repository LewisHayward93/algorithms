# Sum-array loop invariant

```
sum-array(A,n)
    sum = 0
    for i = 1 to n
        sum = sum + A[i]
    return sum
```

- Initialisation: prior to the first interation of the loop, the value of sum is 0 which holds true for the totla sum of all values (none so far) which have been summed.
- Maintenance: after the first iteration, sum = A[0] which holds true for the sum of all elements in checked in the array so far ahead of the next iteration.
- Termination: after each elements has been iterated, the value of i reaches n, the last elements in the array. The value of sum has now had each of the elements added to the variable sum and therefore hold the total sum of the array. Hence the algorithm is correct.
