n = int(input())
a = []
while len(a) < n:
    s = input().strip()
    string = ""
    for i in s + " ":
        if i.isdigit():
            string += i
        elif string:
            a.append(int(string))
            string = ""
        if len(a) == n:
            break
 
for _ in range(n):
    for i in range(n - 1):
        if a[i] % 2 == a[i + 1] % 2 and a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
 
for x in a:
    print(x, end=" ")