import numpy as np 

array1D =np.array([1,2,3,4,5,6,7,8,9,10])
array2D=np.array([[11,12,13,14,15],[16,17,18,19,20]])

print("\n1D Array: ", array1D)
print("2D Array: ", array2D)


array1D_2=np.array([10,12,14,16,18,20,11,13,19,15])

print("\nArray 1: ", array1D)
print("Array 2: ", array1D_2)

print("\nAdding two arrays:",array1D+array1D_2)
print("Subtracting two arrays:",array1D-array1D_2)
print("Multiplying two arrays:",array1D*array1D_2)
print("Dividing two arrays:",array1D/array1D_2)


print("\nMax of 1D array:",array1D.max())
print("Min of 1D array:",array1D.min())
print("Mean of 1D array:",array1D.mean())
print("Sum of 1D array:",array1D.sum())

print("\nMax of 2D array:",array2D.max())
print("Min of 2D array:",array2D.min())
print("Mean of 2D array:",array2D.mean())
print("Sum of 2D array:",array2D.sum())


reshape_1d_to_2d=array1D.reshape(2,5)
print("\n1D to 2D(Reshaped (2,5)):",reshape_1d_to_2d )
reshape_2d_to_1d=array2D.reshape(10)
print("2D to 1D(Reshaped (10)):",reshape_2d_to_1d )
reshape_2D=array2D.reshape(5,2)
print("2D Reshaped (2,5)-(5,2): ",reshape_2D)

print("\nSlicing of 1D(5-8): ",array1D[5:8])
print("Slicing of 2D: ",array2D[1:2,1:3])

print("\n1D Element at (4): ", array1D[4])
print("2D Element at (1,2): ", array2D[1,2])