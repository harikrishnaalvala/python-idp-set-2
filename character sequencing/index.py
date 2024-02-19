s=list(map(int,input().split()))
output=""
for i in s:
    output+=chr(96+i)
print(output)
