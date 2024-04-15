class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
def fractionalKnapsack(sack_capacity, arr):
	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True) 
	finalvalue = 0.0
	for item in arr:
		if item.weight <= sack_capacity:
			sack_capacity -= item.weight
			finalvalue += item.profit
		else:
			finalvalue += item.profit * sack_capacity / item.weight
			break
	print(finalvalue)
	
sack_capacity = 50
arr = [Item(10, 2), Item(15, 5), Item(20, 4)]
fractionalKnapsack(sack_capacity, arr)


arr=[2,5,3,4,0]
sum=0
for i in range(len(arr)):
    sum += arr[i]*i
print("brute force",sum)

arr.sort()
sum=0
for i in range(len(arr)):
    sum += arr[i]*i
print("greedy",sum)

array_one=[7,5,4,1]
array_two=[6,17,9,3]
sum=0
array_one.sort()
array_two.sort(reverse=True)
for i in range(len(array_one)):
    sum += array_one[i]*array_two[i]
print(sum)
