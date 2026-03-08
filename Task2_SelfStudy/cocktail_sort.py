def cocktail_sort(arr, key=None):

    if len(arr) <= 1:
        return arr.copy()
    # Deep copy to avoid modifying the original list
    arr_sorted = arr.copy()
    n = len(arr_sorted)
    left = 0  # Left boundary
    right = n - 1  # Right boundary
    swapped = True  # Flag to indicate if a swap occurred

    # Custom key handling: convert elements to comparison values
    def get_key(x):
        return key(x) if key is not None else x

    while swapped and left < right:
        swapped = False
        # Traverse from left to right: bubble the maximum value to the right
        for i in range(left, right):
            if get_key(arr_sorted[i]) > get_key(arr_sorted[i+1]):
                arr_sorted[i], arr_sorted[i+1] = arr_sorted[i+1], arr_sorted[i]
                swapped = True
        right -= 1  # Move right boundary left, the maximum value is in place
        if not swapped:
            break
        swapped = False
        # Traverse from right to left: bubble the minimum value to the left
        for i in range(right, left, -1):
            if get_key(arr_sorted[i]) < get_key(arr_sorted[i-1]):
                arr_sorted[i], arr_sorted[i-1] = arr_sorted[i-1], arr_sorted[i]
                swapped = True
        left += 1  # Move left boundary right, the minimum value is in place
    return arr_sorted