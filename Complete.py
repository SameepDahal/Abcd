t=int(input())
for i in range(t):
    easy=0
    hard=0
    n,p=map(int,input().split())
    c=list(map(int,input().split()))
    for i in c:
        if i<=p//10:
            hard+=1
        elif i>=p//2:
            easy+=1
    if hard==2 and easy==1:
        print("yes")
    else:
        print('no')