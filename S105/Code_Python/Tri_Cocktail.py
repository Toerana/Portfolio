def Tri_Cocktail(List):
    lengt = len(List)
    left = 0
    right = lengt - 1
    while left < right:
        for i in range(left, right):
            if List[i] > List[i + 1]:
                List[i], List[i + 1] = List[i + 1], List[i]
        right -= 1
        for i in range(right, left, -1):
            if List[i - 1] > List[i]:
                List[i], List[i - 1] = List[i - 1], List[i]
        left += 1
    return List

