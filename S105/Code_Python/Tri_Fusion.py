def Tri_Fusion(List):
    if len(List) > 1:
        center = len(List)//2
        Left = List[:center]
        Right = List[center:]
        Tri_Fusion(Left)
        Tri_Fusion(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                List[k] = Left[i]
                i += 1
            else:
                List[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):
            List[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            List[k] = Right[j]
            j += 1
            k += 1

    return List

