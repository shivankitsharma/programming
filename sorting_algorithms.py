#selection sort
def selectionsort(arr):
	for i in range(len(arr)):
		minelementindex = i
		minelement = arr[i]
		for m in range(i+1,len(arr)):
			if arr[m] < minelement:
				minelement = arr[m]
				minelementindex = m
		arr[i],arr[minelementindex]=arr[minelementindex],arr[i]
	return arr

#bubble sort
def bubblesort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1,i,-1):
			if arr[j] < arr[j-1]:
				arr[j-1],arr[j]=arr[j],arr[j-1]
	return arr

#insertion sort
def insertionsort(arr):
	for i in range(len(arr)):
		j=i-1
		curr=arr[i]
		while j >=0 and arr[j] > curr:
			arr[j+1]=arr[j]
			j -=1
		arr[j+1] = curr
	return arr

#quick sort
def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if len(arr) == 1:
        return arr
    if low<high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
        


#merge sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
              arr[k] = l[i]
              i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k]=r[j]
            j += 1
            k += 1


#heap sort
def heapsort(arr):
    import heapq
    heapq.heapify(arr)
    result = []
    while len(arr) > 0:
        result.append(heapq.heappop(arr))
    return result
