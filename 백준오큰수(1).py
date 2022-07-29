-L = int(input())

num = list(map(int, input().split()))

stack = [num[0]]
l = 0

for i in range(1, L):
    
    if num[i-1] > num[i]:
        stack.append(num[i])
    else: 
        j = i-1
        k = 0
        n = num[i]

        while j >= l and num[j] < num[i]: 
            stack.pop()
            k += 1
            j -= 1 
     
        l = i

        for _ in range(k+1):
            stack.append(n)
        
for _ in range(L):
    if num[_] == stack[_]:
        stack[_] = -1

print(" ".join(map(str, stack)))    

#반례
# 9 7 5 3 6 8 10 
# -1 -1 6 6 8 10 -1