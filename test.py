arr1 = [[1, 2, 3, 4, 5, 6],
        [1, 8, 9, 1, 2, 3],
        [1, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6]]

arr1_cols = []
for i in range(len(arr1[0])):
    arr1_cols.append([str(row[i]) for row in arr1])
    arr1_cols[-1] = ''.join(arr1_cols[-1])
    print(arr1_cols[-1])

decimal_val = int(arr1_cols[0], 2)
print(decimal_val)