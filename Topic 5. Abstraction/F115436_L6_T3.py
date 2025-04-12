import sys

search_list = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272,
               288, 289, 290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510,
               513, 514, 519, 521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713,
               731, 739, 740, 842, 858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988]


def diho_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        if mid == 0 or arr[mid - 1] != target:
            return mid
        return diho_search(arr, target, left, mid - 1)
    elif arr[mid] < target:
        return diho_search(arr, target, mid + 1, right)
    else:
        return diho_search(arr, target, left, mid - 1)


target_value = int(sys.argv[1])
left_index = 0
right_index = len(search_list) - 1
result = diho_search(search_list, target_value, left_index, right_index)

if result != -1:
    print(f"found at {result}")
else:
    print("not found")