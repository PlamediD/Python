#an algorithm for insertion sort.
#Basically, this sort works by starting at index 1, s
# hifting that value to the left until it is sorted relative to all values to the left, 
# and then moving on to the next index position and 
# performing the same shifts until the end of the list is reached. 
# The following animation also shows how insertion sort is done.

def insertionSort(unsortedList):
    count=0
    indexingLength=range(1,len(unsortedList))
    for i in indexingLength:
        valueToSort=unsortedList[i]

        while unsortedList[i-1]>valueToSort and i>0:
            unsortedList[i],unsortedList[i-1]=unsortedList[i-1],unsortedList[i]
            i=i-1
            count+=1

    print("# of iterations: ",count)
    return unsortedList

givenList=[5,8,10,0,1,4,3,6,2,1]
sortedList=insertionSort(givenList)
print(sortedList)
