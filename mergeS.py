# Merge Sort in Python

def merge_sort(arr):
    # If the array has more than one element
    if len(arr) > 1:
        # Find the middle index of the array
        mid = len(arr) // 2
        print('mid:', mid)
        # Divide the array into two subarrays using the middle index
        left_half = arr[:mid]
        print('Left Half:' , left_half)
        right_half = arr[mid:]
        print('Right Half:', right_half)

        # Recursively sort the left and right subarrays
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted subarrays into the original array
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            print('Merge two sorted subarays \n')
            print('i:', left_half, ' j:', right_half, ' k:', arr)

        # Copy any remaining elements of the left subarray into the original array
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            print('copy remaining elements of the left \n')
            print('i:', left_half, ' j:', right_half, ' k:', arr)

        # Copy any remaining elements of the right subarray into the original array
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            print('copy remaining elements of the right \n')
            print('i:', left_half, ' j:', right_half, ' k:', arr)


# Test the merge_sort function
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
