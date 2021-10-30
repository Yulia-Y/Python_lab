from math import ceil 
n = int(input())
bigList = [input().split() for i in range(n)] 
midpointList = []  
fashionList = [] 
oneListInt = [int(j) for i in bigList for j in i]  
oneListStr = [j for i in bigList for j in i]  
 
for numsList in bigList: 
    numsList = [int(i) for i in numsList] 
    numsList.sort()  
    midpoint = numsList[ceil((len(numsList) - 1) / 2)]  
    midpointList.append(midpoint) 
    print(midpoint, end=' ') 
print()
 
for nums in bigList:  
    fashion = [nums.count(nums[i]) for i in range(len(nums))]  
    print(nums[fashion.index(max(fashion))], end=' ') 
    fashionList.append(nums[fashion.index(max(fashion))])  
print()
 
midpointList.sort()
midpoint = midpointList[ceil((len(midpointList) - 1) / 2)]  
print(midpoint)
 
fashion = [fashionList.count(fashionList[i]) for i in range(len(fashionList))]
print(fashionList[fashion.index(max(fashion))])  
 
oneListInt.sort()
midpoint = oneListInt[ceil((len(oneListInt) - 1) / 2)] 
print(midpoint)
 
fashion = [oneListStr.count(oneListStr[i]) for i in range(len(oneListStr))]  
print(oneListStr[fashion.index(max(fashion))])