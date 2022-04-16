def findFibIndex(num):
    nums = [0, 1]
    while nums[-1] < num:
        nums.append(nums[-1]+nums[-2]) # last and second to last numbers are totaled and added to the list
    return nums.index(num) if num in nums else 0 # 0 is returned if num is not valid

print(findFibIndex(8))
