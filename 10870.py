n = int(input());

sum = 0 # 1 
n1 = 0  # 1
n2 = 1 # 1
arr = [];
if n<= 20:
     for i in range(0,n):
          sum = n1+n2
          arr.append(n1);
          arr.append(n2);
          arr.append(sum);
        #   print(n1,n2,sum)
          n1 = n2+sum
          n2 = n1 + sum
          
# print(arr)
print(arr[n]);

n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)
print(fibonacci[n])

# 0 1 3 1