target=input("target= ")

nums = [2, 5, 3, 7, 3, 8]
#print(target)#

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j]==int(target):
            print(i,j) 
        else:
            print("None")  
            break  
'''
nums = [2, 5, 3, 7, 3, 8]
target = nums[1] + nums[3]
index1 = nums.index(5)
index2 = nums.index(7)
print("%s, %s" % (index1, index2))


nums = [2, 5, 3, 7, 3, 8]
target = nums[2] + nums[3]
index1 = nums.index(3)
index2 = nums.index(7)
print("%s, %s" % (index1, index2))


nums = [1, 5, 3, 1, 5, 1]
target = 12
index1 = nums[1] + nums[10]
index1 = nums.index(3)
index2 = nums.index(10)
print("%s, %s" % (index1, index2))
'''