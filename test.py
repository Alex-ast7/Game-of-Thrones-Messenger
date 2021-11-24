n, w = map(int, input().split())
l, r = map(int, input().split())
s = [0 for i in range(r + 1)]
numbers = list(map(int, input().split()))
for i in range(n):
    x = numbers[i]
    s[x] = x
s[l] = l
s[r] = r
last = 0
for i in range(r + 1):
    if s[i] != 0:
        last = s[i]
    else:
        s[i] = last
while True:
    m = (r - l) // 2
    if (s[m] - l) > w:
        r = m
    elif (r - s[m]) > w:

print(s)