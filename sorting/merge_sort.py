to_sort = [5, 9, 12, 6, -3, 14, 13, 12, 0]
#to_sort = [3,2,1]

# main loop splits into left and right, calls merge on left then right
# merge compares first of left and first of right
# append the whole list based on place
# if there is anything left finish it out

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
            
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

def merge_sort(to_sort):
    if len(to_sort) <= 1:
        return to_sort
    
    left = []
    right = []
    
    for i in range(len(to_sort)):
        if i % 2 == 0:
            left.append(to_sort[i])
        else:
            right.append(to_sort[i])
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


        
print merge_sort(to_sort)
