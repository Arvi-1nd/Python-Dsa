###################### Array Basic Problems ############################################
############################################################
###################
#########
####
##
#


# Printing the Alternatives

fresh_list = [10,20,30,40,50,60,70,80]

alter_pack = []

for i in range(0,len(fresh_list),2):
    alter_pack.append(fresh_list[i])
    
print(alter_pack)


# Using recursion

def getAlternativeRec(arr,idx,res):
    if idx < len(arr):
        res.append(arr[idx])
        getAlternativeRec(arr,idx+2,res)

def getAlternative(arr):
    res = []
    getAlternativeRec(arr,0,res)
    return res
    
array = [10,20,30,40,50]
print(getAlternative(array))


# To check if Sorted
def checkSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

print(checkSorted([4,5,6,7,8]))
print(checkSorted([3,2,1,0]))

#Recursive solution

def recsorted(arr, idx=0):
    if idx == len(arr)-1:
        return True
    if arr[idx] > arr[idx + 1]:
        return False
    return recsorted(arr,idx+1)

print(recsorted([45,34,21,11]))

#Removing duplicates

def removeduplicates(arr):
    duplicates = set()
    idx = 0
    
    for i in range(len(arr)):
        if  arr[i] not in duplicates:
            duplicates.add(arr[i])
            arr[idx] = arr[i]
            idx += 1
    return idx

arr = [1,2,1,2,3,2,3,5,4]

new_size = removeduplicates(arr)

for i in range(new_size):
    print(arr[i], end=" ")


# for printing all subArrays

subarr = [1,2,3,4]

net = len(subarr)
for i in range(net):
    for j in range(i, net):
        for k in range(i, j+1):
            print(subarr[k], end =" ")
        print()
    

# Reversing an array

def reverse_arr(arr):
    i,j = 0, len(arr)-1
    
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
        
    return arr

print(reverse_arr([4,3,2,1]))

# Rotate an array

def rotateArr(arr,d):
    n = len(arr)
    
    for _ in range(d):
        
        last = arr[n-1]
        
        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = last
    
    
arr = [1, 2, 3, 4, 5, 6]
d = 2
rotateArr(arr,d)

for i in range(len(arr)):
    print(arr[i], end=" ")