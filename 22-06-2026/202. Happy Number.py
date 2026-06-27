"""n = 19
def happy(n):
    arr = []
    x = 0
    for i in str(n):
        x += int(i) ** 2
    if x in arr:
        return False
    arr.append(x)
    return True
while n > 9:
    n = happy(n)
    if n:
        print("Yes")
        break"""


n = 19
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    n += sum(int(i) ** 2 for i in str(n))

if n == 1:
    print("Yes, it is a happy number")
else:
    print("No, it is not a happy number")


prime
Amstrong
fibonacci
factorial
ugly
