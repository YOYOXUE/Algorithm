import random
def QuickSort(arr):
    less=[]
    equal=[]
    greater=[]

    if len(arr)>1:
        pivot=arr[0]
        for x in arr:
            if x<pivot:
                less.append(x)
            if x==pivot:
                equal.append(x)
            if x>pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return arr
    
if __name__=='__main__':
    L=20
    arr=[random.randint(1,100) for i in range(L)]
    print(arr)
    print(QuickSort(arr))
