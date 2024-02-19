def check_enemy(l):
    for num in l:
        if (l.count(num)==2):
            return num
def check_friend(l):
    n=len(l)
    for i in range(1,n+1):
        if i not in l:
            return i
l=list(map(int,input().split()))
enemy=check_enemy(l)
missing_friend=check_friend(l)
print(enemy,missing_friend)
