def Tri_Insertion(List):
    lengt = len(List)
    for i in range(1, lengt):
        item = List[i]
        j = i-1
        while j >= 0 and item < List[j] :
                List[j + 1] = List[j]
                j -= 1
        List[j + 1] = item
    return List

