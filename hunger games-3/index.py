def hunger_game(n,m,s):
    ch=m%n
    p=ch+s-1
    last=p%n 
    if last==0:
        return n 
    return last
n=int(input())
for i in range(n):
    n,m,s=map(int,input().split())
    result=hunger_game(n,m,s)
    print(result)
