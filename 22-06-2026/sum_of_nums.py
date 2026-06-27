n  = input("enter : ")
while int(n) > 9:
    sum = 0
    for i in str(n):
        sum += int(i)
    n = sum
print(n)

# TC : O(logn)