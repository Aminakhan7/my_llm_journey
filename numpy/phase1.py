import numpy as np

# 1. Create an array
arr = np.arange(12)
print("Original array:")
print(arr)

# 2. Reshape
reshape = arr.reshape(3, 4)
print("\nReshaped array:")
print(reshape)

# 3. Flatten - returns a copy
flattened = reshape.flatten()
print("\nFlattened array:")
print(flattened)

# 4. Ravel - returns a view whenever possible
raveled = reshape.ravel()
print("\nRaveled array:")
print(raveled)

# 5. Transpose
transpose = reshape.T
print("\nTransposed array:")
print(transpose)

# 6. Stack
a = np.array([1, 2])
b = np.array([5, 6])

stacked = np.stack((a, b))
print("\nStacked array:")
print(stacked)
print("Stack shape:", stacked.shape)

# 7. Concatenate
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

concatenated = np.concatenate((a, b), axis=0)
print("\nConcatenated along axis 0:")
print(concatenated)

concatenated_axis1 = np.concatenate((a, b), axis=1)
print("\nConcatenated along axis 1:")
print(concatenated_axis1)