def Asscookies(child,cookies):
    child.sort(reverse = True)
    cookies.sort(reverse = True)
    n = len(child)
    m = len(cookies)
    i,j = 0,0
    cnt = 0
    while i < n and j < m:
        if child[i]<= cookies[j]:
            j += 1
            cnt += 1
        i += 1
    return cnt
print(Asscookies(child=[1,2,3],cookies=[1,1]))
