#1
target=input("target= ")

nums = [2, 5, 3, 7, 3, 8]
#print(target)#

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j)  

#2
target=input("target= ")
nums = [2, 5, 3, 7, 3, 8]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j) 

#3
target=input("target= ")
nums = [1, 5, 3, 1, 5, 1]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j) 
        else:
            print("None")  
            break  


#4
target=input("target= ")
nums = [0, 0, 0, 0]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j) 
        else:
            print("None")  
            break  


#5
target=input("target= ")
nums = [1]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j) 
        else:
            print("None")  
            break  

#6
target=input("target= ")
nums = [1, 3, 2, 42, 1]

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j) 
        else:
            print("None")  
            break 

#7
target=input("target= ")
nums = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j) 
        else:
            print("None")  
            break 