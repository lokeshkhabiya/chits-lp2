# Implement Greedy search algorithm for Selection Sort.

def selectionSort(array):
    n = len(array)

    for i in range(n):
        # find the minimum element
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        # swap the found minimum element with the first element 
        array[i], array[min_index] = array[min_index], array[i]

    return array


# example 
print("Selection sort using greedy search algorithm: \n")
array = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print("Given array is: ", array, "\n")
print("Sorted array is: ", selectionSort(array))