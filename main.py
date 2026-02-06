from data import arr1, arr2
from utils import (
    add_arrays,
    sub_arrays,
    mul_arrays,
    div_arrays,
    difference_array,
    total_sum,
    total_product
)

print("Array 1:", arr1)
print("Array 2:", arr2)

print("---------------------------")

print("Addition:", add_arrays(arr1, arr2))
print("Subtraction:", sub_arrays(arr1, arr2))
print("Multiplication:", mul_arrays(arr1, arr2))
print("Division:", div_arrays(arr1, arr2))

print("---------------------------")

print("Difference of arr1:", difference_array(arr1))
print("Difference of arr2:", difference_array(arr2))

print("---------------------------")

print("Sum of arr1:", total_sum(arr1))
print("Sum of arr2:", total_sum(arr2))

print("---------------------------")

print("Product of arr1:", total_product(arr1))
print("Product of arr2:", total_product(arr2))

print("---------------------------")
print("All operations performed successfully!")
