
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    increasing = decreasing = True
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        else:
             lst[i] < lst[i - 1]
             increasing = False
    return increasing or decreasing

# Examples
print(monotonic([1, 1, 3, 100]))  
print(monotonic([11, 1, -9, -10]))  
print(monotonic([2, 3, 2, 3]))  
print(monotonic([1,2,3,4,5]))

 

