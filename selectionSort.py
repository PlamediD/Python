#Selection sort works by iterating through the list, finding the minimum value, 
# and moving it to the beginning of the list. Then, ignoring the first position, which is now sorted, 
# iterate through the list again to find the next minimum value and move it to index 1. 
# This continues until all values are sorted. Here's an animation and a video of selection sort
#By Plamie D

def selectionSort(unsortedList):
    indexingLength=range(0,len(unsortedList)-1)
    for i in indexingLength:
        min_value=i

        for j in range(i+1,len(unsortedList)-1):
            if(unsortedList[j]<unsortedList[min_value]):
                min_value=j

        if min_value !=i:
            unsortedList[min_value],unsortedList[i]=unsortedList[i],unsortedList[min_value]

    return unsortedList

givenList1=[9,10,11,3,4,2,0,1,6,7,8]
print("The given unsorted list is: ",givenList1)
selectionSort1=selectionSort(givenList1)
print("The sorted list is: ",selectionSort1)

givenList2=[8,14,1,13,4,2,0,19,6,7,8]
print("The given unsorted list is: ",givenList2)
selectionSort2=selectionSort(givenList2)
print("The sorted list is: ",selectionSort2)