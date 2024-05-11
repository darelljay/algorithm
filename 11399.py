num = int(input())
arr = list(map(int,input().split()))
sumArr = []
sum = 0

arr.sort();

for i in range(len(arr)):
    if i > 0:
      sumArr.append(sumArr[i-1] +int(arr[i]))
    else:  
        sumArr.append(int(arr[i]))


for i in range(0,len(sumArr)):
   sum+=sumArr[i]

print(sum)