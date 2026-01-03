def selection_sort(arr):
    size=len(arr)
    for i in range (size-1):
        min_index=i
        for j in range (min_index,size):
            if arr[j]<arr[min_index]:
                min_index=j

        if i!=min_index:
            arr[i],arr[min_index]=arr[min_index],arr[i]

if __name__=="__main__":
    elements=[78,12,15,8,99,32,19,10]
    selection_sort(elements)
    print(elements)
