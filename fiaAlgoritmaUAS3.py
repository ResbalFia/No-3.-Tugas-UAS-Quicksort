def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x > pivot]     # > untuk urut besar → kecil
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort(left) + mid + quicksort(right)

data = [12, 45, 5, 67, 32, 66, 78, 10, 17, 9]
hasil = quicksort(data)

print("Hasil sorting (besar ke kecil):")
print(hasil)