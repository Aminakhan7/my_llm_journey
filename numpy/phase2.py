import numpy as np


# 1. Concatenate 3D Arrays


arr1_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[12, 12, 14], [13, 16, 17]]
])

arr2_3d = np.array([
    [[7, 8, 9], [10, 11, 12]],
    [[14, 15, 16], [17, 18, 19]]
])

result_3d = np.concatenate((arr1_3d, arr2_3d), axis=2)

print("\n--- 3D Concatenation ---")
print(result_3d)
print("Shape of arr1:", arr1_3d.shape)
print("Shape of arr2:", arr2_3d.shape)
print("Result shape:", result_3d.shape)



# 2. Concatenate 1D Arrays


arr1_1d = np.array([10, 20, 30])
arr2_1d = np.array([40, 50, 60])

result_1d = np.concatenate((arr1_1d, arr2_1d))

print("\n--- 1D Concatenation ---")
print(result_1d)
print("Shape:", result_1d.shape)
print("Dimensions:", result_1d.ndim)



# 3. Stack vs Concatenate


stack_arr1 = np.array([1, 2, 3])
stack_arr2 = np.array([4, 5, 6])

# Stack adds a new axis
stack_result = np.stack((stack_arr1, stack_arr2), axis=1)

# Concatenate joins along an existing axis
concat_result = np.concatenate((stack_arr1, stack_arr2), axis=0)

print("\n--- Stack ---")
print(stack_result)
print("Shape:", stack_result.shape)

print("\n--- Concatenate ---")
print(concat_result)
print("Shape:", concat_result.shape)



# 4. Expand Dimensions (1D Array)


expand_arr_1d = np.array([1, 2, 3])

expand_result_1d = np.expand_dims(expand_arr_1d, axis=0)

print("\n--- Expand Dimensions (1D) ---")
print(expand_result_1d)
print("Shape:", expand_result_1d.shape)
print("Dimensions:", expand_result_1d.ndim)


# 5. Expand Dimensions (2D Array)


expand_arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

expand_result_2d = np.expand_dims(expand_arr_2d, axis=1)

print("\n--- Expand Dimensions (2D) ---")
print(expand_result_2d)
print("Shape:", expand_result_2d.shape)
print("Dimensions:", expand_result_2d.ndim)
print("Size:", expand_result_2d.size)