#Bubble Sort
def bubbleSort(list):
    count=0
    for j in range(len(list)-1):
        for i in range(len(list)-1-j):
            count+=1
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
               

    print("Number of evalutions: ",count)           
    return list
list=[1,5,3,2,0,8]
print("Given unsorted list is: ",list)   
print("Sorted list: ",bubbleSort(list))