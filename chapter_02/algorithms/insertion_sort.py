# Insertion sort is an efficient algorithm for sorting a small number of elements.

def insertion_sort(A, n):
    """Sort a list of elements

    Args:
        A (list or numpy array): an array of integers
        n (int): length of the array, A
    """

    for i in range(1, n):
        key = A[i]

        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key
