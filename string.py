print('Enter a string')
A = raw_input().strip()
print('Enter a substring')
x = raw_input().strip()

count = 0
for i in range(len(A) - len(x) + 1):
    if A[i:i+len(x)] == x:
        count += 1
print (count)