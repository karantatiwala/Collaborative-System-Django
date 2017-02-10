array = map(int, raw_input().split(' '))

k = max(array)
# x= array[len(array)]

for i in range(0, len(array)):
	if array[i] == k:
		break

p = len(array) - i -1

print p