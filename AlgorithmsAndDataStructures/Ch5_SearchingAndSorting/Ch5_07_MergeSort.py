def mergeSort(aList):
    print("Splitting ",aList)
    if len(aList)>1:
        mid = len(aList)//2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                aList[k]=leftHalf[i]
                i=i+1
            else:
                aList[k] = rightHalf[j]
                j = j + 1
            k += 1

        while i < len(leftHalf):
            aList[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            aList[k] = rightHalf[j]
            j += 1
            k += 1

    print("Merging ",aList)


dataSet = [10,9,8,7,6,5,4,3,2,1]
mergeSort(dataSet)
