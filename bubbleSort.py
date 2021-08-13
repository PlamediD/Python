def bubble(unsortedList):
    indexing_length = len(unsortedList) - 1 
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if unsortedList[i]>unsortedList[i+1]:
                sorted = False # These values are unsorted
                unsortedList[i], unsortedList[i+1] = unsortedList[i+1], unsortedList[i] #Switch these values
    return unsortedList # Return the sorted list.
givenList=[4,8,1,14,8,2,9,5,7,6,6]
print("The given unsorted list is: ",givenList)
print("The sorted list is: ",bubble(givenList))