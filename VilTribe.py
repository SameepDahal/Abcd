t=int(input())
for i in range(t):
    s=input()
    Aturn=False
    Bturn=False
    Noone=True
    Acount=0
    Bcount=0
    loop=0
    for i in s:
        if i=='A':
            if not Aturn:
                Acount+=1
            else:
                loop+=1
            if Noone:
                Aturn=True
                Noone=False
            elif Bturn:
                Aturn=True
                Bturn=False
                loop=0
            else:
                Acount+=loop
                loop=0
        elif i=='.' and not Noone:
            loop+=1
        elif i=='B':
            if not Bturn:
                Bcount+=1
            else:
                loop+=1
            if Noone:
                Bturn=True
                Noone=False
            elif Aturn:
                Bturn=True
                Aturn=False
                loop=0
            else:
                Bcount+=loop
                loop=0
    print(Acount,Bcount)