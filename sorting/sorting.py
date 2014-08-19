import random

def merge_sort(lst):

    def merge(left, right):
        result = []
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    result.append(left[0])
                    left = left[1:]
                else:
                    result.append(right[0])
                    right = right[1:]
            elif len(left) > 0:
                result.append(left[0])
                left = left[1:]
            elif len(right) > 0:
                result.append(right[0])
                right = right[1:]
        return result


    if len(lst) <= 1:
        return lst

    middle = len(lst) / 2
    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



def fisher_yates_shuffle(lst):

    for i in range(len(lst)):
        rand_ind = random.randrange(0, len(lst) - 1)
        hold = lst[i]
        lst[i] = lst[rand_ind]
        lst[rand_ind] = hold

    return lst



orig =[ random.randrange(1, 30) for i in range(1, 20) ]
print orig
print merge_sort(orig)


print range(1, 20)
print fisher_yates_shuffle(range(1, 20))
print merge_sort(fisher_yates_shuffle(range(1, 20)))
