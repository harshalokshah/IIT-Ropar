'''# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)


# Driver code
array = [10, 7, 8, 9, 1, 5]
N = len(array)
    # Function call
quicksort(array, 0, N - 1)
print('Sorted array:')
for x in array:
    print(x, end=" ")

# This code is contributed by Adnan Aliakbar
'''
def find_max_min(arr, low, high):
    if low == high:  # If there is only one element
        return arr[low], arr[low]



    else:
        mid = (low + high) // 2

        # Divide the array into two halves and recursively find max and min in each half
        max1, min1 = find_max_min(arr, low, mid)
        max2, min2 = find_max_min(arr, mid + 1, high)

        return max(max1, max2), min(min1, min2)

# Driver code
arr = [1000, 11, 445, 1, 330, 3000,3025]
max_num, min_num = find_max_min(arr, 0, len(arr) - 1)
print("Maximum element:", max_num)
print("Minimum element:", min_num)
