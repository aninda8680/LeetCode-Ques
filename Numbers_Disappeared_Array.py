def findDisappearedNumbers(nums):
    not_p = []
    for i in range (1, len(nums)+1):
        if i not in nums:
            not_p.append(i)
    return not_p
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))


