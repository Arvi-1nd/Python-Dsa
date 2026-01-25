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
