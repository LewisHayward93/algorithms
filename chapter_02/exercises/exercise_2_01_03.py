# rewrite the insert ion sort procedure to sort intio monotonically decreatind instead of monotonically increasing order

def insertion_sort(A, n):
    """Sort a list of elements

    Args:
        A (list or numpy array): an array of integers
        n (int): length of the array, A
    """

    for i in range(1, n):
        key = A[i]

        j = i - 1

        # changing the check from A[j] > key to < key will reverse the order
        while j >= 0 and A[j] < key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key


arr = [31, 41, 59, 26, 41, 58]
insertion_sort(arr, len(arr))
print(arr)  # [59,58,41,41,31,26]
