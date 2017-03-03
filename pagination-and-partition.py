# Parts a flat array into an array of chunk of sizes page_size.
def paginate(arr, page_size=3):
	pages = []
	start = 0
	end = 0
	for index, value in enumerate(arr):
		end = index+page_size
		if index % page_size == 0:
			block = arr[start:end]
			pages.append(block)
			start = end
	return pages

# Parts a flat array into an array of chunks, each with size n_parts
def partition(arr, n_parts=2):
	return paginate(arr, int(len(arr)/n_parts))
