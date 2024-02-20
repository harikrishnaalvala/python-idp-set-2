def encoding(s,t):
    if len(s)!=len(t): 
        return "No"
    diff=(ord(s[0])-ord(t[0]))%26
    for i in range(len(s)):
        K=(ord(s[i])-ord(t[i]))%26
        if K!=diff:
            return "No"
    return "Yes"

s=list(input()) 
t=list(input()) 
res=encoding(s, t) 
print (res)
