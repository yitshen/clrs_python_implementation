def bubblesort(inputList):
    for iii in range(len(inputList)):
        for jjj in range(iii):
            inputList[jjj], inputList[iii] = min(inputList[jjj], inputList[iii]), max(inputList[jjj], inputList[iii])
    return inputList
