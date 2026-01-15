c = 0
 
def merge(a, b):
    global c
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            c += len(a) - i
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
 
n = int(input())
A = list(map(int, input().split()))
r = mergeSort(A)
print(c)
print(*r)