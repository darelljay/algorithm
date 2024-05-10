n, k = map(int, input().split())
li = list(map(int, input().split()))
count = 0

for i in range(n - 1, 0, -1):
    idx = li.index(max(li[:i + 1]))
    if idx != i:
        li[idx], li[i] = li[i], li[idx]
        count += 1
        if count == k:
            print(li[idx], li[i])
            exit()
print(-1)
