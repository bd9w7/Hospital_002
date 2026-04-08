# Cocktail Sort (Bidirectional Bubble Sort)
# Time Complexity: O(n²)
def cocktail_sort(arr):
    # Handle empty array
    if not arr:
        return []
        
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        # Left to right
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        # Right to left
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        start += 1
    return arr
