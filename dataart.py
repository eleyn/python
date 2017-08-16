with open('data.txt', 'r') as myfile:       # read file 
    data = myfile.read() 

a = [int(x) for x in data.split(' ')] # make string into array

def bubblesort(lst):
    i = 0
    while i < len(a):
        j = 0
        while j < len(a) - 1:
            if a[j] > a[j+1]:
                x = a[j]
                a[j] = a[j+1]
                a[j+1] = x
            j = j + 1
        i = i + 1

def quicksort(lst):
    helper(lst, 0, len(lst) - 1)

def helper(lst, start, end):
    
    if start < end:
        splitpoint = partition(lst, start, end)

        helper(lst, start, splitpoint-1)
        helper(lst, splitpoint + 1, end)
        


def partition(lst, start, end):
    pivot = lst[start]

    left = start + 1
    right = end

    f = False
    while f != True:
        while left <= right and lst[left] <= pivot:
            left = left + 1
        while right >= left and lst[right] >= pivot:
            right = right - 1

        if right < left:
            f = True
        else:
            x = lst[left]
            lst[left] = lst[right]
            lst[right] = x

    x = lst[start]
    lst[start] = lst[right]
    lst[right] = x

    return right
    
    
def find(array, x):
    for i in range(len(a) - 1):
        if a[i] == x:
            return True

    return False 

def binarysearch(array, x):
    
    while len(array) != 0:
        mid = len(array) // 2
        if x < array[mid]:
            array = array[:mid]
        elif x > array[mid]:
            array = array[mid+1:]
        else:
            return True
        
    return False
        
        
 
    



            
