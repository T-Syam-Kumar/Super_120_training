s = '12ag4aiff56fh'
num = ''
alp = ''
res = [0, '']

for i in s:
    if i.isdigit():
        if alp and len(alp) > len(res[1]):
            res[1] = alp
        alp = ''
        num += i
    else:
        if num and int(num) > res[0]:
            res[0] = int(num)
        num = ''
        alp += i

if num and int(num) > res[0]:
    res[0] = int(num)
if alp and len(alp) > len(res[1]):
    res[1] = alp

print(res)


i = 0
while i < len(s):
    num = alp = ''
    while s[i].isdigit():
        num += s[i]
        i += 1
    while i<len(s) and s[i].isalpha():
        alp += s[i]
        i += 1
    res[0] = res[0] if res[0] > int(num) else int(num)
    res[1] = res[1] if len(res[1]) > len(alp) else alp


# TC = SC = O(n)