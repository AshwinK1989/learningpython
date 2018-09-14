def even_nums(nums):
	return nums%2==0

nums=[1,2,3,4,5,6]

print(list(filter(even_nums,nums)))