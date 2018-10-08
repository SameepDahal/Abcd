t=int(input())
for i in range(t):
    easy=0
    hard=0
    n,p=map(int,input().split())
    c=list(map(int,input().split()))
    for i in c:
        if i*10<=p:
            hard+=1
        elif i*2>=p:
            easy+=1
    if hard==2 and easy==1:
        print("yes")
    else:
        print('no')