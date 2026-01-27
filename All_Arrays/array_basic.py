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
