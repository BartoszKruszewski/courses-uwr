def mergeSort(arr, temp_arr, left, right):
	inv_count = 0
	if left < right:
		mid = (left + right) // 2
		inv_count += mergeSort(arr, temp_arr,left, mid)
		inv_count += mergeSort(arr, temp_arr,mid + 1, right)
		inv_count += merge(arr, temp_arr, left, mid, right)
	return inv_count

def merge(arr, temp_arr, left, mid, right):
	i = left
	j = mid + 1
	k = left
	inv_count = 0
	while i <= mid and j <= right:
		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]

	return inv_count
