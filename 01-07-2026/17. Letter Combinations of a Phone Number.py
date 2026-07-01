def combination(s):
    dic = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
    }
    res = []
    def backtracking(i,path):
        if i == len(s):
            res.append(path)
            return 
        for v in dic[s[i]]:
            backtracking(i+1,path+v)
    backtracking(0,'')
    return res