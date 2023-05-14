def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def test():
    arr = input("请输入要排序的数字，以空格分隔：").split()
    arr = [int(x) for x in arr]
    sorted_arr = selection_sort(arr)
    print("排序后的结果为：", sorted_arr)

test()
