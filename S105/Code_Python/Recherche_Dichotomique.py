def dichotomique_iterative(List, x):
    start = 0
    end = len(List) - 1
    while start <= end:
        center = (end + start) // 2
        if List[center] < x:
            start = center + 1
        elif List[center] > x:
            end = center - 1
        else:
            return center
    return -1

def dichotomique_recursive(List, x, start=0, end= -5):
    if end == -5 :
        end = len(List)-1

    if start > end:
        return -1
    center = (end + start) // 2
    if List[center] == x:
        return center
    elif List[center] > x:
        return dichotomique_recursive(List, x, start, center-1)
    else:
        return dichotomique_recursive(List, x, center+1, end)


