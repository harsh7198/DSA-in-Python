k = int(input("Enter K : "))
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
if k > len(arr):
    print("Invalid input")
    exit()
win_sum = sum(arr[0:k])
max_sum = win_sum 

for i in range(k ,len(arr)):
    win_sum = win_sum - arr[i-k] + arr[i]
    max_sum = max(max_sum , win_sum)

print("Max sum is :",max_sum)