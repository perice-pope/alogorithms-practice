# pull apart here... cheers

def insertionSort(nums): 
  # print(nums)
  for i in range(1,len(nums)):
    key = nums[i] # each element 
    j = i-1 # the item to the left of i 
    print(nums[j+1])

nums = [1,25,0]
insertionSort(nums)

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
    # move things forward and backwards for fun! :D We movin baby! 