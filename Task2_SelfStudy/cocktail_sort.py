def cocktail_sort(arr, key=None):
    # Cocktail sort (bidirectional bubble sort) with optional key function
    if len(arr) <= 1:
        return arr.copy()
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    left = 0
    right = n - 1
    swapped = True

    def get_key(x):
        return key(x) if key is not None else x

    while swapped and left < right:
        swapped = False
        # bubble the maximum to the right
        for i in range(left, right):
            if get_key(sorted_arr[i]) > get_key(sorted_arr[i+1]):
                sorted_arr[i], sorted_arr[i+1] = sorted_arr[i+1], sorted_arr[i]
                swapped = True
        right -= 1
        if not swapped:
            break
        swapped = False
        # bubble the minimum to the left
        for i in range(right, left, -1):
            if get_key(sorted_arr[i]) < get_key(sorted_arr[i-1]):
                sorted_arr[i], sorted_arr[i-1] = sorted_arr[i-1], sorted_arr[i]
                swapped = True
        left += 1
    return sorted_arr