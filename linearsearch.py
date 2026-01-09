l=[1,2,'a',5,6,'b',9]     #linear-search Algorithm
target=9
for ind in range(len(l)-1):
    if l[ind] == target:
        print(ind)
        break
else:
    print(-1)  
    
l=[-17,-5,0,1,5,12,15,23]  #Binary-sort Algorithm
target=15
least=0
high=len(l)-1
while least <high:
    mid = (least+high)//2
    if l[mid] > target:
        high = mid-1
    if l[mid] < target:
        least = mid+1
    else:
        print(mid)
        break
else:
    print(-1) 
    
l=[12,33,15,17,3,9]   #Bubble-sort Algorithm
for ind1 in range(len(l)-1):
    for ind2 in range(len(l)-ind1-1):
        if l[ind2] > l[ind2+1]:
            l[ind2],l[ind2+1] = l[ind2+1],l[ind2]
print(l) 

l=[6,2,9,4,0,6]     #selection-sort Algorithm
for ind1 in range(len(l)-1):
    leng=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[leng] > l[ind2]:
            leng=ind2
    l[ind1],l[leng]=l[leng],l[ind1]
print(l) 

def quick(l):
    if len(l) <= 1:
        return l
    pivot=l[0]
    left= [ele for ele in l[1:] if ele < pivot]
    right = [ele for ele in l[1:] if ele >= pivot]
    return quick(left) + [pivot] + quick(right)
l=[2,6,-5,0,7,6,11,2] 
print(quick(l))            
