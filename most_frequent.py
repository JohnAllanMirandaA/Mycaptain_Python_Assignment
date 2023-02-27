def most_frequent(arr, Len):
	d = {}
	for i in range(Len):
		if(arr[i] in d):
			d[arr[i]] = d[arr[i]] + 1
		else:
			d[arr[i]] = 1
	size = len(d)
	while (size > 0):
		currentMax = 0
		arg_max = 0
		for key, value in d.items():
			if (value > currentMax or (value == currentMax and key > arg_max)):
				arg_max = key
				currentMax = value
		print(f"{arg_max} = {currentMax}",end=" ")
		d.pop(arg_max)
		size -= 1
a=input("Enter a string: ")
Len=len(a)
most_frequent(list(a), Len)
