# Parts a flat array into an array of of arrays, each with specified size. Includes the last inner array, even if not to size.
def paginate(arr, size=2):
	result = []
	start = 0
	end = 0
	
	for index, value in enumerate(arr):
		end = index+size
		if index % size == 0:
			block = arr[start:end]
			pages.append(block)
			start = end
	return pages

# Parts a flat array into an array of of arrays, where the size is calculated based on the number of elements in the flat array divided by partition size.
def partition(arr, size=3):
	return paginate(arr, int(len(arr)/size))

# Quick partitioning (~ ½ dt of partition(). Parts a flat array into an array of arrays, where the size is calculated based on the number of elements in the flat array divided by partition size. Doesn't include the last inner array, if not to size.
def q_partition(arr, size=3):
    result = []
    start = 0
    end = 0
    
    for i in range(int(len(arr)/size)):
        end = start + size
        result.append(arr[start:end])
        start = end
    return result
