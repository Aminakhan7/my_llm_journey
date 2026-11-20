import numpy as np

# 1. Array Indexing (2D)

arr1_index = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print("\n--- Array Indexing ---")
print("Element at row 2, column 3:", arr1_index[1, 2])
print("Entire second row:", arr1_index[1])
print("Entire first column:", arr1_index[:, 0])


# 2. Sorting Arrays

arr2_sort = np.array([
    [1, 6, 2, 4],
    [5, 6, 7, 8]
])

print("\n--- Sorting Array ---")
print("Original array:")
print(arr2_sort)

print("Sorted array row-wise:")
print(np.sort(arr2_sort))


# 3. Sorting Along Axis 0 and Axis 1

unsorted_arr = np.array([
    [34, 1],
    [1, 2],
    [2, 3]
])

print("\n--- Sorting Along Axis 0 ---")
print(np.sort(unsorted_arr, axis=0))

print("\n--- Sorting Along Axis 1 ---")
print(np.sort(unsorted_arr, axis=1))


# 4. Filtering Even Numbers

even_arr = np.array([1, 2, 3, 4, 5, 6, 6, 7])

even_num = even_arr[even_arr % 2 == 0]

print("\n--- Even Numbers ---")
print(even_num)

odd_num = even_arr[even_arr % 2 != 0]

print("\n--- Odd Numbers ---")
print(odd_num)


# 5. Basic 1D Indexing

arr_basic = np.arange(12)

print("\n--- Basic Indexing ---")
print("Original array:", arr_basic)
print("First element:", arr_basic[0])
print("Last element:", arr_basic[-1])
print("Element at index 5:", arr_basic[5])


# 6. Negative Indexing and Slicing

start_negative = np.array([1, 2, 3, 4, 5])

window_negative = start_negative[-1:-4:-2]

print("\n--- Negative Slicing ---")
print("Original array:", start_negative)
print("Negative slicing result:", window_negative)


# 7. Normal Slicing

start_slice = np.array([1, 2, 3, 4, 5])

window_slice = start_slice[1:4:2]

print("\n--- Normal Slicing ---")
print("Original array:", start_slice)
print("Slicing result:", window_slice)


# 8. Negative Indexing with Step

arr_step = np.array([10, 20, 30, 40, 50, 60])

step_result = arr_step[-2::-2]

print("\n--- Negative Indexing with Step ---")
print("Original array:", arr_step)
print("Result:", step_result)


# 9. 2D Array Indexing

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n--- 2D Array Indexing ---")

print("First row:", data[0])
print("Second row:", data[1])

print("First column:", data[:, 0])
print("Second column:", data[:, 1])
print("Third column:", data[:, 2])

print("Specific element (row 3, column 2):", data[2, 1])


# 10. Selecting Rows and Columns

print("\n--- Row and Column Selection ---")

print("First two rows, all columns:")
print(data[0:2, 0:3])

print("\nFirst two rows, columns 2 and 3:")
print(data[0:2, 1:3])