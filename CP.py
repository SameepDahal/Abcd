t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=list(map(int,input().split()))
    leftend=-1
    rightend=-1
    error=False
    for c in s[:len(s)-1]:
        if c>b:
            if rightend==-1 or c<rightend:
                rightend=c
            else:
                error=True
                break
        elif c<b:
            if leftend==-1 or leftend<c:
                leftend=c
            else:
                error=True
                break
    if error:
        print("NO")
    else:
        print("YES")