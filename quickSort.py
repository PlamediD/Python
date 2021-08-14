#The Quick Sort algorithm takes an item from the unsorted list and uses it as the 'pivot'
#  or the item to compare the remainder of the items in the list. 
# it does not compare by placing the items in lists according to if they are larger or smaller than the pivot value.
#repeat this process creating smaller and smaller lists until we have list values of one which have been sorted.

def quickSort(unsortedSequence):
    count=0
    length=len(unsortedSequence)

    #checkc to see if the sequence is empty or contains only 1 element
    #if it is the case, then simply return the given sequence
    if(length<=1):
        return unsortedSequence
    
    else:
        pivot=unsortedSequence.pop()

    elementsGreater=[]
    elementsSmaller=[]

    for element in unsortedSequence:
        if element>pivot:
            elementsGreater.append(element)

        else:
            elementsSmaller.append(element)

    #Descending order
    #return quickSort(elementsGreater)+[pivot]+quickSort(elementsSmaller)
    
    #Ascending order
    return quickSort(elementsSmaller)+[pivot]+quickSort(elementsGreater)

givenList=[5,12,3,6,2,1,6,8,9]
SortedList=quickSort(givenList)
print("Given unsorted list is: ", givenList)
print("New list with elements in ascending order: ", SortedList)
