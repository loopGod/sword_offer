strlist=[]
def allpl(sl,i): #全排列
    if i>=len(sl):
        strlist.append(list(map(int,' '.join(list(map(str,sl))).strip().split())))
        return
    for j in range(i,len(sl)):
        sl[j],sl[i]=sl[i],sl[j]
        allpl(sl, i+1)
        sl[j],sl[i]=sl[i],sl[j]
    return
#allpl([1,2,3,4],0)
#print(strlist)
#eoor(10)

def plnum(pllist): #顺序对的对数
    dp=[0 for _ in range(len(pllist))]
    dp[len(pllist)-1]=0
    
    for i in range(len(pllist)-1)[::-1]:
        count=0
        for j in range(i+1,len(pllist)):
            if pllist[i]>pllist[j]:
                count+=1
        dp[i]=count
    return sum(dp)

nk=list(map(int,input().split()))
n,k=nk[0],nk[1]
Atmp=[i for i in range(1,n+1)]
Atmp2=[]
A=list(map(int,input().split()))
for ai in Atmp:
    if ai not in A:
        Atmp2.append(ai)

allpl(Atmp2,0)
num=0
B=[0 for i in range(len(A))]
for i in range(len(strlist)):
    for j in range(len(A)):
        if A[j]==0:
            B[j]=strlist[i].pop(0)
        else:
            B[j]=A[j]
    if plnum(B)==k:
        num+=1
print(num)
#strlist
